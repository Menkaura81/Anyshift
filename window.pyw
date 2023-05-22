"""GUI for Anyshift config util. Still WIP"""

import tkinter
from tkinter import *
from tkinter import ttk
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import pygame
import configparser
import keyboard
import sys
import csv

first = '-'
second = '-'
third = '-'
fourth = '-'
fifth = '-'
sixth = '-'
seventh = '-'
reverse = '-'

def load_data(juegos, index):

    # Load variables from dictionary
    global upshift 
    upshift = hex_convert(juegos[index]['upshift'])  # Read and converted to hex
    global downshift
    downshift = hex_convert(juegos[index]['downshift'])
    global rev_key
    rev_key = hex_convert(juegos[index]['reverse'])
    global neut_key
    neut_key = juegos[index]['neutral key']
    global seven_gears
    seven_gears = juegos[index]['seven gears']
    global neutral
    neutral = juegos[index]['neutral detection']
    global rev_bool
    rev_bool = juegos[index]['reverse is button']
    global nascar
    nascar = juegos[index]['nascar racing mode']
    global presskey_timer
    presskey_timer = juegos[index]['presskey timer']
    global releasekey_timer
    releasekey_timer = juegos[index]['releasekey timer']
    global mem_mode
    mem_mode = juegos[index]['memory write mode']
    global db_base_addr
    db_base_addr = juegos[index]['dosbox base address']
    global offset 
    offset = juegos[index]['offset']                  

    global joy     ####FIX THISSSS TO READ THE VALUES FROM INI
    global first
    global second
    global third
    global fourth
    global fifth
    global sixth
    global seventh
    global reverse

         
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

def save_data():
    
    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i

    global joy
    joy = active_joystick_id
    global first
    global second
    global third
    global fourth
    global fifth
    global sixth
    global seventh
    global reverse
    upshift = upshift_key_entry.get()
    upshift = hex_convert(upshift.lower())
    neut_key = neutral_key_entry.get()
    downshift = downshift_key_entry.get()
    downshift = hex_convert(downshift.lower())
    rev_key = reverse_key_entry.get()
    rev_key = hex_convert(rev_key.lower())
    seven_gears = seven_var.get()
    neutral = neutral_var.get()
    db_base_addr = dosbase_key_entry.get()
    offset = offset_key_entry.get()
    presskey_timer = press_key_entry.get()
    releasekey_timer = release_key_entry.get()


    # Create object config
    config = configparser.ConfigParser(allow_no_value=True)

    config['SHIFTER'] = {'; This is the id number of the joystick you want to use': None,
                         'Joystick id': joy,
                         '; Joystick buttons for each gear': None,
                         'first gear': first,
                         'second gear': second,
                         'third gear': third,
                         'fourth gear': fourth,
                         'fifth gear': fifth,
                         'sixth gear': sixth,
                         'seventh gear': seventh,
                         'reverse': reverse
                        }

    config['KEYS'] = {'; Upshift, downshift and reverse key in hex code': None,
                      'upshift': upshift,
                      'downshift': downshift,
                      'reverse': rev_key,
                      '; Neutral key is not necessary to be in hex code': None,
                      'neutral key': neut_key
                    }

    config['OPTIONS'] = {'; True if you have a shifter with seven gears. Seventh gear button must be configured or anyshift will crash ': None,
                         'seven gears': seven_gears,
                         '; True if you want to change to neutral if no gear is selected in shifter. Most old games doesnt support this': None,
                         'neutral detection': neutral,
                         '; True if the game uses a separated button for reverse. Gran Turismo or Nascar Racing for example': None,
                         'reverse is button': rev_bool,
                         '; Unique mode for old papyrus games where the game remember the gear you were in when you changed to': None,
                         '; reverse. This will change all way down to first gear and then press reverse to avoid desynchronization': None,
                         'nascar racing mode': nascar,
                         '; Instead of key presses it writes data to memory. I only included it because of Grand Prix 2': None,
                         '; Each game has different memory values. No offical support for this one': None,
                         'memory write mode': mem_mode,
                         '; DosBox version base address. Ex: 0.74 = 0x01D3A1A0 ': None,
                         'DosBox Version base address': db_base_addr,
                         '; Memory value offset from base addres ': None,
                         'Memory value offset': offset,
                         '; Delays for key presses and releases. Tinker with this if game doesnt detect key presses': None,
                         'presskey timer': presskey_timer,
                         'releasekey timer': releasekey_timer,
                        }         

    # Write the file
    with open("Anyshift.ini", "w") as configfile:
        config.write(configfile)

def windows_updater():
    
    global first
     
    # configure
    first_gear_value.config(text = first)
    second_gear_value.config(text = second)
    third_gear_value.config(text = third)
    fourth_gear_value.config(text = fourth)
    fifth_gear_value.config(text = fifth)
    sixth_gear_value.config(text = sixth)
    seventh_gear_value.config(text = seventh)
    reverse_gear_value.config(text = reverse)

    
def select_first():

    global first
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
                        first = i
                        done = True
    pygame.quit()
    windows_updater()


