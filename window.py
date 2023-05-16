import tkinter
from tkinter import ttk
import pygame
import configparser
import keyboard

def save_data():
    joy = joystick_id_combobox.get()
    first_gear = first_gear_entry.get()
    second_gear = second_gear_entry.get()
    third_gear = third_gear_entry.get()
    fourth_gear = fourth_gear_entry.get()
    fifth_gear = fifth_gear_entry.get() 
    sixth_gear = sixth_gear_entry.get()
    seventh_gear = seventh_gear_entry.get()
    reverse = reverse_gear_entry.get()
    upshift = upshift_key_entry.get()
    neut_key = neutral_key_entry.get()
    downshift = downshift_key_entry.get()
    seven_gears = seven_var.get()
    neutral = neutral_var.get()

    # Create object config
    config = configparser.ConfigParser()

    # Set configuration
    config['SHIFTER'] = {'Joystick id': joy,                   
                       'first gear': first_gear,
                       'second gear': second_gear,
                       'third gear': third_gear,
                       'fourth gear': fourth_gear,
                       'fifth gear': fifth_gear,
                       'sixth gear': sixth_gear,
                       'seventh gear': seventh_gear,
                       'reverse button': reverse                   
                       }

    config['KEYS'] = {'upshift': upshift,
                    'downshift': downshift,
                    'neutral keyboard key': neut_key
                     }   

    config['OPTIONS'] = {'seven gears': seven_gears,
                        'neutral detection': neutral,
                        'presskey timer': 0.2,  
                        'releasekey timer': 0.5
                        }

    # Write the file
    with open("Anyshift.ini", "w") as configfile:
        config.write(configfile)

def joystick_activation():


    active_joystick = joystick_id_combobox.get()
    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i
    
    shifter = pygame.joystick.Joystick(active_joystick_id)
    shifter.init()
    num_buttons = shifter.get_numbuttons()

    done = False
    while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        keyboard.press_and_release(i)                        
                        
              

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
window.title("Anyshift Config Tool")

frame = tkinter.Frame(window)
frame.pack()

# Joystick buttons selection
gears_selection_frame = tkinter.LabelFrame(frame, text = "Joystick Buttons")
gears_selection_frame.grid(row = 0, column = 0, padx= 20, pady = 20)

joystick_id_label = tkinter.Label(gears_selection_frame, text = "Joystick id")
joystick_id_combobox = ttk.Combobox(gears_selection_frame, values = joys)
joystick_id_label.grid(row = 0, column = 0)
joystick_id_combobox.grid(row = 1, column = 0)

# Select joystick button
joy_button = tkinter.Button(gears_selection_frame, text = "Activate selected joystick", command = joystick_activation)
joy_button.grid(row = 0, column = 1)

first_gear_label = tkinter.Label(gears_selection_frame, text = "1")
first_gear_label.grid(row = 2, column = 0)
first_gear_entry = tkinter.Entry(gears_selection_frame)
first_gear_entry.grid(row = 3, column = 0)


second_gear_label = tkinter.Label(gears_selection_frame, text = "2")
second_gear_label.grid(row = 4, column = 0)
second_gear_entry = tkinter.Entry(gears_selection_frame)
second_gear_entry.grid(row = 5, column = 0)


third_gear_label = tkinter.Label(gears_selection_frame, text = "3")
third_gear_label.grid(row = 2, column = 1)
third_gear_entry = tkinter.Entry(gears_selection_frame)
third_gear_entry.grid(row = 3, column = 1)


fourth_gear_label = tkinter.Label(gears_selection_frame, text = "4")
fourth_gear_label.grid(row = 4, column = 1)
fourth_gear_entry = tkinter.Entry(gears_selection_frame)
fourth_gear_entry.grid(row = 5, column = 1)


fifth_gear_label = tkinter.Label(gears_selection_frame, text = "5")
fifth_gear_label.grid(row = 2, column = 2)
fifth_gear_entry = tkinter.Entry(gears_selection_frame)
fifth_gear_entry.grid(row = 3, column = 2)


sixth_gear_label = tkinter.Label(gears_selection_frame, text = "6")
sixth_gear_label.grid(row = 4, column = 2)
sixth_gear_entry = tkinter.Entry(gears_selection_frame)
sixth_gear_entry.grid(row = 5, column = 2)


seventh_gear_label = tkinter.Label(gears_selection_frame, text = "7")
seventh_gear_label.grid(row = 2, column = 3)
seventh_gear_entry = tkinter.Entry(gears_selection_frame)
seventh_gear_entry.grid(row = 3, column = 3)


reverse_gear_label = tkinter.Label(gears_selection_frame, text = "R")
reverse_gear_label.grid(row = 4, column = 3)
reverse_gear_entry = tkinter.Entry(gears_selection_frame)
reverse_gear_entry.grid(row = 5, column = 3)


for widget in gears_selection_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# Keys selection

keys_selection_frame = tkinter.LabelFrame(frame, text = "Key Selection")
keys_selection_frame.grid(row = 1, column = 1, padx= 20, pady = 20)

upshift_key_label = tkinter.Label(keys_selection_frame, text = "Upshift")
upshift_key_label.grid(row = 0, column = 0)
upshift_key_entry = tkinter.Entry(keys_selection_frame)
upshift_key_entry.grid(row = 0, column = 1)

neutral_key_label = tkinter.Label(keys_selection_frame, text = "Neutral")
neutral_key_label.grid(row = 1, column = 0)
neutral_key_entry = tkinter.Entry(keys_selection_frame)
neutral_key_entry.grid(row = 1, column = 1)

downshift_key_label = tkinter.Label(keys_selection_frame, text = "Downshift")
downshift_key_label.grid(row = 2, column = 0)
downshift_key_entry = tkinter.Entry(keys_selection_frame)
downshift_key_entry.grid(row = 2, column = 1)

for widget in keys_selection_frame.winfo_children():
    widget.grid_configure(pady = 5)

# Options

options_selection_frame = tkinter.LabelFrame(frame, text = "Options")
options_selection_frame.grid(row = 1, column = 0, padx = 20, pady = 20)

neutral_var = tkinter.StringVar(value="False")
neutral_check = tkinter.Checkbutton(options_selection_frame, text= "Detect Neutral",
                                  variable=neutral_var, onvalue="True", offvalue="False")
neutral_check.grid(row=0, column=0)

seven_var = tkinter.StringVar(value="False")
seven_check = tkinter.Checkbutton(options_selection_frame, text= "Use seventh gear",
                                  variable=seven_var, onvalue="True", offvalue="False")
seven_check.grid(row=1, column=0)

# Save data button
button = tkinter.Button(frame, text="Save config", command= save_data)
button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

pygame.init() 
window.mainloop()