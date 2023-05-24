"""Legacy Anyshift console mode. No longer maintained"""

import os  # Hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # Joystick input
import keyboard  # Key presses
import configparser  # Read ini files
import time  # Delays
import ctypes  # Kernel level key presses
import pyMeow as pm  # Read and write memmory addresses
from ReadWriteMemory import ReadWriteMemory


def main():  

    # Define console windows size (rows, lines)
    #os.system("mode con cols=70 lines=13")
    
    # Import config from anyshift.ini
    options = read_options()       

    # Draw splash screen
    splash_screen()   

    # Lauch joystick loop in the selected mode    
    if options['mem_mode'] == 'False':
       joystick_loop_keys(options)
    else:
       joystick_loop_mem(options) 


def joystick_loop_keys(options):

    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
    print("Active shifter: ", shifter.get_name())
    
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


def joystick_loop_mem(options):

    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
    print("Active shifter: ", shifter.get_name())

    # Open DosBox process
    rwm = ReadWriteMemory()
    try:
        process = rwm.get_process_by_name('DOSBox.exe')
        process.open()        
        # DosBox base address. Got from the pointer we have
        x_pointer = process.get_pointer(int(options['db_base_addr'], 16)) 
        # Gear address is the base address plus the offset. This is the value we found in Cheat Engine
        gear_address = process.read(x_pointer) + int(options['offset'], 16)
    except:
        print("DOSBox not found. Launch it before Anyshift")
        time.sleep(3)

    # Open process
    process = pm.open_process("DOSBox.exe")
    address = gear_address
     
    if options['nascar_mode'] == 'False':
        # Loop
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.
                if event.type == pygame.JOYBUTTONDOWN:
                    if shifter.get_button(options['first']) == True:
                        pm.w_byte(process, address, 1)
                        gear_selected = 1
                    if shifter.get_button(options['second']) == True:
                        pm.w_byte(process, address, 2)
                        gear_selected = 2
                    if shifter.get_button(options['third']) == True:
                        pm.w_byte(process, address, 3)
                        gear_selected = 3
                    if shifter.get_button(options['fourth']) == True:
                        pm.w_byte(process, address, 4)
                        gear_selected = 4
                    if shifter.get_button(options['fifth']) == True:
                        pm.w_byte(process, address, 5)
                        gear_selected = 5
                    if shifter.get_button(options['sixth']) == True:
                        pm.w_byte(process, address, 6)
                        gear_selected = 6  
                    if options['seven_gears'] == 'True':  # To avoid invalid button error
                        if shifter.get_button(options['seventh']) == True:
                            pm.w_byte(process, address, 7)
                            gear_selected = 7
                    if shifter.get_button(options['reverse']) == True:
                        pm.w_byte(process, address, -1)
                        gear_selected = -1                
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r")

                # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
                if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True':
                    time.sleep(0.3)
                    if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                        pm.w_byte(process, address, 0)
                        gear_selected = 0
                        print(f"Gear in joystick: {gear_selected}   ",  end="\r")

            # Select neutral if this key is pressed
            if keyboard.is_pressed(options['neut_key']):
                gear_selected = 0
                print(f"Gear in joystick: {gear_selected}   ",  end="\r")
    else:  # Nascar mode is True
        # Loop
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.

                if event.type == pygame.JOYBUTTONDOWN:
                    if shifter.get_button(options['first']) == True:
                        pm.w_byte(process, address, 0)
                        gear_selected = 1
                    if shifter.get_button(options['second']) == True:
                        pm.w_byte(process, address, 1)
                        gear_selected = 2
                    if shifter.get_button(options['third']) == True:
                        pm.w_byte(process, address, 2)
                        gear_selected = 3
                    if shifter.get_button(options['fourth']) == True:
                        pm.w_byte(process, address, 3)
                        gear_selected = 4
                    if shifter.get_button(options['fifth']) == True:
                        pm.w_byte(process, address, 4)
                        gear_selected = 5
                    if shifter.get_button(options['sixth']) == True:
                        pm.w_byte(process, address, 5)
                        gear_selected = 6
                    if shifter.get_button(options['reverse']) == True:
                        KeyPress_rev(options)
                        gear_selected = -1                
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r") 

                if event.type == pygame.JOYBUTTONUP :
                    KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse


# Function to read config from anyshift.ini
def read_options():

    # Dictonary to store options of the .ini
    options = {}
    # Create a config objet and read config values
    config = configparser.ConfigParser()
    config.read('Anyshift.ini')
    
    # Save values into dictionay
    options['nascar_mode'] = config['OPTIONS']['nascar racing mode']
    options['seven_gears'] = config['OPTIONS']['seven gears']
    options['rev_button'] = config['OPTIONS']['reverse is button']
    options['neutral'] = config['OPTIONS']['neutral detection']
    options['mem_mode'] = config['OPTIONS']['memory write mode']
    options['db_base_addr'] = config['OPTIONS']['dosbox version base address']
    options['offset'] = config['OPTIONS']['memory value offset']
    options['joy_id'] = config['SHIFTER']['joystick id']
    options['first'] = int(config['SHIFTER']['first gear'])
    options['second'] = int(config['SHIFTER']['second gear'])
    options['third'] = int(config['SHIFTER']['third gear'])
    options['fourth'] = int(config['SHIFTER']['fourth gear'])
    options['fifth'] = int(config['SHIFTER']['fifth gear'])
    options['sixth'] = int(config['SHIFTER']['sixth gear'])
    options['seventh'] = int(config['SHIFTER']['seventh gear'])
    options['reverse'] = int(config['SHIFTER']['reverse'])
    options['neut_key'] = config['KEYS']['neutral key']
    options['up_key'] = config['KEYS']['upshift']
    options['down_key'] = config['KEYS']['downshift']
    options['rev_key'] = config['KEYS']['reverse']
    options['presskey_timer'] = float(config['OPTIONS']['presskey timer'])
    options['releasekey_timer'] = float(config['OPTIONS']['releasekey timer'])
    return options


# Draw splash screen function
def splash_screen():

    # Cool window design ;)
    print()
    print("    ___                _____ __    _ ______              ___  ____  ")
    print("   /   |  ____  __  __/ ___// /_  (_) __/ /_   _   __   <  / / __ \ ")
    print("  / /| | / __ \/ / / /\__ \/ __ \/ / /_/ __/  | | / /   / / / / / / ")
    print(" / ___ |/ / / / /_/ /___/ / / / / / __/ /_    | |/ /   / /_/ /_/ /  ")
    print("/_/  |_/_/ /_/\__, //____/_/ /_/_/_/  \__/    |___/   /_/(_)____/   ")
    print("             /____/                           ©2023 Menkaura Soft   ")
    print()
    print("Buy me a coffe if you like this app: https://bmc.link/Menkaura")
    print()
    
                
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
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Global variables
first_time = True

# Ctypes complicated stuff for low level key presses
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def KeyPress_up(options):
    time.sleep(options['presskey_timer'])
    PressKey(int(options['up_key'], 16))  # press
    time.sleep(options['releasekey_timer'])
    ReleaseKey(int(options['up_key'], 16))  # release


def KeyPress_down(options):
    time.sleep(options['presskey_timer'])
    PressKey(int(options['down_key'], 16))  # press
    time.sleep(options['releasekey_timer'])
    ReleaseKey(int(options['down_key'], 16))  # release


def KeyPress_rev(options):
    time.sleep(options['presskey_timer'])
    PressKey(int(options['rev_key'], 16))  # press


def KeyRelease_rev(options):
    time.sleep(options['releasekey_timer'])
    ReleaseKey(int(options['rev_key'], 16))  # release
    

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()