def select_second():

    global second
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
                        second = i
                        done = True
    pygame.quit()
    windows_updater()


def select_third():

    global third
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
                        third = i
                        done = True
    pygame.quit()
    windows_updater()


def select_fourth():

    global fourth
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
                        fourth = i
                        done = True
    pygame.quit()
    windows_updater()


def select_fifth():

    global fifth
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
                        fifth = i
                        done = True
    pygame.quit()
    windows_updater()


def select_sixth():

    global sixth
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
                        sixth = i
                        done = True
    pygame.quit()
    windows_updater()


def select_seventh():

    global seventh
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
                        seventh = i
                        done = True
    pygame.quit()
    windows_updater()


def select_reverse():

    global reverse
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
                        reverse = i
                        done = True
    pygame.quit()
    windows_updater() 

                        
def run_any():
    
    mypath = os.path.abspath(os.path.dirname(__file__))
    os.system( f'"{mypath}/anyshift.exe"' )      
         

# Get list of joystick ids and save them into joys list
pygame.joystick.init()
num_joy = pygame.joystick.get_count()
joys = []
for i in range(num_joy):
    joy = pygame.joystick.Joystick(i)
    joy_id = joy.get_name()
    joys.append(joy_id)
    joy.quit()


window = tkinter.Tk()
window.title("Anyshift Config")

frame = tkinter.Frame(window)
frame.pack()

# Joystick selection
joystick_frame = tkinter.LabelFrame(frame, text = "Joystick id")
joystick_frame.grid(row = 0, column = 0, padx= 20, pady = 5)

joystick_id_combobox = ttk.Combobox(joystick_frame, values = joys)
joystick_id_combobox.grid(row = 0, column = 0)

# Select joystick button
#joy_button = tkinter.Button(frame, text = "Config shifter buttons", command = select_all)
#joy_button.grid(row = 1, column = 0)

# Joystick buttons selection
gears_selection_frame = tkinter.LabelFrame(frame, text = "Joystick Buttons")
gears_selection_frame.grid(row = 1, column = 0, padx= 20, pady = 5)

first_gear_button = tkinter.Button(gears_selection_frame, text = "1", command = select_first)
first_gear_button.grid(row = 2, column = 0)
first_gear_value = tkinter.Label(gears_selection_frame, text = first)
first_gear_value.grid(row = 3, column = 0)


second_gear_button = tkinter.Button(gears_selection_frame, text = "2", command = select_second)
second_gear_button.grid(row = 4, column = 0)
second_gear_value = tkinter.Label(gears_selection_frame, text = second)
second_gear_value.grid(row = 5, column = 0)


third_gear_button = tkinter.Button(gears_selection_frame, text = "3", command = select_third)
third_gear_button.grid(row = 2, column = 1)
third_gear_value = tkinter.Label(gears_selection_frame, text = third)
third_gear_value.grid(row = 3, column = 1)


fourth_gear_button = tkinter.Button(gears_selection_frame, text = "4", command = select_fourth)
fourth_gear_button.grid(row = 4, column = 1)
fourth_gear_value = tkinter.Label(gears_selection_frame, text = fourth)
fourth_gear_value.grid(row = 5, column = 1)


fifth_gear_button = tkinter.Button(gears_selection_frame, text = "5", command = select_fifth)
fifth_gear_button.grid(row = 2, column = 2)
fifth_gear_value = tkinter.Label(gears_selection_frame, text = fifth)
fifth_gear_value.grid(row = 3, column = 2)


sixth_gear_button = tkinter.Button(gears_selection_frame, text = "6", command = select_sixth)
sixth_gear_button.grid(row = 4, column = 2)
sixth_gear_value = tkinter.Label(gears_selection_frame, text = sixth)
sixth_gear_value.grid(row = 5, column = 2)


seventh_gear_button = tkinter.Button(gears_selection_frame, text = "7", command = select_seventh)
seventh_gear_button.grid(row = 2, column = 3)
seventh_gear_value = tkinter.Label(gears_selection_frame, text = seventh)
seventh_gear_value.grid(row = 3, column = 3)


reverse_gear_label = tkinter.Button(gears_selection_frame, text = "R", command = select_reverse)
reverse_gear_label.grid(row = 4, column = 3)
reverse_gear_value = tkinter.Label(gears_selection_frame, text = reverse)
reverse_gear_value.grid(row = 5, column = 3)


# Keys selection

keys_selection_frame = tkinter.LabelFrame(frame, text = "Key Selection")
keys_selection_frame.grid(row = 2, column = 0, padx= 20, pady = 5)

upshift_key_label = tkinter.Label(keys_selection_frame, text = "Upshift")
upshift_key_label.grid(row = 0, column = 0)
upshift_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
upshift_key_entry.insert(0, "S")
upshift_key_entry.grid(row = 0, column = 1)

neutral_key_label = tkinter.Label(keys_selection_frame, text = "Neutral")
neutral_key_label.grid(row = 1, column = 0)
neutral_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
neutral_key_entry.insert(0, "N")
neutral_key_entry.grid(row = 1, column = 1)

