"""GUI for Anyshift config util. Still WIP"""

import tkinter  # GUI
from tkinter import *  # Toplevel window
from tkinter import ttk  # GUI combobox
import os  # Hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # Joystick input
import configparser  # Write and read ini files
import keyboard  # key presses
import csv  # Load and write csv files
import time  # Delays
import ctypes  # Kernel level key presses
from ReadWriteMemory import ReadWriteMemory  # Memory writing


# Global variables
first_time = True
options = {}

# READ CONFIG FROM THE DICTIONARY CREATED FROM PRESETS.CSV
def load_preset():
    
    # Read selected preset in combobox
    name = presets_combobox.get()
    index = 0
    for game in juegos:
        if game['name'] == name:
            index = int(game['id'])
    
    # Load variables from dictionary
    global options 
    options['up_key'] = juegos[index]['upshift']
    upshift_key_entry.delete(0, 2)  
    upshift_key_entry.insert(0, options['up_key'])
    options['up_key'] = hex_convert(options['up_key'])
    options['down_key'] = juegos[index]['downshift']
    downshift_key_entry.delete(0, 2)  
    downshift_key_entry.insert(0, options['down_key'])
    options['down_key'] = hex_convert(options['down_key'])
    options['rev_key'] = juegos[index]['reverse']
    reverse_key_entry.delete(0, 2)  
    reverse_key_entry.insert(0, options['rev_key'])
    options['rev_key']  = hex_convert(options['rev_key'])
    options['neut_key'] = juegos[index]['neutral key']
    neutral_key_entry.delete(0, 2) 
    neutral_key_entry.insert(0, options['neut_key'])
    options['seven_gears'] = juegos[index]['seven gears']
    options['neutral'] = juegos[index]['neutral detection']
    options['rev_button'] = juegos[index]['reverse is button']
    options['nascar'] = juegos[index]['nascar racing mode']
    options['presskey_timer'] = juegos[index]['presskey timer']
    press_key_entry.delete(0, 5)
    press_key_entry.insert(0, options['presskey_timer'])
    options['releasekey_timer'] = juegos[index]['releasekey timer']
    release_key_entry.delete(0, 5)
    release_key_entry.insert(0, options['releasekey_timer'])
    options['mem_mode'] = juegos[index]['memory write mode']
    options['process'] = juegos[index]['process name']
    process_key_entry.delete(0, 12)
    process_key_entry.insert(0, options['process'])
    options['db_base_addr'] = juegos[index]['base address']
    dosbase_key_entry.delete(0, 12)
    dosbase_key_entry.insert(0, options['db_base_addr'])
    options['offset'] = juegos[index]['offset'] 
    offset_key_entry.delete(0, 12)
    offset_key_entry.insert(0, options['offset'])

    # Update checks in window
    global neutral_var
    neutral_var = tkinter.StringVar(value = options['neutral'])
    neutral_check = tkinter.Checkbutton(options_selection_frame, text= "Detect Neutral",
                                variable=neutral_var, onvalue="True", offvalue="False")
    neutral_check.grid(row=0, column=0)

    global seven_var
    seven_var = tkinter.StringVar(value = options['seven_gears'])
    seven_check = tkinter.Checkbutton(options_selection_frame, text= "Use seventh gear",
                                  variable=seven_var, onvalue="True", offvalue="False")
    seven_check.grid(row=1, column=0)

    global rev_bool
    rev_bool = tkinter.StringVar(value = options['rev_button'])
    rev_check = tkinter.Checkbutton(options_selection_frame, text= "Reverse is a button",
                                  variable=rev_bool, onvalue="True", offvalue="False")
    rev_check.grid(row=0, column=1)

    global nascar
    nascar = tkinter.StringVar(value = options['nascar'])
    nascar_check = tkinter.Checkbutton(options_selection_frame, text= "Nascar mode",
                                  variable=nascar, onvalue="True", offvalue="False")
    nascar_check.grid(row=1, column=1)

    global mem_var
    mem_var = tkinter.StringVar(value = options['mem_mode'])
    mem_check = tkinter.Checkbutton(memory_selection_frame, text= "Memory mode",
                                  variable=mem_var, onvalue="True", offvalue="False")                                  
    mem_check.grid(row=0, column=0)
            

