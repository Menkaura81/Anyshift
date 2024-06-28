################################################################################################
# Gearbox module provides all the shifting logic to Anyshift software
#
# There is no warranty for the program, to the extent permitted by applicable law. Except 
# when otherwise stated in writing the copyright holders and/or other parties provide the
# program "as is" without warranty of any kind, either expressed or implied, including, but
# not limited to, the implied warranties of merchantability and fitness for a particular purpose.  
# The entire risk as to the quality and performance of the program is with you.  
# Should the program prove defective, you assume the cost of all necessary servicing, 
# repair or correction.
#
# 2023 Menkaura Soft
################################################################################################

import pygame  # Joystick input
import time  # Delays
from CtypeKeyPressSimulator import PressKey, ReleaseKey  # Low level key presses
import keyboard  # Normal key presses
from ReadWriteMemory import ReadWriteMemory  # Memory writing
import serial # Arduino serial comunication
from PlaySound import play_sound

# Flag for avoiding first shifting bug when running nascar mode 
first_time = True
# COM_PORT = "COM13"

# Mem mode joystick loop
def joystick_loop_mem(options):

    pygame.init()
    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
    #detect how many buttons has the joystick. It will be used later to detect multibutton presses
    numButtons = shifter.get_numbuttons()

    # Setting serial port for arduino
    arduino_conected = False
    try:
        arduino = serial.Serial(options['comport'], 9600)
        time.sleep(2)
        arduino.write(b'8')  # Light the display so the user can confirm it is working
        arduino_conected = True
    except:
        print(f"No arduino conected in {options['comport']}")

    # Create clutch joystick object and initialize it if clutch = true
    if options['clutch'] == 'True':
        clutch = pygame.joystick.Joystick(int(options['clutch_id']))
        clutch.init()
    clutch_pressed = False
    clutch_value = -((-2 * int(options['bitepoint'])) / 100 + 1)
        
    # Open DosBox process and check for process opened
    rwm = ReadWriteMemory()
    process = rwm.get_process_by_name(options['process'])
    process.open()        
    # Base address. Got from the pointer we have
    x_pointer = process.get_pointer(int(options['db_base_addr'], 16)) 
        
    if options['process'] == 'pcsx2.exe':
        # In pcsx2 1.6 is allways de same address
        address = x_pointer
    else:
        # Gear address is the base address plus the offset. This is the value we found in Cheat Engine
        address = process.read(x_pointer) + int(options['offset'], 16)        

    #region MEM MODE NO CLUTCH
    gear_selected = 0 
    if options['clutch'] == 'False':  # Doesn´t require clutch to shift          
        # Loop
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.

                if event.type == pygame.JOYBUTTONDOWN:
                    # Flag to detect if a defined key for changing gear is pressed
                    validKey = False
                    # Check for multibutton presses
                    buttons = 0
                    for i in range (numButtons):
                        if shifter.get_button(i) == True:
                            buttons += 1                    
                    if buttons == 1:
                        validKey = True

                    if shifter.get_button(options['first']) == True :
                        process.write(address, int(options['first_value']))
                        gear_selected = 1
                        if arduino_conected == True:
                            arduino.write(b'1')  # Send gear indicator data to arduino
                    if shifter.get_button(options['second']) == True:
                        process.write(address, int(options['second_value']))
                        gear_selected = 2
                        if arduino_conected == True:
                            arduino.write(b'2')  # Send gear indicator data to arduino
                    if shifter.get_button(options['third']) == True:
                        process.write(address, int(options['third_value']))
                        gear_selected = 3
                        if arduino_conected == True:
                            arduino.write(b'3')  # Send gear indicator data to arduino
                    if shifter.get_button(options['fourth']) == True:
                        process.write(address, int(options['fourth_value']))
                        gear_selected = 4
                        if arduino_conected == True:
                            arduino.write(b'4')  # Send gear indicator data to arduino
                    if shifter.get_button(options['fifth']) == True:
                        process.write(address, int(options['fifth_value']))
                        gear_selected = 5
                        if arduino_conected == True:
                            arduino.write(b'5')  # Send gear indicator data to arduino
                    if shifter.get_button(options['sixth']) == True:
                        process.write(address, int(options['sixth_value']))
                        gear_selected = 6
                        if arduino_conected == True:
                            arduino.write(b'6')  # Send gear indicator data to arduino  
                    if options['seven_gears'] == 'True':  # To avoid invalid button error
                        if shifter.get_button(options['seventh']) == True:
                            process.write(address, int(options['seventh_value']))
                            gear_selected = 7
                            if arduino_conected == True:
                                arduino.write(b'7')  # Send gear indicator data to arduino
                    if shifter.get_button(options['reverse']) == True:
                        if options['rev_button'] == 'False':
                            process.write(address, int(options['reverse_value']))
                            gear_selected = -1
                        else:
                            KeyPress_rev(options)
                            gear_selected = -1                 
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r")

                if event.type == pygame.JOYBUTTONUP:        
                    KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse
                    
                # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
                if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True' and validKey == True:
                    time.sleep(0.3)
                    if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                        process.write(address, int(options['neutral_value']))
                        gear_selected = 0
                        if arduino_conected == True:
                            arduino.write(b'0')
                        print(f"Gear in joystick: {gear_selected}   ",  end="\r")
                        
            # Select neutral if this key is pressed
            if keyboard.is_pressed(options['neut_key']):
                process.write(address, int(options['neutral_value']))
                gear_selected = 0
                if arduino_conected == True:
                    arduino.write(b'0')  
                print(f"Gear in joystick: {gear_selected}   ",  end="\r")

            if keyboard.is_pressed('End'):
                done = True

    #region MEM MODE CLUTCH     
    else: # Require clutch is true
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.
                
                if clutch.get_axis(int(options['clutch_axis'])) > clutch_value:  # First we check if clutch if pressed or not
                    clutch_pressed = True
                else:
                    clutch_pressed = False    

                if event.type == pygame.JOYBUTTONDOWN:
                    sound = True                    
                    # Flag to detect if a defined key for changing gear is pressed
                    validKey = False
                    # Check for multibutton presses
                    buttons = 0
                    for i in range (numButtons):
                        if shifter.get_button(i) == True:
                            buttons += 1                    
                    if buttons == 1:
                        validKey = True
                    # Check if in neutral
                    inNeutral = False
                    if shifter.get_button(options['first']) == False and shifter.get_button(options['second']) == False \
                    and shifter.get_button(options['third']) == False and shifter.get_button(options['fourth']) == False \
                    and shifter.get_button(options['fifth']) == False and shifter.get_button(options['sixth']) == False \
                    and shifter.get_button(options['seventh']) == False and shifter.get_button(options['reverse']) == False:
                        inNeutral = True
                    
                    if shifter.get_button(options['first']) == True and clutch_pressed == True:
                        process.write(address, int(options['first_value']))
                        gear_selected = 1
                        if arduino_conected == True:
                            arduino.write(b'1')  
                        sound = False
                        
                    if shifter.get_button(options['second']) == True and clutch_pressed == True:
                        process.write(address, int(options['second_value']))                            
                        gear_selected = 2
                        if arduino_conected == True:
                            arduino.write(b'2') 
                        sound = False
                        
                    if shifter.get_button(options['third']) == True and clutch_pressed == True:
                        process.write(address, int(options['third_value']))
                        gear_selected = 3
                        if arduino_conected == True:
                            arduino.write(b'3') 
                        sound = False
                        
                    if shifter.get_button(options['fourth']) == True and clutch_pressed == True:
                        process.write(address, int(options['fourth_value']))
                        gear_selected = 4
                        if arduino_conected == True:
                            arduino.write(b'4') 
                        sound = False
                        
                    if shifter.get_button(options['fifth']) == True and clutch_pressed == True:
                        process.write(address, int(options['fifth_value']))
                        gear_selected = 5
                        if arduino_conected == True:
                            arduino.write(b'5') 
                        sound = False
                    if shifter.get_button(options['sixth']) == True and clutch_pressed == True:
                        process.write(address, int(options['sixth_value']))
                        gear_selected = 6
                        if arduino_conected == True:
                            arduino.write(b'6') 
                        sound = False
                    if options['seven_gears'] == 'True':  # To avoid invalid button error
                        if shifter.get_button(options['seventh']) == True and clutch_pressed == True:
                            process.write(address, int(options['seventh_value']))
                            gear_selected = 7
                            if arduino_conected == True:
                                arduino.write(b'7') 
                            sound = False                                                                    
                    if shifter.get_button(options['reverse']) == True and clutch_pressed == True:
                        if options['rev_button'] == 'False':
                            process.write(address, int(options['reverse_value']))
                            gear_selected = -1
                            sound = False
                        else:
                            KeyPress_rev(options)
                            sound = False
                            gear_selected = -1 

                    if sound == True and validKey == True and inNeutral == False:  # Play sound if clutch was not pressed and the key pressed was one of the defined keys for changing gear
                        play_sound()                             
                                
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r")
                    
                if event.type == pygame.JOYBUTTONUP:        
                    KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse

                # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
                if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True' and validKey == True:
                    time.sleep(0.3)
                    if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                        process.write(address, int(options['neutral_value']))
                        gear_selected = 0
                        if arduino_conected == True:
                            arduino.write(b'0') 
                        print(f"Gear in joystick: {gear_selected}   ",  end="\r")
                        
            # Select neutral if this key is pressed
            if keyboard.is_pressed(options['neut_key']):
                process.write(address, int(options['neutral_value']))
                gear_selected = 0
                if arduino_conected == True:
                    arduino.write(b'0') 
                print(f"Gear in joystick: {gear_selected}   ",  end="\r")

            if keyboard.is_pressed('End'):
                done = True
                
        
    pygame.quit()
    if arduino_conected == True:
        arduino.write(b'9')  # Blank the display    
        arduino.close()  # Closing arduino
    

