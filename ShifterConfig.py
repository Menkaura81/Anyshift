#####################################################################################################
# ShifterConfig module provides functions to select wich joystick button use as each gear
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
#####################################################################################################

import pygame
import keyboard  # Normal key presses

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