"""Main Anyshift executable"""
import pygame
import keyboard
import configparser
import time
import ctypes

# Bunch of stuff so that the script can send keystrokes to game #
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]



# Global variables
up_key = 's'
down_key = 'z'

def main():

    # Create a config objet and read config values
    config = configparser.ConfigParser()
    config.read('Anyshift.ini')
    neutral = config['SHIFTER']['neutral detection']
    joy_id = config['SHIFTER']['joystick id']
    first = int(config['SHIFTER']['first gear'])
    second = int(config['SHIFTER']['second gear'])
    third = int(config['SHIFTER']['third gear'])
    fourth = int(config['SHIFTER']['fourth gear'])
    fifth = int(config['SHIFTER']['fifth gear']) 
    sixth = int(config['SHIFTER']['sixth gear'])
    reverse = int(config['SHIFTER']['reverse button'])
    neut_key = config['KEYS']['neutral keyboard key']
    global up_key
    up_key = config['KEYS']['upshift']
    global down_key 
    down_key = config['KEYS']['downshift']
    
    # Initialize joystick module
    pygame.joystick.init()
    pygame.init()   
        
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(joy_id))
    shifter.init()

    # Cool window design ;)    
    print()
    print("    ___                _____ __    _ ______              ___  ____  ")
    print("   /   |  ____  __  __/ ___// /_  (_) __/ /_   _   __   <  / / __ \ ")
    print("  / /| | / __ \/ / / /\__ \/ __ \/ / /_/ __/  | | / /   / / / / / / ")
    print(" / ___ |/ / / / /_/ /___/ / / / / / __/ /_    | |/ /   / /_/ /_/ /  ")
    print("/_/  |_/_/ /_/\__, //____/_/ /_/_/_/  \__/    |___/   /_/(_)____/   ")
    print("             /____/                           ©2022 Menkaura Soft   ")    
    print()
    print("Buy me a coffe if you like this app: https://bmc.link/Menkaura")
    print()
    print("Active shifter: ",shifter.get_name())
        
    gear_selected = 0
    actual_gear = 0
        
    done = False
    while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                if shifter.get_button(first) == True:
                    gear_selected = 1
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(second) == True:
                    gear_selected = 2
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(third) == True:
                    gear_selected = 3
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(fourth) == True:
                    gear_selected = 4
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(fifth) == True:
                    gear_selected = 5
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(sixth) == True:
                    gear_selected = 6
                    actual_gear = update_gear(gear_selected, actual_gear)
                #if shifter.get_button(6) == True:
                #   gear_selected = 7
                #   actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(reverse) == True: 
                    gear_selected = -1
                    actual_gear = update_gear(gear_selected, actual_gear)        
                print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r") 

            # Change to neutral if the option is enabled
            if event.type == pygame.JOYBUTTONUP and neutral == 'True': 
                gear_selected = 0
                actual_gear = update_gear(gear_selected, actual_gear)
                print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

        # Reset to neutral if this key is pressed 
        if keyboard.is_pressed(neut_key):  
            gear_selected = 0
            actual_gear = update_gear(gear_selected, actual_gear)
            print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")
            
         
def update_gear(gear_selected, actual_gear):
    
    act_gear = actual_gear
    while act_gear != gear_selected:
        if act_gear < gear_selected:
            act_gear += 1
            #keyboard.press_and_release(up_key)   # Lo mismo tengo que alternar entre los dos metodos para dosbox y emuladores. o dar la opcion de elegir
            KeyPress_up()
            #time.sleep(0.25)
        if act_gear > gear_selected:
            act_gear -= 1
            KeyPress_down()
            #keyboard.press_and_release(down_key)
            #time.sleep(0.25)   # A lo mejor para dosbox hay que reactivarlo
    
    return act_gear


# Actuals Functions
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def KeyPress_up():
    time.sleep(.02)
    PressKey(0x1F) # press S
    time.sleep(.02)
    ReleaseKey(0x1F) #release s


def KeyPress_down():
    time.sleep(.02)
    PressKey(0x2C) # press Z
    time.sleep(.02)
    ReleaseKey(0x2C) #release Z


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()