# Keys mode joystick loop
def joystick_loop_keys(options):

    pygame.init()
    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
    #detect how many buttons has the joystick. It will be used later to detect multibutton presses
    numButtons = shifter.get_numbuttons()
    
    # Setting serial port for arduino
    arduino_conected = False
    try:
        arduino = serial.Serial(options['comport'], 9600)
        time.sleep(2)
        arduino.write(b'8')  # Light the display so the user can confirm it is working
        arduino_conected = True
    except:
        print(f"No arduino conected in {options['comport']}")

    # Create clutch joystick object and initialize it if clutch = true
    if options['clutch'] == 'True':
        clutch = pygame.joystick.Joystick(int(options['clutch_id']))
        clutch.init()
    clutch_pressed = False
    clutch_value = -((-2 * int(options['bitepoint'])) / 100 + 1) 
   
    #region KEY MODE NO CLUTCH    
    gear_selected = 0 
    actual_gear = 0
    if options['clutch'] == 'False':  # Doesn´t require clutch to shift
        # Joystick read loop  
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.

                if event.type == pygame.JOYBUTTONDOWN:
                    # Flag to detect if a defined key for changing gear is pressed
                    validKey = False
                    # Check for multibutton presses
                    buttons = 0
                    for i in range (numButtons):
                        if shifter.get_button(i) == True:
                            buttons += 1                    
                    if buttons == 1:
                        validKey = True

                    if shifter.get_button(options['first']) == True:
                        gear_selected = 1
                        if arduino_conected == True:
                            arduino.write(b'1')
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                    if shifter.get_button(options['second']) == True:
                        gear_selected = 2
                        if arduino_conected == True:
                            arduino.write(b'2')
                        actual_gear = update_gear(gear_selected, actual_gear, options) 
                    if shifter.get_button(options['third']) == True:
                        gear_selected = 3
                        if arduino_conected == True:
                            arduino.write(b'3')
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                    if shifter.get_button(options['fourth']) == True:
                        gear_selected = 4
                        if arduino_conected == True:
                            arduino.write(b'4')
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                    if shifter.get_button(options['fifth']) == True:
                        gear_selected = 5
                        if arduino_conected == True:
                            arduino.write(b'5')
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                    if shifter.get_button(options['sixth']) == True:
                        gear_selected = 6
                        if arduino_conected == True:
                            arduino.write(b'6')
                        actual_gear = update_gear(gear_selected, actual_gear, options)  
                    if options['seven_gears'] == 'True':  # To avoid invalid button error
                        if shifter.get_button(options['seventh']) == True:
                            gear_selected = 7
                            if arduino_conected == True:
                                arduino.write(b'7')
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                    if shifter.get_button(options['reverse']) == True:
                        gear_selected = -1
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                    print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

                # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
                if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True' and validKey == True:
                    time.sleep(0.3)
                    if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                        gear_selected = 0
                        if arduino_conected == True:
                            arduino.write(b'0')
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                        print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

            # Select neutral if this key is pressed
            if keyboard.is_pressed(options['neut_key']):
                gear_selected = 0
                if arduino_conected == True:
                    arduino.write(b'0')
                actual_gear = update_gear(gear_selected, actual_gear, options)
                print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

            # Escape to exit from Anyshift    
            if keyboard.is_pressed('End'):
                    done = True

    #region KEY MODE CLUTCH
    else:  # Require clutch is true        
        # Joystick read loop  
        done = False
        while not done:
            for event in pygame.event.get():                

                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.
                
                if clutch.get_axis(int(options['clutch_axis'])) > clutch_value:  # First we check if clutch if pressed or not
                    clutch_pressed = True
                else:
                    clutch_pressed = False
                                
                if event.type == pygame.JOYBUTTONDOWN:
                    # Flag to detect if grind sound must be played
                    sound = True
                    # Flag to detect if a defined key for changing gear is pressed
                    validKey = False
                    # Check for multibutton presses
                    buttons = 0
                    for i in range (numButtons):
                        if shifter.get_button(i) == True:
                            buttons += 1                    
                    if buttons == 1:
                        validKey = True                    
                    # Check if in neutral
                    inNeutral = False
                    if shifter.get_button(options['first']) == False and shifter.get_button(options['second']) == False \
                    and shifter.get_button(options['third']) == False and shifter.get_button(options['fourth']) == False \
                    and shifter.get_button(options['fifth']) == False and shifter.get_button(options['sixth']) == False \
                    and shifter.get_button(options['seventh']) == False and shifter.get_button(options['reverse']) == False:
                        inNeutral = True

                    if shifter.get_button(options['first']) == True: 
                        if clutch_pressed == True:
                            gear_selected = 1
                            if arduino_conected == True:
                                arduino.write(b'1')
                            sound = False                                              
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                                                

                    if shifter.get_button(options['second']) == True:
                        if clutch_pressed == True:
                            gear_selected = 2
                            if arduino_conected == True:
                                arduino.write(b'2')
                            sound = False   
                            actual_gear = update_gear(gear_selected, actual_gear, options) 
                        
                    
                    if shifter.get_button(options['third']) == True:
                        if clutch_pressed == True:
                            gear_selected = 3
                            if arduino_conected == True:
                                arduino.write(b'3')
                            sound = False
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                        

                    if shifter.get_button(options['fourth']) == True:
                        if clutch_pressed == True:
                            gear_selected = 4
                            if arduino_conected == True:
                                arduino.write(b'4')
                            sound = False
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                        

                    if shifter.get_button(options['fifth']) == True:
                        if clutch_pressed == True:
                            gear_selected = 5
                            if arduino_conected == True:
                                arduino.write(b'5')
                            sound = False
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                        

                    if shifter.get_button(options['sixth']) == True:
                        if clutch_pressed == True:
                            gear_selected = 6
                            if arduino_conected == True:
                                arduino.write(b'6')
                            sound = False
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                        

                    if options['seven_gears'] == 'True':  # To avoid invalid button error
                        if shifter.get_button(options['seventh']) == True:
                            if clutch_pressed == True:
                                gear_selected = 7
                                if arduino_conected == True:
                                    arduino.write(b'7')
                                sound = False
                                actual_gear = update_gear(gear_selected, actual_gear, options)
                            

                    if shifter.get_button(options['reverse']) == True:
                        if clutch_pressed == True:
                            gear_selected = -1
                            sound = False
                            actual_gear = update_gear(gear_selected, actual_gear, options)
                                            
                    if sound == True and validKey == True and inNeutral == False:  # Play sound if clutch was not pressed and the key pressed was one of the defined keys for changing gear
                        play_sound()                        

                    print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

                # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
                if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True' and validKey == True:
                    time.sleep(0.3)
                    if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                        gear_selected = 0
                        if arduino_conected == True:
                            arduino.write(b'0')
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                        print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

            # Select neutral if this key is pressed
            if keyboard.is_pressed(options['neut_key']):
                gear_selected = 0
                if arduino_conected == True:
                    arduino.write(b'0')
                actual_gear = update_gear(gear_selected, actual_gear, options)
                print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

            # Escape to exit from Anyshift    
            if keyboard.is_pressed('End'):
                done = True    
    
    pygame.quit() 
    if arduino_conected == True:
        arduino.write(b'9')  # Blank the display    
        arduino.close()  # Closing arduino  
    