# SAVE ACTUAL CONFIG IN WINDOW TO PRESETS.CSV
def save_preset():
    
    preset = []
    keys = []

    id = len(juegos)
    #print(presets_combobox.currentText())    TODO NAME OF PRESET
    name = save_name_entry.get()
    preset.append(id)
    preset.append(name)

    upshift = upshift_key_entry.get()[:1].lower()
    if ord(upshift) >= 97 and ord(upshift) <= 122:
        preset.append(upshift)
        keys.append(upshift)
    else:
        error_window = Toplevel(window)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = tkinter.Frame(error_window)
        error_frame.pack()
        error_label = tkinter.Label(error_frame, text = "Upshift key error. Only one char (a to z)")
        error_label.grid(row = 0, column = 0)
        return
    
    downshift = downshift_key_entry.get().lower()
    print(downshift)
    if ord(downshift) >= 97 and ord(downshift) <= 122 and downshift not in keys:
        preset.append(downshift)
        keys.append(downshift)
    else:
        error_window = Toplevel(window)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = tkinter.Frame(error_window)
        error_frame.pack()
        error_label = tkinter.Label(error_frame, text = "Downshift key error. Repeated or not a to z char")
        error_label.grid(row = 0, column = 0)
        return
    
    reverse = reverse_key_entry.get().lower() 
    if ord(reverse) >= 97 and ord(reverse) <= 122 and reverse not in keys:
        preset.append(reverse)
        keys.append(reverse)
    else:
        error_window = Toplevel(window)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = tkinter.Frame(error_window)
        error_frame.pack()
        error_label = tkinter.Label(error_frame, text = "Reverse key error. Repeated or not a to z char")
        error_label.grid(row = 0, column = 0) 
        return
    
    neutral = neutral_key_entry.get().lower()
    if ord(neutral) >= 97 and ord(neutral) <= 122 and neutral not in keys:
        preset.append(neutral)
        keys.append(neutral)
    else:
        error_window = Toplevel(window)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = tkinter.Frame(error_window)
        error_frame.pack()
        error_label = tkinter.Label(error_frame, text = "Neutral key error. Only one char (a to z)")
        error_label.grid(row = 0, column = 0) 
        return
    
    preset.append(seven_var.get())
    preset.append(neutral_var.get())
    preset.append(rev_bool.get())
    preset.append(nascar.get())
    preset.append(mem_var.get())
    preset.append(process_key_entry.get())
    preset.append(dosbase_key_entry.get())
    preset.append(offset_key_entry.get())
    preset.append(press_key_entry.get())
    preset.append(release_key_entry.get())

    with open('presets.csv', 'a') as file: 
        # Pass this file object to csv.writer()
        # and get a writer object
        writer = csv.writer(file) 
        # Pass the list as an argument into
        # the writerow()
        writer.writerow(preset) 
        # Close the file object
        file.close()
    

# STORE CURRENT OPTIONS DISPLAYED IN THE WINDOWS TO OPTIONS[]
def read_options_from_windows():

    # Dictonary to store options of the .ini
    global options 
        
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i

    
    options['joy'] = active_joystick_id
    upshift = upshift_key_entry.get()
    options['up_key'] =  hex_convert(upshift.lower())
    neut_key = neutral_key_entry.get()
    options['neut_key'] = neut_key
    downshift = downshift_key_entry.get()
    options['down_key'] = hex_convert(downshift.lower())
    rev_key = reverse_key_entry.get()
    options['rev_key'] = rev_key = hex_convert(rev_key.lower())
    options['seven_gears'] = seven_var.get()
    options['neutral'] = neutral_var.get()
    options['rev_button'] = rev_bool.get()
    options['nascar_mode'] = nascar.get()
    options['mem_mode'] = mem_var.get()
    process = process_key_entry.get()
    options['process'] = process
    db_base_addr = dosbase_key_entry.get()
    options['db_base_addr'] = db_base_addr
    offset = offset_key_entry.get()
    options['offset'] = offset
    presskey_timer = press_key_entry.get()
    options['presskey_timer'] = presskey_timer
    releasekey_timer = release_key_entry.get()
    options['releasekey_timer'] = releasekey_timer


# READ OPTIONS FROM INI FILE
def read_ini():

    # Create a config objet and read config values
    config = configparser.ConfigParser()
    config.read('Anyshift.ini')
    
    # Save values into dictionay
    options['nascar_mode'] = config['OPTIONS']['nascar racing mode']
    options['seven_gears'] = config['OPTIONS']['seven gears']
    options['rev_button'] = config['OPTIONS']['reverse is button']
    options['neutral'] = config['OPTIONS']['neutral detection']
    options['mem_mode'] = config['OPTIONS']['memory write mode']
    options['process'] = config['OPTIONS']['process name']
    options['db_base_addr'] = config['OPTIONS']['base address']
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


