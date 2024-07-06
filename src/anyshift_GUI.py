#########################################################################################################
# Anyshift GUI
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
#########################################################################################################

from tkinter import Tk, Button
from tkinter import *  # Toplevel window
from tkinter import ttk  # GUI combobox
import csv  # Load and write csv files
from Gearbox import joystick_loop
from ShifterConfig import gear_selection, joystick_lister
from ReadWriteSaves import ini_reader, ini_writer, hex_convert, char_convert
import webbrowser
import threading

# Get active joystick of combobox anc calls gear selection to select button for the desired gear
def gears(gear):

    global options
    read_options_from_windows()
    gear_selection(options, gear)
    
    # Show characters no hex code as we came from read options from windows not read ini
    options['up_key'] = char_convert(options['up_key'])
    options['down_key'] = char_convert(options['down_key'])
    options['rev_key'] = char_convert(options['rev_key'])    
    windows_updater()



# Tkinter window class
class GUI(Tk):

    def __init__(self, options, joys):

        super().__init__()
        self.title("Anyshift")
        self.iconbitmap("any_ico.ico")
        self.resizable(False, False)
        
        # Create frame
        self.frame = Frame()
        self.frame.pack()

        # Joystick selection
        self.joystick_frame = LabelFrame(self.frame, text = "Joysticks selection")
        self.joystick_frame.grid(row = 0, column = 0, padx= 10, pady = 5)
        
        # No joystick connected check
        try:
            self.shifter_label = Label(self.joystick_frame, text="Shifter")
            self.shifter_label.grid(row=0, column=0)
            self.joystick_id_combobox = ttk.Combobox(self.joystick_frame, values=joys)
            self.joystick_id_combobox.current(options['joy_id'])
            self.joystick_id_combobox.grid(row = 1, column = 0)
            self.clutch_var = StringVar(value = options['clutch'])
            self.clutch_check = Checkbutton(self.joystick_frame, text= "Clutch",
                                            variable=self.clutch_var, onvalue="True", offvalue="False")
            self.clutch_check.grid(row=0, column=1)
            self.clutch_id_combobox = ttk.Combobox(self.joystick_frame, values = joys)
            self.clutch_id_combobox.current(options['clutch_id'])
            self.clutch_id_combobox.grid(row = 1, column = 1, padx=(0,1))
        except:
            # Case no devices connected
            if len(joys) == 0:
                error_label = Label(self.joystick_frame, text = "No devices connected.")
                error_label.grid(row = 0, column = 0)
                error_label = Label(self.joystick_frame, text = "Connect at least one device")
                error_label.grid(row = 1, column = 0)
                error_label = Label(self.joystick_frame, text = "and launch Anyshift again")
                error_label.grid(row = 2, column = 0)
            # Case .ini device not coneccted, it default to joy_id = 0
            else:
                self.shifter_label = Label(self.joystick_frame, text="Shifter")
                self.shifter_label.grid(row=0, column=0)
                self.joystick_id_combobox = ttk.Combobox(self.joystick_frame, values=joys)
                self.joystick_id_combobox.current(0)
                self.joystick_id_combobox.grid(row = 1, column = 0)
                self.clutch_var = StringVar(value = options['clutch'])
                self.clutch_check = Checkbutton(self.joystick_frame, text= "Clutch",
                                                variable=self.clutch_var, onvalue="True", offvalue="False")
                self.clutch_check.grid(row=0, column=1)
                self.clutch_id_combobox = ttk.Combobox(self.joystick_frame, values = joys)
                self.clutch_id_combobox.current(0)
                self.clutch_id_combobox.grid(row = 1, column = 1, padx=(0,1))
 
        #region JOYSTICK BUTTONS
        self.gears_selection_frame = LabelFrame(self.frame, text = "Joystick Buttons")
        self.gears_selection_frame.grid(row = 1, column = 0)

        self.first_gear_button = Button(self.gears_selection_frame, text = "1", command = lambda: gears(1))
        self.first_gear_button.grid(row = 2, column = 0, padx=(10,0))
        self.first_gear_value = Label(self.gears_selection_frame, text = options['first'])
        self.first_gear_value.grid(row = 3, column = 0, padx=(10,0))

        self.second_gear_button = Button(self.gears_selection_frame, text = "2", command = lambda: gears(2))
        self.second_gear_button.grid(row = 4, column = 0, padx=(10,0))
        self.second_gear_value = Label(self.gears_selection_frame, text = options['second'])
        self.second_gear_value.grid(row = 5, column = 0, padx=(10,0))

        self.third_gear_button = Button(self.gears_selection_frame, text = "3", command = lambda: gears(3))
        self.third_gear_button.grid(row = 2, column = 1)
        self.third_gear_value = Label(self.gears_selection_frame, text = options['third'])
        self.third_gear_value.grid(row = 3, column = 1)

        self.fourth_gear_button = Button(self.gears_selection_frame, text = "4", command = lambda: gears(4))
        self.fourth_gear_button.grid(row = 4, column = 1)
        self.fourth_gear_value = Label(self.gears_selection_frame, text = options['fourth'])
        self.fourth_gear_value.grid(row = 5, column = 1)

        self.fifth_gear_button = Button(self.gears_selection_frame, text = "5", command = lambda: gears(5))
        self.fifth_gear_button.grid(row = 2, column = 2)
        self.fifth_gear_value = Label(self.gears_selection_frame, text = options['fifth'])
        self.fifth_gear_value.grid(row = 3, column = 2)

        self.sixth_gear_button = Button(self.gears_selection_frame, text = "6", command = lambda: gears(6))
        self.sixth_gear_button.grid(row = 4, column = 2)
        self.sixth_gear_value = Label(self.gears_selection_frame, text = options['sixth'])
        self.sixth_gear_value.grid(row = 5, column = 2)

        self.seventh_gear_button = Button(self.gears_selection_frame, text = "7", command = lambda: gears(7))
        self.seventh_gear_button.grid(row = 2, column = 3)
        self.seventh_gear_value = Label(self.gears_selection_frame, text = options['seventh'])
        self.seventh_gear_value.grid(row = 3, column = 3)

        self.clutch_axis = Button(self.gears_selection_frame, text = "Clutch Axis", command = lambda: gears(10))
        self.clutch_axis.grid(row = 2, column = 4, padx=(25,0))
        self.clutch_axis_value = Label(self.gears_selection_frame, text = options['clutch_axis'])  
        self.clutch_axis_value.grid(row = 3, column = 4, padx=(25,0))        

        self.reverse_gear_label = Button(self.gears_selection_frame, text = "R", command = lambda: gears(8))
        self.reverse_gear_label.grid(row = 4, column = 3)
        self.reverse_gear_value = Label(self.gears_selection_frame, text = options['reverse'])
        self.reverse_gear_value.grid(row = 5, column = 3)

        self.bitepoint_label = Label(self.gears_selection_frame, text = "        Bitepoint:")
        self.bitepoint_label.grid(row = 4, column = 4)
        self.bitepoint_entry = Entry(self.gears_selection_frame, width= 3)
        self.bitepoint_entry.insert(0, options['bitepoint'])
        self.bitepoint_entry.grid(row = 4, column = 5)
        self.bitepoint2_label = Label(self.gears_selection_frame, text = "%")
        self.bitepoint2_label.grid(row = 4, column = 6, padx=(0,5))

        #region KEYS
        # Keys selection

        self.keys_selection_frame = LabelFrame(self.frame, text = "Key Selection")
        self.keys_selection_frame.grid(row = 2, column = 0)

        self.upshift_key_label = Label(self.keys_selection_frame, text = "Upshift")
        self.upshift_key_label.grid(row = 0, column = 0)
        self.upshift_key_entry = Entry(self.keys_selection_frame, width= 2)
        self.upshift_key_entry.insert(0, options['up_key'])
        self.upshift_key_entry.grid(row = 0, column = 1)

        self.downshift_key_label = Label(self.keys_selection_frame, text = "Downshift")
        self.downshift_key_label.grid(row = 1, column = 0)
        self.downshift_key_entry = Entry(self.keys_selection_frame, width= 2)
        self.downshift_key_entry.insert(0, options['down_key'])
        self.downshift_key_entry.grid(row = 1, column = 1)

        self.neutral_key_label = Label(self.keys_selection_frame, text = "Neutral")
        self.neutral_key_label.grid(row = 0, column = 2)
        self.neutral_key_entry = Entry(self.keys_selection_frame, width= 2)
        self.neutral_key_entry.insert(0, options['neut_key'])
        self.neutral_key_entry.grid(row = 0, column = 3)

        self.reverse_key_label = Label(self.keys_selection_frame, text = "Reverse")
        self.reverse_key_label.grid(row = 1, column = 2)
        self.reverse_key_entry = Entry(self.keys_selection_frame, width= 2)
        self.reverse_key_entry.insert(0, options['rev_key'])
        self.reverse_key_entry.grid(row = 1, column = 3)

        #region TIMERS

        self.press_key_label = Label(self.keys_selection_frame, text = "Press key delay")
        self.press_key_label.grid(row = 2, column = 0)
        self.press_key_entry = Entry(self.keys_selection_frame, width= 4)
        self.press_key_entry.insert(0, options['presskey_timer'])
        self.press_key_entry.grid(row = 2, column = 1)

        self.release_key_label = Label(self.keys_selection_frame, text = "Release key delay")
        self.release_key_label.grid(row = 2, column = 2)
        self.release_key_entry = Entry(self.keys_selection_frame, width= 4)
        self.release_key_entry.insert(0, options['releasekey_timer'])
        self.release_key_entry.grid(row = 2, column = 3, padx=(0,6))

        for widget in self.keys_selection_frame.winfo_children():
            widget.grid_configure(pady = 5)

        #region OPTIONS

        self.options_selection_frame = LabelFrame(self.frame, text = "Options")
        self.options_selection_frame.grid(row = 3, column = 0, padx = 20, pady = 5)

        self.neutral_var = StringVar(value = options['neutral'])
        self.neutral_check = Checkbutton(self.options_selection_frame, text= "Detect Neutral",
                                        variable=self.neutral_var, onvalue="True", offvalue="False")
        self.neutral_check.grid(row=0, column=0)

        
        self.neutral_delay_label = Label(self.options_selection_frame, text = "             Neutral Delay")
        self.neutral_delay_label.grid(row = 0, column = 1)
        self.neutral_delay_entry = Entry(self.options_selection_frame, width= 4)
        self.neutral_delay_entry.insert(0, options['neutral_wait_time'])
        self.neutral_delay_entry.grid(row = 0, column = 2)

        self.seven_var = StringVar(value = options['seven_gears'])
        self.seven_check = Checkbutton(self.options_selection_frame, text= "Use seventh gear",
                                        variable=self.seven_var, onvalue="True", offvalue="False")
        self.seven_check.grid(row=1, column=0)

        self.rev_bool = StringVar(value = options['rev_button'])
        self.rev_check = Checkbutton(self.options_selection_frame, text= "Reverse is a button",
                                        variable=self.rev_bool, onvalue="True", offvalue="False")
        self.rev_check.grid(row=1, column=1)

        self.nascar = StringVar(value = options['nascar_mode'])
        self.nascar_check = Checkbutton(self.options_selection_frame, text= "Nascar mode",
                                        variable=self.nascar, onvalue="True", offvalue="False")
        self.nascar_check.grid(row=1, column=2)

        # Mem mode
        self.memory_selection_frame = LabelFrame(self.frame, text = "Memory mode")
        self.memory_selection_frame.grid(row = 4, column = 0, padx = 20, pady = 5)

        self.mem_var = StringVar(value = options['mem_mode'])
        self.mem_check = Checkbutton(self.memory_selection_frame, text= "Active",
                                        variable=self.mem_var, onvalue="True", offvalue="False")                                  
        self.mem_check.grid(row=0, column=0)

        self.process_label = Label(self.memory_selection_frame, text = "Process name")
        self.process_label.grid(row = 1, column = 0)
        self.process_key_entry = Entry(self.memory_selection_frame, width= 12)
        self.process_key_entry.insert(0, options['process'])
        self.process_key_entry.grid(row = 1, column = 1, padx=(0,10))

        self.dosbase_key_label = Label(self.memory_selection_frame, text = "Base address")
        self.dosbase_key_label.grid(row = 2, column = 0)
        self.dosbase_key_entry = Entry(self.memory_selection_frame, width= 12)
        self.dosbase_key_entry.insert(0, options['db_base_addr'])
        self.dosbase_key_entry.grid(row = 2, column = 1, padx=(0,10))

        self.offset_key_label = Label(self.memory_selection_frame, text = "Memory address offset")
        self.offset_key_label.grid(row = 3, column = 0)
        self.offset_key_entry = Entry(self.memory_selection_frame, width= 12)
        self.offset_key_entry.insert(0, options['offset'])
        self.offset_key_entry.grid(row = 3, column = 1, padx=(0,10))

        # Gear values
        self.process_label = Label(self.memory_selection_frame, text = "Gear values ingame:")
        self.process_label.grid(row = 0, column =2, columnspan=8)

        self.first_gear_value_label = Label(self.memory_selection_frame, text = "1:")
        self.first_gear_value_label.grid(row = 1, column = 3)
        self.first_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.first_gear_value_entry.grid(row = 1, column = 4)
        self.first_gear_value_entry.insert(0, options['first_value'])

        self.third_gear_value_label = Label(self.memory_selection_frame, text = "3:")
        self.third_gear_value_label.grid(row = 1, column = 5)
        self.third_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.third_gear_value_entry.grid(row = 1, column = 6)
        self.third_gear_value_entry.insert(0, options['third_value'])

        self.fifth_gear_value_label = Label(self.memory_selection_frame, text = "5:")
        self.fifth_gear_value_label.grid(row = 1, column = 7)
        self.fifth_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.fifth_gear_value_entry.grid(row = 1, column = 8)
        self.fifth_gear_value_entry.insert(0, options['fifth_value'])

        self.seventh_gear_value_label = Label(self.memory_selection_frame, text = "7:")
        self.seventh_gear_value_label.grid(row = 1, column = 9)
        self.seventh_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.seventh_gear_value_entry.grid(row = 1, column = 10, padx=(0,8))
        self.seventh_gear_value_entry.insert(0, options['seventh_value'])

        self.neutral_gear_value_label = Label(self.memory_selection_frame, text = "N:")
        self.neutral_gear_value_label.grid(row = 2, column = 6)
        self.neutral_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.neutral_gear_value_entry.grid(row = 2, column = 7)
        self.neutral_gear_value_entry.insert(0, options['neutral_value'])        

        self.second_gear_value_label = Label(self.memory_selection_frame, text = "2:")
        self.second_gear_value_label.grid(row = 3, column = 3)
        self.second_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.second_gear_value_entry.grid(row = 3, column = 4)
        self.second_gear_value_entry.insert(0, options['second_value'])

        self.fourth_gear_value_label = Label(self.memory_selection_frame, text = "4:")
        self.fourth_gear_value_label.grid(row = 3, column = 5)
        self.fourth_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.fourth_gear_value_entry.grid(row = 3, column = 6)
        self.fourth_gear_value_entry.insert(0, options['fourth_value'])

        self.sixth_gear_value_label = Label(self.memory_selection_frame, text = "6:")
        self.sixth_gear_value_label.grid(row = 3, column = 7)
        self.sixth_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.sixth_gear_value_entry.grid(row = 3, column = 8)
        self.sixth_gear_value_entry.insert(0, options['sixth_value'])

        self.reverse_gear_value_label = Label(self.memory_selection_frame, text = "R:")
        self.reverse_gear_value_label.grid(row = 3, column = 9)
        self.reverse_gear_value_entry = Entry(self.memory_selection_frame, width= 2)        
        self.reverse_gear_value_entry.grid(row = 3, column = 10, padx=(0,8))
        self.reverse_gear_value_entry.insert(0, options['reverse_value'])       
        

        # Profiles
        profiles_selection_frame = LabelFrame(self.frame, text = "Profiles")
        profiles_selection_frame.grid(row = 6, column = 0, padx = 20, pady = 5)

        # Presets buttons
        lista = []
        with open("presets.csv", "r") as file:
            reader = csv.DictReader(file)    
            for row in reader:  # Load csv in a list of dictionaries
                lista.append(row['name'])

        self.presets_combobox = ttk.Combobox(profiles_selection_frame, values = lista, width = 30)
        self.presets_combobox.grid(row = 0, column = 1) 


        self.load_button = Button(profiles_selection_frame, text="Load profile", command= load_preset)
        self.load_button.grid(row=0, column=0, sticky="news", padx=20, pady = 5)

        self.save_button = Button(profiles_selection_frame, text="Save profile", command= save_preset)  
        self.save_button.grid(row=1, column=0, sticky="news", padx=20, pady = 5)

        self.save_name_entry = Entry(profiles_selection_frame, width= 33)
        self.save_name_entry.grid(row = 1, column = 1)

        # Save data button
        self.save_data_button = Button(self.frame, text="Remember current options", command= write_ini)
        self.save_data_button.grid(row=8, column=0, sticky="news", padx=10, pady = 5)

        # Run Button
        self.run_button = Button(self.frame, text="Run Anyshift", command= run_any)
        self.run_button.grid(row=9, column=0, sticky="news", padx=10, pady = 5)

        # Buyme a coffe
        self.pay_label = Label(self.frame, fg="blue", cursor="hand2", text = "Do you like Anyshift?. If so, you can buy me a coffee")
        self.pay_label.grid(row = 10, column = 0)
        self.pay_label.bind("<Button-1>", lambda e: callback("https://www.buymeacoffee.com/Menkaura"))

    
if __name__ == "__main__":    
    # Read config from ini file
    options = ini_reader()
    # Get list of joystick ids and save them into joys list
    joys, num_joy = joystick_lister()  # Get joystick list and count. Is a little sketchy but i don´t know hot to do it betterat the momment
    # Create windows object and run tkinter loop
    app = GUI(options, joys)
    app.mainloop() 