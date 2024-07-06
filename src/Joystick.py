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
from CtypeKeyPressSimulator import *
import keyboard  # Normal key presses
from ReadWriteMemory import ReadWriteMemory  # Memory writing
import serial # Arduino serial comunication
from PlaySound import play_sound
from PySide6.QtWidgets import QMessageBox
import Global


def joystick_loop(options):
    ##############################################################################################################
    # INITIALIZE PYGAME
    ##############################################################################################################
    pygame.init()
    # Initialize joystick module
    pygame.joystick.init()   
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()    
    #detect how many buttons has the joystick. It will be used later to detect multibutton presses
    numButtons = shifter.get_numbuttons()

    ##############################################################################################################
    # INITIALIZE ARDUINO IF ENABLED
    ##############################################################################################################
    arduino_conected = False
    try:
        arduino = serial.Serial(options['comport'], 9600)
        time.sleep(2)
        arduino.write(b'8')  # Light the display so the user can confirm it is working
        arduino_conected = True
    except:
        print(f"No arduino conected in {options['comport']}")

    ##############################################################################################################
    # Create clutch joystick object and initialize it if clutch = true
    ##############################################################################################################
    if options['clutch'] == True:
        clutch = pygame.joystick.Joystick(int(options['clutch_id']))
        clutch.init()
    clutch_pressed = False
    clutch_value = -((-2 * int(options['bitepoint'])) / 100 + 1)

    ##############################################################################################################
    # Initialize mem mode if enabled
    ##############################################################################################################
    if options['mem_mode'] == True:
        # Open DosBox process and check for process opened
        rwm = ReadWriteMemory()
        try:
            process = rwm.get_process_by_name(options['process'])
            process.open()        
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Process not found. Open it before Anyshift')
            msg.setWindowTitle("Error")
            msg.exec_()             
            return    
        
        # Base address. Got from the pointer we have
        x_pointer = process.get_pointer(int(options['db_base_addr'], 16)) 
            
        if options['process'] == 'pcsx2.exe':
            # In pcsx2 1.6 is allways de same address
            address = x_pointer
        else:
            # Gear address is the base address plus the offset. This is the value we found in Cheat Engine
            address = process.read(x_pointer) + int(options['offset'], 16) 
    
    
    #############################################################################################################
    # MAIN LOOP
    #############################################################################################################
    gear_selected = 0 
    actual_gear = 0
    gear_detected = False
    release_gear_time = time.time()     
    validKey = False 
    while Global.done == False:
                
        for event in pygame.event.get():
            # Event for end the loop
            if event.type == pygame.QUIT:
                done = True  
            # First we check if clutch if pressed or not
            if options['clutch'] == True:
                if clutch.get_axis(options['clutch_axis']) > clutch_value:  # First we check if clutch if pressed or not
                    clutch_pressed = True
                else:
                    clutch_pressed = False
            # Event ButtonDown
            if event.type == pygame.JOYBUTTONDOWN: 
                # Flag for gear engage detection
                gear_detected = False
                # Flag for grind sound
                sound = True
                # Flag to detect if a defined key for changing gear is pressed
                validKey = False 
                # Flag for neutral
                inNeutral = False        
                # Check for multibutton presses
                buttons = 0
                for i in range (numButtons):
                    if shifter.get_button(i) == True:
                        buttons += 1                    
                if buttons == 1:
                    validKey = True
                # Check if in neutral                
                if shifter.get_button(options['first']) == False and shifter.get_button(options['second']) == False \
                and shifter.get_button(options['third']) == False and shifter.get_button(options['fourth']) == False \
                and shifter.get_button(options['fifth']) == False and shifter.get_button(options['sixth']) == False \
                and shifter.get_button(options['seventh']) == False and shifter.get_button(options['reverse']) == False:
                    inNeutral = True
                ####################################### FIRST GEAR ####################################################
                if shifter.get_button(options['first']) == True :                    
                    if options['clutch'] == False: 
                        gear_detected = True                  
                        gear_selected = 1
                        if options['mem_mode'] == True:
                            process.write(address, int(options['first_value']))
                        else:
                            actual_gear = sendKeystrokes(gear_selected, actual_gear, options)                        
                        if arduino_conected == True:
                            arduino.write(b'1')  # Send gear indicator data to arduino                    
                    else:    
                        if clutch_pressed == True: 
                            gear_detected = True                       
                            gear_selected = 1
                            if options['mem_mode'] == True:
                                process.write(address, int(options['first_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
                            if arduino_conected == True:
                                arduino.write(b'1')  
                            sound = False   
                ####################################### SECOND GEAR ####################################################
                if shifter.get_button(options['second']) == True:
                    if options['clutch'] == False:
                        gear_detected = True
                        gear_selected = 2
                        if options['mem_mode'] == True:
                            process.write(address, int(options['second_value']))
                        else:
                            actual_gear = sendKeystrokes(gear_selected, actual_gear, options)                        
                        if arduino_conected == True:
                            arduino.write(b'2')  # Send gear indicator data to arduino                        
                    else:
                        if clutch_pressed == True:
                            gear_detected = True
                            gear_selected = 2
                            if options['mem_mode'] == True:
                                process.write(address, int(options['second_value']))                            
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options) 
                            if arduino_conected == True:
                                arduino.write(b'2') 
                            sound = False
                ####################################### THIRD GEAR ####################################################
                if shifter.get_button(options['third']) == True:
                    if options['clutch'] == False:
                        gear_detected = True
                        gear_selected = 3
                        if options['mem_mode'] == True:
                            process.write(address, int(options['third_value']))
                        else:
                            actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
                        if arduino_conected == True:
                            arduino.write(b'3')  # Send gear indicator data to arduino                        
                    else:
                        if clutch_pressed == True:
                            gear_detected = True
                            gear_selected = 3
                            if options['mem_mode'] == True:
                                process.write(address, int(options['third_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options)                         
                            if arduino_conected == True:
                                arduino.write(b'3') 
                            sound = False
                ####################################### FOURTH GEAR ####################################################
                if shifter.get_button(options['fourth']) == True:
                    if options['clutch'] == False:
                        gear_detected = True
                        gear_selected = 4
                        if options['mem_mode'] == True:
                            process.write(address, int(options['fourth_value']))
                        else:
                            actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
                        if arduino_conected == True:
                            arduino.write(b'4')  # Send gear indicator data to arduino                        
                    else:
                        if clutch_pressed == True:
                            gear_detected = True
                            gear_selected = 4
                            if options['mem_mode'] == True:
                                process.write(address, int(options['fourth_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options) 
                            if arduino_conected == True:
                                arduino.write(b'4') 
                            sound = False
                ####################################### FIFTH GEAR ####################################################
                if shifter.get_button(options['fifth']) == True:
                    if options['clutch'] == False:
                        gear_detected = True
                        gear_selected = 5
                        if options['mem_mode'] == True:
                            process.write(address, int(options['fifth_value']))
                        else:
                            actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
                        if arduino_conected == True:
                            arduino.write(b'5')  # Send gear indicator data to arduino                        
                    else:                        
                        if clutch_pressed == True:
                            gear_detected = True
                            gear_selected = 5
                            if options['mem_mode'] == True:
                                process.write(address, int(options['fifth_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options) 
                            if arduino_conected == True:
                                arduino.write(b'5') 
                            sound = False    
                ####################################### SIXTH GEAR ####################################################
                if shifter.get_button(options['sixth']) == True:
                    if options['clutch'] == 'False':
                        gear_detected = True
                        gear_selected = 6
                        if options['mem_mode'] == True:
                            process.write(address, int(options['sixth_value']))
                        else:
                            actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
                        if arduino_conected == True:
                            arduino.write(b'6')  # Send gear indicator data to arduino                  
                    else:
                        if clutch_pressed == True:
                            gear_detected = True
                            gear_selected = 6
                            if options['mem_mode'] == True:
                                process.write(address, int(options['sixth_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options) 
                            if arduino_conected == True:
                                arduino.write(b'6') 
                            sound = False
                ##################################### SEVENTH GEAR ####################################################
                if options['seven_gears'] == 'True':  # To avoid invalid button error
                    if shifter.get_button(options['seventh']) == True:
                        if options['clutch'] == False:
                            gear_detected = True
                            gear_selected = 7
                            if options['mem_mode'] == True:
                                process.write(address, int(options['seventh_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
                            if arduino_conected == True:
                                arduino.write(b'7')  # Send gear indicator data to arduino                            
                        else:
                            if clutch_pressed == True:
                                gear_detected = True
                                gear_selected = 7
                                if options['mem_mode'] == True:
                                    process.write(address, int(options['seventh_value']))
                                else:
                                    actual_gear = sendKeystrokes(gear_selected, actual_gear, options) 
                                if arduino_conected == True:
                                    arduino.write(b'7') 
                                sound = False  
                ######################################### REVERSE ####################################################
                if shifter.get_button(options['reverse']) == True:
                    if options['rev_button'] == False:
                        if options['clutch'] == False:
                            gear_detected = True
                            gear_selected = -1
                            if options['mem_mode'] == True:
                                process.write(address, int(options['reverse_value']))
                            else:
                                actual_gear = sendKeystrokes(gear_selected, actual_gear, options)                             
                        else:
                            if clutch_pressed == True:
                                gear_detected = True
                                gear_selected = -1
                                if options['mem_mode'] == True:
                                    process.write(address, int(options['reverse_value']))
                                else:
                                    actual_gear = sendKeystrokes(gear_selected, actual_gear, options)
                                sound = False    
                    else:
                        KeyPress_rev(options)
                        sound = False
                        gear_selected = -1
                        gear_detected = True

                # Play sound if clutch was not pressed and the key pressed was one of the defined keys for changing gear 
                if sound == True and validKey == True and inNeutral == False and options['clutch'] == True: 
                    play_sound()                             
                                
                print(f"Gear in joystick: {gear_selected}   ",  end="\r")
            
            # Release de reverse key just in case we came from reverse and start the timer for Detect Neutral 
            if event.type == pygame.JOYBUTTONUP:        
                KeyRelease_rev(options) 
                release_gear_time = time.time()
                gear_detected = False
            
        #################################################### NEUTRAL ##############################################################    
        # Change to neutral if the option is enabled and the timer is greater than neutral_wait_time                 
        if (time.time() - release_gear_time) >= options['neutral_wait_time'] and options['neutral'] == True and gear_detected == False and validKey == True:
            gear_selected = 0
            if options['mem_mode'] == True:
                process.write(address, int(options['neutral_value']))
            else:
                actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
            if arduino_conected == True:
                arduino.write(b'0')
            print(f"Gear in joystick: {gear_selected}   ",  end="\r")         
                        
        # Select neutral if this key is pressed
        if keyboard.is_pressed(options['neut_key']):
            gear_selected = 0
            if options['mem_mode'] == True:
                process.write(address, int(options['neutral_value']))
            else:
                actual_gear = sendKeystrokes(gear_selected, actual_gear, options)  
            if arduino_conected == True:
                arduino.write(b'0')  
            print(f"Gear in joystick: {gear_selected}   ",  end="\r")

        # Close Anyshift if end is pressed
        if keyboard.is_pressed('End'):
            Global.done = True        

    # Close pygame and arduino   
    pygame.quit()
    if arduino_conected == True:
        arduino.write(b'9')  # Blank the display    
        arduino.close()  # Closing arduino


# Get list of joystick ids and save them into joys list
def joystick_lister():

    pygame.joystick.init()
    num_joy = pygame.joystick.get_count()
    joys = []
    for i in range(num_joy):
        joy = pygame.joystick.Joystick(i)
        joy_id = joy.get_name()
        joys.append(joy_id)
        joy.quit()

    return joys, num_joy


# Function to choose wich gear config
def gear_selection(options, gear):

    if gear == 1:
        select_first(options)
    elif gear == 2:
        select_second(options)
    elif gear == 3:
        select_third(options)
    elif gear == 4:
        select_fourth(options)
    elif gear == 5:
        select_fifth(options)
    elif gear == 6:
        select_sixth(options)
    elif gear == 7:
        select_seventh(options)
    elif gear == 8:
        select_reverse(options)
    elif gear == 10:  # clutch axis
        get_axis(options)

 
def select_first(options):

    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['first'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()    
    return options


def select_second(options):

    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['second'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options


def select_third(options):
    
    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['third'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options


def select_fourth(options):
    
    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['fourth'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options


def select_fifth(options):
    
    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['fifth'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options


def select_sixth(options):
    
    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['sixth'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options
    

def select_seventh(options):
    
    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['seventh'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options


def select_reverse(options):
    
    pygame.init()
    try:
        shifter = pygame.joystick.Joystick(int(options['joy_id']))
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        options['reverse'] = i
                        done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
    return options


def get_axis(options):
    
    pygame.init()
    try:
        clutch = pygame.joystick.Joystick(int(options['clutch_id']))
        clutch.init()
    except:
        pygame.quit()
        return
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                options['clutch_axis'] = event.axis
                done = True
        if keyboard.is_pressed('End'):
            done = True
    pygame.quit()
        
    return options