# WRITE INI FILE WITH THE OPTIONS DISPLAYED IN WINDOWS
def write_ini():
    
    read_options_from_windows()

    # Those are readed again because in options[] they are stored as hex
    upshift = upshift_key_entry.get()
    downshift = downshift_key_entry.get()
    rev_key = reverse_key_entry.get()   

    # Create object config
    config = configparser.ConfigParser(allow_no_value=True)

    config['SHIFTER'] = {'; This is the id number of the joystick you want to use': None,
                         'Joystick id': options['joy_id'],
                         '; Joystick buttons for each gear': None,
                         'first gear': options['first'],
                         'second gear': options['second'],
                         'third gear': options['third'],
                         'fourth gear': options['fourth'],
                         'fifth gear': options['fifth'],
                         'sixth gear': options['sixth'],
                         'seventh gear': options['seventh'],
                         'reverse': options['reverse']
                        }

    config['KEYS'] = {'; Upshift, downshift and reverse key in hex code': None,
                      'upshift': upshift,
                      'downshift': downshift,
                      'reverse': rev_key,
                      '; Neutral key is not necessary to be in hex code': None,
                      'neutral key': options['neut_key']
                    }

    config['OPTIONS'] = {'; True if you have a shifter with seven gears. Seventh gear button must be configured or anyshift will crash ': None,
                         'seven gears': options['seven_gears'],
                         '; True if you want to change to neutral if no gear is selected in shifter. Most old games doesnt support this': None,
                         'neutral detection': options['neutral'],
                         '; True if the game uses a separated button for reverse. Gran Turismo or Nascar Racing for example': None,
                         'reverse is button': options['rev_button'],
                         '; Unique mode for old papyrus games where the game remember the gear you were in when you changed to': None,
                         '; reverse. This will change all way down to first gear and then press reverse to avoid desynchronization': None,
                         'nascar racing mode': options['nascar_mode'],
                         '; Instead of key presses it writes data to memory. I only included it because of Grand Prix 2': None,
                         '; Each game has different memory values. No offical support for this one': None,
                         'memory write mode': options['mem_mode'],
                         '; Name of the process of the game': None,
                         'Process name': options['process'],
                         '; Base address. Ex: 0.74 = 0x01D3A1A0 ': None,
                         'Base address': options['db_base_addr'],
                         '; Memory value offset from base addres ': None,
                         'Memory value offset': options['offset'],
                         '; Delays for key presses and releases. Tinker with this if game doesnt detect key presses': None,
                         'presskey timer': options['presskey_timer'],
                         'releasekey timer': options['releasekey_timer'],
                        }         

    # Write the file
    with open("Anyshift.ini", "w") as configfile:
        config.write(configfile)        


# CONVERT KEYS CHAR TO HEX CODES
def hex_convert(key):

    # Dictionary for converting input keys to hex values
    keys = {
        '1': '0x02',
        '2': '0x03',
        '3': '0x04',
        '4': '0x05',
        '5': '0x06',
        '6': '0x07',
        '7': '0x08',
        '8': '0x09',
        '9': '0x0A',
        '0': '0x0B',
        'q': '0x10',
        'w': '0x11',
        'e': '0x12',
        'r': '0x13',
        't': '0x14',
        'y': '0x15',
        'u': '0x16',
        'i': '0x17',
        'o': '0x18',
        'p': '0x19',
        'a': '0x1E',
        's': '0x1F',
        'd': '0x20',
        'f': '0x21',
        'g': '0x22',
        'h': '0x23',
        'j': '0x24',
        'k': '0x25',
        'l': '0x26',
        'z': '0x2C',
        'x': '0x2D',
        'c': '0x2E',
        'v': '0x2F',
        'b': '0x30',
        'n': '0x31',
        'm': '0x32'
    }

    # Convert input keys to hex values. Cheks if the key is in the dictionary and return its hex value
    if key in keys:
        result = keys[key]
    return result


