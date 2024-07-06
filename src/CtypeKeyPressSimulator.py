########################################################################################################
# CtypeKeyPressSimulator module provides low level simulated key presses functions
#
# Original code by DanielShaww found in this subreddit:
# https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/
#
# DirectInput Key Code Table:
# http://www.flint.jp/misc/?q=dik&lang=en
#
# Example of function call (press Q):
#
#    def KeyPress():
#       time.sleep(3)
#       PressKey(0x10)  # press
#       time.sleep(0.05)
#       ReleaseKey(0x10)  # release
#
#########################################################################################################

import ctypes  # Kernel level key presses
import time  # Delays

#region CTYPE

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


# Ctypes complicated stuff for low level key presses
def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


# Ctypes complicated stuff for low level key releases
def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

#region KEYPRESSES
# (code by Menkaura)
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


# Function to apply sequential logic to h-shifter inputs, and make the necessary key presses
# Flag for avoiding first shifting bug when running nascar mode 
first_time = True
def sendKeystrokes(gear_selected, actual_gear, options):
    global first_time
    if options['nascar_mode'] == True:
        if options['rev_button'] == True and gear_selected == -1:
            while actual_gear != 1:
                KeyPress_down(options)
                actual_gear -= 1
            KeyPress_rev(options) 
            act_gear = 1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == True:  # Normal operation with gear 0 for neutral
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
        if options['rev_button'] == True and gear_selected == -1:
            KeyPress_rev(options) 
            act_gear = -1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev(options)  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == True:  # Normal operation with gear 0 for neutral
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