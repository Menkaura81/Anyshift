#################################################################################################################################
# Anyshift GUI
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
##################################################################################################################################

import tkinter  # GUI
from tkinter import *  # Toplevel window
from tkinter import ttk  # GUI combobox
import pygame  # Joystick input
import configparser  # Write and read ini files
import csv  # Load and write csv files
from ReadWriteMemory import ReadWriteMemory  # Memory writing
from Gearbox import joystick_loop_keys, joystick_loop_mem
from ShifterConfig import gear_selection, joystick_lister

# Global variables
options = {}

# READ CONFIG FROM THE DICTIONARY CREATED FROM PRESETS.CSV
def load_preset():

    # Read presets.csv and store data in a list of dictionaries
    juegos = []    
    with open("presets.csv", "r") as file:
        reader = csv.DictReader(file)    
        for row in reader:  
            juegos.append(row)
                
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

    id = len(lista)
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


# GET ACTIVE JOYSTICK OF COMBOBOX AND CALLS GEARS SELECTION TO SELECT BUTTON FOR THE DESIRED GEAR
def gears(gear):

    global options
    pygame.init()
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
    gear_selection(options, gear, active_joystick_id)
    windows_updater()


# RUN ANYSHIFT JOYSTICK LOOP                       
def run_any():   

    # Read the actual configuration displayed
    read_options_from_windows()
    
    # Update button text
    run_button.config(text="Anyshift running. Press 'End' to stop")
    window.update()    

    if options['mem_mode'] == 'True':
        # Open DosBox process and check for process opened
        rwm = ReadWriteMemory()
        try:
            process = rwm.get_process_by_name(options['process'])
            process.open()        
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
        joystick_loop_mem(options)
        run_button.config(text="Run Anyshift")  # Return button to normal text
    else:
        joystick_loop_keys(options)
        run_button.config(text="Run Anyshift")  # Return button to normal text   
   


####################################  MAIN   ########################################

# Get list of joystick ids and save them into joys list
joys, num_joy = joystick_lister()

# Read config from ini file
read_ini()

# Create tkinter windows object
window = tkinter.Tk()
window.title("Anyshift")
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

first_gear_button = tkinter.Button(gears_selection_frame, text = "1", command = lambda: gears(1))
first_gear_button.grid(row = 2, column = 0)
first_gear_value = tkinter.Label(gears_selection_frame, text = options['first'])
first_gear_value.grid(row = 3, column = 0)

second_gear_button = tkinter.Button(gears_selection_frame, text = "2", command = lambda: gears(2))
second_gear_button.grid(row = 4, column = 0)
second_gear_value = tkinter.Label(gears_selection_frame, text = options['second'])
second_gear_value.grid(row = 5, column = 0)

third_gear_button = tkinter.Button(gears_selection_frame, text = "3", command = lambda: gears(3))
third_gear_button.grid(row = 2, column = 1)
third_gear_value = tkinter.Label(gears_selection_frame, text = options['third'])
third_gear_value.grid(row = 3, column = 1)

fourth_gear_button = tkinter.Button(gears_selection_frame, text = "4", command = lambda: gears(4))
fourth_gear_button.grid(row = 4, column = 1)
fourth_gear_value = tkinter.Label(gears_selection_frame, text = options['fourth'])
fourth_gear_value.grid(row = 5, column = 1)

fifth_gear_button = tkinter.Button(gears_selection_frame, text = "5", command = lambda: gears(5))
fifth_gear_button.grid(row = 2, column = 2)
fifth_gear_value = tkinter.Label(gears_selection_frame, text = options['fifth'])
fifth_gear_value.grid(row = 3, column = 2)

sixth_gear_button = tkinter.Button(gears_selection_frame, text = "6", command = lambda: gears(6))
sixth_gear_button.grid(row = 4, column = 2)
sixth_gear_value = tkinter.Label(gears_selection_frame, text = options['sixth'])
sixth_gear_value.grid(row = 5, column = 2)

seventh_gear_button = tkinter.Button(gears_selection_frame, text = "7", command = lambda: gears(7))
seventh_gear_button.grid(row = 2, column = 3)
seventh_gear_value = tkinter.Label(gears_selection_frame, text = options['seventh'])
seventh_gear_value.grid(row = 3, column = 3)

reverse_gear_label = tkinter.Button(gears_selection_frame, text = "R", command = lambda: gears(8))
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
lista = []
with open("presets.csv", "r") as file:
    reader = csv.DictReader(file)    
    counter = 0
    for row in reader:  # Load csv in a list of dictionaries
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