# UPDATE WINDOWS WHEN A JOYSTICK BUTTON IS CONFIGURED
def windows_updater():
    
    global options
    # configure
    first_gear_value.config(text = options['first'])
    second_gear_value.config(text = options['second'])
    third_gear_value.config(text = options['third'])
    fourth_gear_value.config(text = options['fourth'])
    fifth_gear_value.config(text = options['fifth'])
    sixth_gear_value.config(text = options['sixth'])
    seventh_gear_value.config(text = options['seventh'])
    reverse_gear_value.config(text = options['reverse'])


# LOOPS FOR SELECTING BUTTONS IN SHIFTER   
def select_first():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_second():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_third():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_fourth():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_fifth():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_sixth():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_seventh():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater()
def select_reverse():

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
       
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
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
    windows_updater() 


# RUN ANYSHIFT JOYSTICK LOOP                       
def run_any():   

    read_options_from_windows()
    
    run_button.config(text="Anyshift running. Press 'End' to stop")
    window.update()
    

    if options['mem_mode'] == 'True':
        joystick_loop_mem()
    else:
        joystick_loop_keys()
   

# MEM MODE JOYSTICK LOOP
def joystick_loop_mem():

    pygame.init()
    # Initialize joystick module
    pygame.joystick.init()    
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(options['joy_id']))
    shifter.init()
        
    # Open DosBox process and check for process opened
    rwm = ReadWriteMemory()
    try:
        process = rwm.get_process_by_name(options['process'])
        process.open()        
        # DosBox base address. Got from the pointer we have
        x_pointer = process.get_pointer(int(options['db_base_addr'], 16)) 
        
        if options['process'] == 'pcsx2.exe':
            # In pcsx2 1.6 is allways de same address
            gear_address = x_pointer
        else:
            # In dosbox gear address is the base address plus the offset. This is the value we found in Cheat Engine
            gear_address = process.read(x_pointer) + int(options['offset'], 16)        
    except:
        error_window = Toplevel(window)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = tkinter.Frame(error_window)
        error_frame.pack()
        error_label = tkinter.Label(error_frame, text = "Process not found. Open it before Anyshift")
        error_label.grid(row = 0, column = 0)

        run_button.config(text="Run Anyshift")
        pygame.quit()
        return

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
                            KeyPress_rev()
                            gear_selected = -1                 
                    print(f"Gear in joystick: {gear_selected}   ",  end="\r")
                if event.type == pygame.JOYBUTTONUP:        
                    KeyRelease_rev()  # Release de reverse key just in case we came from reverse

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
                    KeyRelease_rev()  # Release de reverse key just in case we came from reverse
            if keyboard.is_pressed('End'):
                done = True
    pygame.quit()
    run_button.config(text="Run Anyshift")    


# KEYS MODE JOYSTICK LOOP
def joystick_loop_keys():

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
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(options['second']) == True:
                    gear_selected = 2
                    actual_gear = update_gear(gear_selected, actual_gear) 
                if shifter.get_button(options['third']) == True:
                    gear_selected = 3
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(options['fourth']) == True:
                    gear_selected = 4
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(options['fifth']) == True:
                    gear_selected = 5
                    actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(options['sixth']) == True:
                    gear_selected = 6
                    actual_gear = update_gear(gear_selected, actual_gear)  
                if options['seven_gears'] == 'True':  # To avoid invalid button error
                    if shifter.get_button(options['seventh']) == True:
                        gear_selected = 7
                        actual_gear = update_gear(gear_selected, actual_gear)
                if shifter.get_button(options['reverse']) == True:
                    gear_selected = -1
                    actual_gear = update_gear(gear_selected, actual_gear)
                print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

            # Change to neutral if the option is enabled. The program sleeps, and then check if the next event is a joybuttondown, if true skips neutral
            if event.type == pygame.JOYBUTTONUP and options['neutral'] == 'True':
                time.sleep(0.3)
                if not pygame.event.peek(pygame.JOYBUTTONDOWN):
                    gear_selected = 0
                    actual_gear = update_gear(gear_selected, actual_gear)
                    print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

        # Select neutral if this key is pressed
        if keyboard.is_pressed(options['neut_key']):
            gear_selected = 0
            actual_gear = update_gear(gear_selected, actual_gear)
            print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")

        # Escape to exit from Anyshift    
        if keyboard.is_pressed('End'):
                done = True
    pygame.quit()   
    run_button.config(text="Run Anyshift") 


