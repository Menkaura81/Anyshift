##########################################################################################
# ShifterConfig module provides functions to select wich joystick button use as each gear
#
# THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
# APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
# HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
# OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
# IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
# ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
#
# 2023 Menkaura Soft
#########################################################################################

import pygame

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
def gear_selection(options, gear, active_joystick_id):

    if gear == 1:
        select_first(options, active_joystick_id)
    elif gear == 2:
        select_second(options, active_joystick_id)
    elif gear == 3:
        select_third(options, active_joystick_id)
    elif gear == 4:
        select_fourth(options, active_joystick_id)
    elif gear == 5:
        select_fifth(options, active_joystick_id)
    elif gear == 6:
        select_sixth(options, active_joystick_id)
    elif gear == 7:
        select_seventh(options, active_joystick_id)
    elif gear == 8:
        select_reverse(options, active_joystick_id)

 
def select_first(options, active_joystick_id):

    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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


def select_second(options, active_joystick_id):

    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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


def select_third(options, active_joystick_id):
    
    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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


def select_fourth(options, active_joystick_id):
    
    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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


def select_fifth(options, active_joystick_id):
    
    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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


def select_sixth(options, active_joystick_id):
    
    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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
    

def select_seventh(options, active_joystick_id):
    
    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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


def select_reverse(options, active_joystick_id):
    
    try:
        shifter = pygame.joystick.Joystick(active_joystick_id)
        shifter.init()
        num_buttons = shifter.get_numbuttons()
    except:
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