downshift_key_label = tkinter.Label(keys_selection_frame, text = "Downshift")
downshift_key_label.grid(row = 2, column = 0)
downshift_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
downshift_key_entry.insert(0, "Z")
downshift_key_entry.grid(row = 2, column = 1)

reverse_key_label = tkinter.Label(keys_selection_frame, text = "Reverse")
reverse_key_label.grid(row = 3, column = 0)
reverse_key_entry = tkinter.Entry(keys_selection_frame, width= 2)
reverse_key_entry.insert(0, "C")
reverse_key_entry.grid(row = 3, column = 1)

for widget in keys_selection_frame.winfo_children():
    widget.grid_configure(pady = 5)

# Options

options_selection_frame = tkinter.LabelFrame(frame, text = "Options")
options_selection_frame.grid(row = 3, column = 0, padx = 20, pady = 5)

neutral_var = tkinter.StringVar(value="False")
neutral_check = tkinter.Checkbutton(options_selection_frame, text= "Detect Neutral",
                                  variable=neutral_var, onvalue="True", offvalue="False")
neutral_check.grid(row=0, column=0)

seven_var = tkinter.StringVar(value="False")
seven_check = tkinter.Checkbutton(options_selection_frame, text= "Use seventh gear",
                                  variable=seven_var, onvalue="True", offvalue="False")
seven_check.grid(row=1, column=0)

rev_bool = tkinter.StringVar(value="False")
rev_check = tkinter.Checkbutton(options_selection_frame, text= "Reverse is a button",
                                  variable=rev_bool, onvalue="True", offvalue="False")
rev_check.grid(row=2, column=0)

nascar = tkinter.StringVar(value="False")
nascar_check = tkinter.Checkbutton(options_selection_frame, text= "Nascar mode",
                                  variable=nascar, onvalue="True", offvalue="False")
nascar_check.grid(row=3, column=0)

# Mem mode

memory_selection_frame = tkinter.LabelFrame(frame, text = "Memory mode")
memory_selection_frame.grid(row = 4, column = 0, padx = 20, pady = 5)

mem_mode = tkinter.StringVar(value="False")
mem_check = tkinter.Checkbutton(memory_selection_frame, text= "Active",
                                  variable=mem_mode, onvalue="True", offvalue="False")
                                  
mem_check.grid(row=0, column=0)

dosbase_key_label = tkinter.Label(memory_selection_frame, text = "DOSBox base address")
dosbase_key_label.grid(row = 1, column = 0)
dosbase_key_entry = tkinter.Entry(memory_selection_frame, width= 12)
dosbase_key_entry.insert(0, "0x01D3A1A0")
dosbase_key_entry.grid(row = 1, column = 1)

offset_key_label = tkinter.Label(memory_selection_frame, text = "Memory address offset")
offset_key_label.grid(row = 2, column = 0)
offset_key_entry = tkinter.Entry(memory_selection_frame, width= 12)
offset_key_entry.grid(row = 2, column = 1)

# Timers

timers_selection_frame = tkinter.LabelFrame(frame, text = "Delay values")
timers_selection_frame.grid(row = 5, column = 0, padx = 20, pady = 5)

press_key_label = tkinter.Label(timers_selection_frame, text = "Press key delay")
press_key_label.grid(row = 0, column = 0)
press_key_entry = tkinter.Entry(timers_selection_frame, width= 4)
press_key_entry.insert(0, "0.05")
press_key_entry.grid(row = 0, column = 1)

release_key_label = tkinter.Label(timers_selection_frame, text = "Release key delay")
release_key_label.grid(row = 1, column = 0)
release_key_entry = tkinter.Entry(timers_selection_frame, width= 4)
release_key_entry.insert(0, "0.2")
release_key_entry.grid(row = 1, column = 1)

# Profiles
profiles_selection_frame = tkinter.LabelFrame(frame, text = "Saved profiles")
profiles_selection_frame.grid(row = 6, column = 0, padx = 20, pady = 5)

juegos = []
lista = []
with open("presets.csv", "r") as file:
    reader = csv.DictReader(file)    
    counter = 0
    for row in reader:  # Load csv in a list of dictionaries
        juegos.append(row)
        lista.append(row['name'])

presets_combobox = ttk.Combobox(profiles_selection_frame, values = lista, width = 30)
presets_combobox.grid(row = 0, column = 0) 

name = presets_combobox.get()
index = 0
for game in juegos:
    if game['name'] == name:
        index = game['id']

button = tkinter.Button(profiles_selection_frame, text="Load profile", command= load_data(juegos, index))
button.grid(row=1, column=0, sticky="news", padx=20, pady = 5)

# Save data button
button = tkinter.Button(frame, text="Save to .ini", command= save_data)
button.grid(row=8, column=0, sticky="news", padx=20, pady = 5)

# Run Button
run_button = tkinter.Button(frame, text="Run Anyshift", command= run_any)
run_button.grid(row=9, column=0, sticky="news", padx=20, pady = 5)

window.mainloop()