# Function to apply sequential logic to h-shifter inputs, and make the necessary key presses
def update_gear(gear_selected, actual_gear):

    global first_time

    if options['nascar_mode'] == 'True':
        if options['rev_button'] == 'True' and gear_selected == -1:
            while actual_gear != 1:
                KeyPress_down()
                actual_gear -= 1
            KeyPress_rev() 
            act_gear = 1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev()  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == 'True':  # Normal operation with gear 0 for neutral
                act_gear = actual_gear
                while act_gear != gear_selected:
                    if act_gear < gear_selected:
                        act_gear += 1
                        KeyPress_up()                
                    if act_gear > gear_selected:
                        act_gear -= 1
                        KeyPress_down()
            else:  # Game doesn´t detect neutral, so we skip gear 0    
                act_gear = actual_gear
                while act_gear != gear_selected:  
                    if act_gear < gear_selected:
                        if act_gear == 0:
                            act_gear += 1
                            if first_time == True:  # To prevent the bug where it doesn´t change the first time you use the shifter
                                KeyPress_up()
                                first_time = False   
                        else:
                            act_gear += 1
                            KeyPress_up()                
                    if act_gear > gear_selected:
                        if act_gear == 0:
                            act_gear -= 1                                           
                        else:
                            act_gear -= 1
                            KeyPress_down()
    else:
        # Press key selected for reverse
        if options['rev_button'] == 'True' and gear_selected == -1:
            KeyPress_rev() 
            act_gear = -1
        else:  # Reverse is a gear, not a button   
            KeyRelease_rev()  # Release de reverse key just in case we came from reverse is a button mode
            if options['neutral'] == 'True':  # Normal operation with gear 0 for neutral
                act_gear = actual_gear
                while act_gear != gear_selected:
                    if act_gear < gear_selected:
                        act_gear += 1
                        KeyPress_up()                
                    if act_gear > gear_selected:
                        act_gear -= 1
                        KeyPress_down()
            else:  # Game doesn´t detect neutral, so we skip gear 0    
                act_gear = actual_gear
                while act_gear != gear_selected:  
                    if act_gear < gear_selected:
                        if act_gear == 0:
                            act_gear += 1
                            if first_time == True:  # To prevent the bug where it doesn´t change the first time you use the shifter
                                KeyPress_up()
                                first_time = False  
                        else:
                            act_gear += 1
                            KeyPress_up()                
                    if act_gear > gear_selected:
                        if act_gear == 0:
                            act_gear -= 1                                           
                        else:
                            act_gear -= 1
                            KeyPress_down()
                            
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


def KeyPress_up():
    time.sleep(float(options['presskey_timer']))
    PressKey(int(options['up_key'], 16))  # press
    time.sleep(float(options['releasekey_timer']))
    ReleaseKey(int(options['up_key'], 16))  # release


def KeyPress_down():
    time.sleep(float(options['presskey_timer']))
    PressKey(int(options['down_key'], 16))  # press
    time.sleep(float(options['releasekey_timer']))
    ReleaseKey(int(options['down_key'], 16))  # release


def KeyPress_rev():
    time.sleep(float(options['presskey_timer']))
    PressKey(int(options['rev_key'], 16))  # press


def KeyRelease_rev():
    time.sleep(float(options['releasekey_timer']))
    ReleaseKey(int(options['rev_key'], 16))  # release


#####################WINDOWS CREATION AND LOOP###################

# Get list of joystick ids and save them into joys list
pygame.joystick.init()
num_joy = pygame.joystick.get_count()
joys = []
for i in range(num_joy):
    joy = pygame.joystick.Joystick(i)
    joy_id = joy.get_name()
    joys.append(joy_id)
    joy.quit()

# Read config from ini file
read_ini()

# Create tkinter windows object
window = tkinter.Tk()
window.title("Anyshift Config")
window.iconbitmap("any_ico.ico")

# Create frame
frame = tkinter.Frame(window)
frame.pack()

# Joystick selection
joystick_frame = tkinter.LabelFrame(frame, text = "Joystick id")
joystick_frame.grid(row = 0, column = 0, padx= 20, pady = 5)

# No joystick connected check
try:
    joystick_id_combobox = ttk.Combobox(joystick_frame, values = joys)
    joystick_id_combobox.current(options['joy_id'])
    joystick_id_combobox.grid(row = 0, column = 0)
except:
    error_label = tkinter.Label(joystick_frame, text = "No devices connected.")
    error_label.grid(row = 0, column = 0)
    error_label = tkinter.Label(joystick_frame, text = "Connect at least one device")
    error_label.grid(row = 1, column = 0)
    error_label = tkinter.Label(joystick_frame, text = "and launch Anyshift again")
    error_label.grid(row = 2, column = 0)
        

