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

# Flag for avoiding first shifting bug when running nascar mode 
first_time = True

# Mem mode joystick loop
def joystick_loop_mem(options):

    pygame.init()
    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
        
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
        # In dosbox gear address is the base address plus the offset. This is the value we found in Cheat Engine
        address = process.read(x_pointer) + int(options['offset'], 16)        
         
    if options['nascar_mode'] == 'False':
        # Loop
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.
                if event.type == pygame.JOYBUTTONDOWN:
                    if shifter.get_button(options['first']) == True:
                        process.write(address, 1)
                        gear_selected = 1
                    if shifter.get_button(options['second']) == True:
                        process.write(address, 2)
                        gear_selected = 2
                    if shifter.get_button(options['third']) == True:
                        process.write(address, 3)
                        gear_selected = 3
                    if shifter.get_button(options['fourth']) == True:
                        process.write(address, 4)
                        gear_selected = 4
                    if shifter.get_button(options['fifth']) == True:
                        process.write(address, 5)
                        gear_selected = 5
                    if shifter.get_button(options['sixth']) == True:
                        process.write(address, 6)
                        gear_selected = 6  
                    if options['seven_gears'] == 'True':  # To avoid invalid button error
                        if shifter.get_button(options['seventh']) == True:
                            process.write(address, 7)
                            gear_selected = 7
                    if shifter.get_button(options['reverse']) == True:
                        if options['rev_button'] == 'False':
                            process.write(address, -1)
                            gear_selected = -1
                        else:
                            KeyPress_rev(options)
                            gear_selected = -1                 
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r")
                if event.type == pygame.JOYBUTTONUP:        
                    KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse

                # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
                if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True':
                    time.sleep(0.3)
                    if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                        process.write(address, 0)
                        gear_selected = 0
                        print(f"Gear in joystick: {gear_selected}   ",  end="\r")
                        
            # Select neutral if this key is pressed
            if keyboard.is_pressed(options['neut_key']):
                gear_selected = 0
                print(f"Gear in joystick: {gear_selected}   ",  end="\r")

            if keyboard.is_pressed('End'):
                done = True
    else:  # Nascar mode is True    Memory Locations doesn´t seem to be correct
        # Loop
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.

                if event.type == pygame.JOYBUTTONDOWN:
                    if shifter.get_button(options['first']) == True:
                        process.write(address, 0)
                        gear_selected = 1
                    if shifter.get_button(options['second']) == True:
                        process.write(address, 1)
                        gear_selected = 2
                    if shifter.get_button(options['third']) == True:
                        process.write(address, 2)
                        gear_selected = 3
                    if shifter.get_button(options['fourth']) == True:
                        process.write(address, 3)
                        gear_selected = 4
                    if shifter.get_button(options['fifth']) == True:
                        process.write(address, 4)
                        gear_selected = 5
                    if shifter.get_button(options['sixth']) == True:
                        process.write(address, 5)
                        gear_selected = 6
                    if shifter.get_button(options['reverse']) == True:
                        KeyPress_rev()
                        gear_selected = -1                
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r") 

                if event.type == pygame.JOYBUTTONUP :
                    KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse
            if keyboard.is_pressed('End'):
                done = True
    pygame.quit()
    

# Keys mode joystick loop
def joystick_loop_keys(options):

    pygame.init()
    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
        
    gear_selected = 0 
    actual_gear = 0
    # Joystick read loop  
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                if shifter.get_button(options['first']) == True:
                    gear_selected = 1
                    actual_gear = update_gear(gear_selected, actual_gear, options)
                if shifter.get_button(options['second']) == True:
                    gear_selected = 2
                    actual_gear = update_gear(gear_selected, actual_gear, options) 
                if shifter.get_button(options['third']) == True:
                    gear_selected = 3
                    actual_gear = update_gear(gear_selected, actual_gear, options)
                if shifter.get_button(options['fourth']) == True:
                    gear_selected = 4
                    actual_gear = update_gear(gear_selected, actual_gear, options)
                if shifter.get_button(options['fifth']) == True:
                    gear_selected = 5
                    actual_gear = update_gear(gear_selected, actual_gear, options)
                if shifter.get_button(options['sixth']) == True:
                    gear_selected = 6
                    actual_gear = update_gear(gear_selected, actual_gear, options)  
                if options['seven_gears'] == 'True':  # To avoid invalid button error
                    if shifter.get_button(options['seventh']) == True:
                        gear_selected = 7
                        actual_gear = update_gear(gear_selected, actual_gear, options)
                if shifter.get_button(options['reverse']) == True:
                    gear_selected = -1
                    actual_gear = update_gear(gear_selected, actual_gear, options)
                print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

            # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
            if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True':
                time.sleep(0.3)
                if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                    gear_selected = 0
                    actual_gear = update_gear(gear_selected, actual_gear, options)
                    print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

        # Select neutral if this key is pressed
        if keyboard.is_pressed(options['neut_key']):
            gear_selected = 0
            actual_gear = update_gear(gear_selected, actual_gear, options)
            print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

        # Escape to exit from Anyshift    
        if keyboard.is_pressed('End'):
                done = True
    pygame.quit()   
    

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