#region UPDATE GEARS
# Function to apply sequential logic to h-shifter inputs, and make the necessary key presses
def update_gear(gear_selected, actual_gear, options):

    global first_time

    if options['nascar_mode'] == 'True':
        if options['rev_button'] == 'True' and gear_selected == -1:
            while actual_gear != 1:
                KeyPress_down(options)
                actual_gear -= 1
            KeyPress_rev(options) 
            act_gear = 1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == 'True':  # Normal operation with gear 0 for neutral
                act_gear = actual_gear
                while act_gear != gear_selected:
                    if act_gear < gear_selected:
                        act_gear += 1
                        KeyPress_up(options)                
                    if act_gear > gear_selected:
                        act_gear -= 1
                        KeyPress_down(options)
            else:  # Game doesn´t detect neutral, so we skip gear 0    
                act_gear = actual_gear
                while act_gear != gear_selected:  
                    if act_gear < gear_selected:
                        if act_gear == 0:
                            act_gear += 1
                            if first_time == True:  # To prevent the bug where it doesn´t change the first time you use the shifter
                                KeyPress_up(options)
                                first_time = False   
                        else:
                            act_gear += 1
                            KeyPress_up(options)                
                    if act_gear > gear_selected:
                        if act_gear == 0:
                            act_gear -= 1                                           
                        else:
                            act_gear -= 1
                            KeyPress_down(options)
    else:
        # Press key selected for reverse
        if options['rev_button'] == 'True' and gear_selected == -1:
            KeyPress_rev(options) 
            act_gear = -1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == 'True':  # Normal operation with gear 0 for neutral
                act_gear = actual_gear
                while act_gear != gear_selected:
                    if act_gear < gear_selected:
                        act_gear += 1
                        KeyPress_up(options)                
                    if act_gear > gear_selected:
                        act_gear -= 1
                        KeyPress_down(options)
            else:  # Game doesn´t detect neutral, so we skip gear 0    
                act_gear = actual_gear
                while act_gear != gear_selected:  
                    if act_gear < gear_selected:
                        if act_gear == 0:
                            act_gear += 1
                            if first_time == True:  # To prevent the bug where it doesn´t change the first time you use the shifter
                                KeyPress_up(options)
                                first_time = False  
                        else:
                            act_gear += 1
                            KeyPress_up(options)                
                    if act_gear > gear_selected:
                        if act_gear == 0:
                            act_gear -= 1                                           
                        else:
                            act_gear -= 1
                            KeyPress_down(options)
                            
    return act_gear

#region KEYPRESSES
# Function to send key presses for upshift
def KeyPress_up(options):
    time.sleep(float(options['presskey_timer']))
    PressKey(int(options['up_key'], 16))  # press
    time.sleep(float(options['releasekey_timer']))
    ReleaseKey(int(options['up_key'], 16))  # release


# Function to send key presses for downshift
def KeyPress_down(options):
    time.sleep(float(options['presskey_timer']))
    PressKey(int(options['down_key'], 16))  # press
    time.sleep(float(options['releasekey_timer']))
    ReleaseKey(int(options['down_key'], 16))  # release


# Function to send key presses for reverse is button mode. Two separate functions, one for press...
def KeyPress_rev(options):
    time.sleep(float(options['presskey_timer']))
    PressKey(int(options['rev_key'], 16))  # press


# ... And another to release
def KeyRelease_rev(options):
    time.sleep(float(options['releasekey_timer']))
    ReleaseKey(int(options['rev_key'], 16))  # release