# Joystick buttons selection
gears_selection_frame = tkinter.LabelFrame(frame, text = "Joystick Buttons")
gears_selection_frame.grid(row = 1, column = 0)

first_gear_button = tkinter.Button(gears_selection_frame, text = "1", command = select_first)
first_gear_button.grid(row = 2, column = 0)
first_gear_value = tkinter.Label(gears_selection_frame, text = options['first'])
first_gear_value.grid(row = 3, column = 0)

second_gear_button = tkinter.Button(gears_selection_frame, text = "2", command = select_second)
second_gear_button.grid(row = 4, column = 0)
second_gear_value = tkinter.Label(gears_selection_frame, text = options['second'])
second_gear_value.grid(row = 5, column = 0)

third_gear_button = tkinter.Button(gears_selection_frame, text = "3", command = select_third)
third_gear_button.grid(row = 2, column = 1)
third_gear_value = tkinter.Label(gears_selection_frame, text = options['third'])
third_gear_value.grid(row = 3, column = 1)

fourth_gear_button = tkinter.Button(gears_selection_frame, text = "4", command = select_fourth)
fourth_gear_button.grid(row = 4, column = 1)
fourth_gear_value = tkinter.Label(gears_selection_frame, text = options['fourth'])
fourth_gear_value.grid(row = 5, column = 1)

fifth_gear_button = tkinter.Button(gears_selection_frame, text = "5", command = select_fifth)
fifth_gear_button.grid(row = 2, column = 2)
fifth_gear_value = tkinter.Label(gears_selection_frame, text = options['fifth'])
fifth_gear_value.grid(row = 3, column = 2)

sixth_gear_button = tkinter.Button(gears_selection_frame, text = "6", command = select_sixth)
sixth_gear_button.grid(row = 4, column = 2)
sixth_gear_value = tkinter.Label(gears_selection_frame, text = options['sixth'])
sixth_gear_value.grid(row = 5, column = 2)

seventh_gear_button = tkinter.Button(gears_selection_frame, text = "7", command = select_seventh)
seventh_gear_button.grid(row = 2, column = 3)
seventh_gear_value = tkinter.Label(gears_selection_frame, text = options['seventh'])
seventh_gear_value.grid(row = 3, column = 3)

reverse_gear_label = tkinter.Button(gears_selection_frame, text = "R", command = select_reverse)
reverse_gear_label.grid(row = 4, column = 3)
reverse_gear_value = tkinter.Label(gears_selection_frame, text = options['reverse'])
reverse_gear_value.grid(row = 5, column = 3)

# Keys selection

keys_selection_frame = tkinter.LabelFrame(frame, text = "Key Selection")
keys_selection_frame.grid(row = 2, column = 0)

upshift_key_label = tkinter.Label(keys_selection_frame, text = "Upshift")
upshift_key_label.grid(row = 0, column = 0)
upshift_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
upshift_key_entry.insert(0, options['up_key'])
upshift_key_entry.grid(row = 0, column = 1)

downshift_key_label = tkinter.Label(keys_selection_frame, text = "Downshift")
downshift_key_label.grid(row = 1, column = 0)
downshift_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
downshift_key_entry.insert(0, options['down_key'])
downshift_key_entry.grid(row = 1, column = 1)

neutral_key_label = tkinter.Label(keys_selection_frame, text = "Neutral")
neutral_key_label.grid(row = 0, column = 2)
neutral_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
neutral_key_entry.insert(0, options['neut_key'])
neutral_key_entry.grid(row = 0, column = 3)

reverse_key_label = tkinter.Label(keys_selection_frame, text = "Reverse")
reverse_key_label.grid(row = 1, column = 2)
reverse_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
reverse_key_entry.insert(0, options['rev_key'])
reverse_key_entry.grid(row = 1, column = 3)

for widget in keys_selection_frame.winfo_children():
    widget.grid_configure(pady = 5)

# Options

options_selection_frame = tkinter.LabelFrame(frame, text = "Options")
options_selection_frame.grid(row = 3, column = 0, padx = 20, pady = 5)

neutral_var = tkinter.StringVar(value = options['neutral'])
neutral_check = tkinter.Checkbutton(options_selection_frame, text= "Detect Neutral",
                                  variable=neutral_var, onvalue="True", offvalue="False")
neutral_check.grid(row=0, column=0)

seven_var = tkinter.StringVar(value = options['seven_gears'])
seven_check = tkinter.Checkbutton(options_selection_frame, text= "Use seventh gear",
                                  variable=seven_var, onvalue="True", offvalue="False")
seven_check.grid(row=1, column=0)

rev_bool = tkinter.StringVar(value = options['rev_button'])
rev_check = tkinter.Checkbutton(options_selection_frame, text= "Reverse is a button",
                                  variable=rev_bool, onvalue="True", offvalue="False")
rev_check.grid(row=0, column=1)

nascar = tkinter.StringVar(value = options['nascar_mode'])
nascar_check = tkinter.Checkbutton(options_selection_frame, text= "Nascar mode",
                                  variable=nascar, onvalue="True", offvalue="False")
nascar_check.grid(row=1, column=1)

# Mem mode

memory_selection_frame = tkinter.LabelFrame(frame)
memory_selection_frame.grid(row = 4, column = 0, padx = 20, pady = 5)

mem_var = tkinter.StringVar(value = options['mem_mode'])
mem_check = tkinter.Checkbutton(memory_selection_frame, text= "Memory mode",
                                  variable=mem_var, onvalue="True", offvalue="False")                                  
mem_check.grid(row=0, column=0)

process_label = tkinter.Label(memory_selection_frame, text = "Process name")
process_label.grid(row = 1, column = 0)
process_key_entry = tkinter.Entry(memory_selection_frame, width= 12)
process_key_entry.insert(0, options['process'])
process_key_entry.grid(row = 1, column = 1)

dosbase_key_label = tkinter.Label(memory_selection_frame, text = "Base address")
dosbase_key_label.grid(row = 2, column = 0)
dosbase_key_entry = tkinter.Entry(memory_selection_frame, width= 12)
dosbase_key_entry.insert(0, options['db_base_addr'])
dosbase_key_entry.grid(row = 2, column = 1)

offset_key_label = tkinter.Label(memory_selection_frame, text = "Memory address offset")
offset_key_label.grid(row = 3, column = 0)
offset_key_entry = tkinter.Entry(memory_selection_frame, width= 12)
offset_key_entry.insert(0, options['offset'])
offset_key_entry.grid(row = 3, column = 1)

# Timers

press_key_label = tkinter.Label(memory_selection_frame, text = "Press key delay")
press_key_label.grid(row = 2, column = 2)
press_key_entry = tkinter.Entry(memory_selection_frame, width= 4)
press_key_entry.insert(0, options['presskey_timer'])
press_key_entry.grid(row = 2, column = 3)

release_key_label = tkinter.Label(memory_selection_frame, text = "Release key delay")
release_key_label.grid(row = 3, column = 2)
release_key_entry = tkinter.Entry(memory_selection_frame, width= 4)
release_key_entry.insert(0, options['releasekey_timer'])
release_key_entry.grid(row = 3, column = 3)

# Profiles
profiles_selection_frame = tkinter.LabelFrame(frame, text = "Profiles")
profiles_selection_frame.grid(row = 6, column = 0, padx = 20, pady = 5)

# Presets buttons
juegos = []
lista = []
with open("presets.csv", "r") as file:
    reader = csv.DictReader(file)    
    counter = 0
    for row in reader:  # Load csv in a list of dictionaries
        juegos.append(row)
        lista.append(row['name'])

presets_combobox = ttk.Combobox(profiles_selection_frame, values = lista, width = 30)
presets_combobox.grid(row = 0, column = 1) 


button = tkinter.Button(profiles_selection_frame, text="Load profile", command= load_preset)
button.grid(row=0, column=0, sticky="news", padx=20, pady = 5)

button = tkinter.Button(profiles_selection_frame, text="Save profile", command= save_preset)  
button.grid(row=1, column=0, sticky="news", padx=20, pady = 5)

save_name_entry = tkinter.Entry(profiles_selection_frame, width= 33)
save_name_entry.grid(row = 1, column = 1)


# Save data button
button = tkinter.Button(frame, text="Remember current options", command= write_ini)
button.grid(row=8, column=0, sticky="news", padx=20, pady = 5)

# Run Button
run_button = tkinter.Button(frame, text="Run Anyshift", command= run_any)
run_button.grid(row=9, column=0, sticky="news", padx=20, pady = 5)


window.mainloop()