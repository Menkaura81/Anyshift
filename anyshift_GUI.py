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
from ReadWriteMemory import ReadWriteMemory  # Memory writing
from Gearbox import joystick_loop_keys, joystick_loop_mem
from ShifterConfig import gear_selection, joystick_lister
from ReadWriteSaves import ini_reader, ini_writer, hex_convert, char_convert
import webbrowser

# Open buymeacoffee link
def callback(url):
    webbrowser.open_new(url)

# Read config from presets.csv
def load_preset():

    # Read presets.csv and store data in a list of dictionaries
    juegos = []    
    with open("presets.csv", "r") as file:
        reader = csv.DictReader(file)    
        for row in reader:  
            juegos.append(row)
                
    # Read selected preset in combobox
    name = app.presets_combobox.get()
    index = 0
    for game in juegos:
        if game['name'] == name:
            index = int(game['id'])
    
    # Load variables from dictionary
    global options 
    options['up_key'] = juegos[index]['upshift']    
    options['up_key'] = options['up_key']
    options['down_key'] = juegos[index]['downshift']
    options['down_key'] = options['down_key']
    options['rev_key'] = juegos[index]['reverse']
    options['rev_key']  = options['rev_key']
    options['neut_key'] = juegos[index]['neutral key']    
    options['seven_gears'] = juegos[index]['seven gears']
    options['neutral'] = juegos[index]['neutral detection']
    options['rev_button'] = juegos[index]['reverse is button']
    options['nascar_mode'] = juegos[index]['nascar racing mode']
    options['presskey_timer'] = juegos[index]['presskey timer']    
    options['releasekey_timer'] = juegos[index]['releasekey timer']    
    options['mem_mode'] = juegos[index]['memory write mode']
    options['process'] = juegos[index]['process name']    
    options['db_base_addr'] = juegos[index]['base address']    
    options['offset'] = juegos[index]['offset']
    options['first_value'] = juegos[index]['first value']
    options['second_value'] = juegos[index]['second value']
    options['third_value'] = juegos[index]['third value']
    options['fourth_value'] = juegos[index]['fourth value']
    options['fifth_value'] = juegos[index]['fifth value']
    options['sixth_value'] = juegos[index]['sixth value']
    options['seventh_value'] = juegos[index]['seventh value']
    options['reverse_value'] = juegos[index]['reverse value']
    options['neutral_value'] = juegos[index]['neutral value']  
    
    # Update windows with read values
    windows_updater()


# Save actual config displayed in windows into presets.csv
def save_preset():
    
    preset = []
    keys = []

    counter = 0
    with open("presets.csv", "r") as file:
        reader = csv.DictReader(file)    
        for row in reader:  # Count csv profiles
            counter += 1
            
    id = counter
    preset.append(id)

    name = app.save_name_entry.get()
    if name:  # Check if we have a name to save the preset
        preset.append(name)

        upshift = app.upshift_key_entry.get()[:1].lower()
        if ord(upshift) >= 97 and ord(upshift) <= 122:
            preset.append(upshift)
            keys.append(upshift)
        else:
            error_window = Toplevel(app)        
            error_window.title("Error")
            error_window.config(width=200, height=50)
            error_frame = Frame(error_window)
            error_frame.pack()
            error_label = Label(error_frame, text = "Upshift key error. Only one char (a to z)")
            error_label.grid(row = 0, column = 0)
            return
        
        downshift = app.downshift_key_entry.get()[:1].lower()
        if ord(downshift) >= 97 and ord(downshift) <= 122 and downshift not in keys:
            preset.append(downshift)
            keys.append(downshift)
        else:
            error_window = Toplevel(app)        
            error_window.title("Error")
            error_window.config(width=200, height=50)
            error_frame = Frame(error_window)
            error_frame.pack()
            error_label = Label(error_frame, text = "Downshift key error. Repeated or not a to z char")
            error_label.grid(row = 0, column = 0)
            return
        
        reverse = app.reverse_key_entry.get()[:1].lower() 
        if ord(reverse) >= 97 and ord(reverse) <= 122 and reverse not in keys:
            preset.append(reverse)
            keys.append(reverse)
        else:
            error_window = Toplevel(app)        
            error_window.title("Error")
            error_window.config(width=200, height=50)
            error_frame = Frame(error_window)
            error_frame.pack()
            error_label = Label(error_frame, text = "Reverse key error. Repeated or not a to z char")
            error_label.grid(row = 0, column = 0) 
            return
        
        neutral = app.neutral_key_entry.get()[:1].lower()
        if ord(neutral) >= 97 and ord(neutral) <= 122 and neutral not in keys:
            preset.append(neutral)
            keys.append(neutral)
        else:
            error_window = Toplevel(app)        
            error_window.title("Error")
            error_window.config(width=200, height=50)
            error_frame = Frame(error_window)
            error_frame.pack()
            error_label = Label(error_frame, text = "Neutral key error. Only one char (a to z)")
            error_label.grid(row = 0, column = 0) 
            return
        
        preset.append(app.seven_var.get())
        preset.append(app.neutral_var.get())
        preset.append(app.rev_bool.get())
        preset.append(app.nascar.get())
        preset.append(app.mem_var.get())
        preset.append(app.process_key_entry.get())
        preset.append(app.dosbase_key_entry.get())
        preset.append(app.offset_key_entry.get())
        preset.append(app.press_key_entry.get())
        preset.append(app.release_key_entry.get())
        preset.append(app.neutral_gear_value_entry.get())
        preset.append(app.first_gear_value_entry.get())
        preset.append(app.second_gear_value_entry.get())
        preset.append(app.third_gear_value_entry.get())
        preset.append(app.fourth_gear_value_entry.get())
        preset.append(app.fifth_gear_value_entry.get())
        preset.append(app.sixth_gear_value_entry.get())
        preset.append(app.seventh_gear_value_entry.get())
        preset.append(app.reverse_gear_value_entry.get())

        with open('presets.csv', 'a') as file: 
            # Pass this file object to csv.writer()
            # and get a writer object
            writer = csv.writer(file) 
            # Pass the list as an argument into
            # the writerow()
            writer.writerow(preset) 
            # Close the file object
            file.close()
    else:
        return
    

# Read options displayed in windows and store the into options[]
def read_options_from_windows():
    
    global options 
    keys = []  # To keep track of already selected keys

    joys, num_joy = joystick_lister()  # Get joystick list and count   
    active_joystick = app.joystick_id_combobox.get()
    active_clutch =  app.clutch_id_combobox.get()

    for i in range(num_joy):
        if joys[i] == active_joystick:
            active_joystick_id = i 

    for i in range(num_joy):
        if joys[i] == active_clutch:
            active_clutch_id = i
       

    options['joy_id'] = active_joystick_id
    options['clutch_id'] = active_clutch_id

    options['clutch'] = app.clutch_var.get()
    
    upshift = app.upshift_key_entry.get()[:1].lower()
    if ord(upshift) >= 97 and ord(upshift) <= 122:
        keys.append(upshift)
        options['up_key'] =  hex_convert(upshift)
    else:
        error_window = Toplevel(app)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = Frame(error_window)
        error_frame.pack()
        error_label = Label(error_frame, text = "Upshift key error. Only one char (a to z)")
        error_label.grid(row = 0, column = 0)
        return    
    
    downshift = app.downshift_key_entry.get()[:1].lower()
    if ord(downshift) >= 97 and ord(downshift) <= 122 and downshift not in keys:
        keys.append(downshift)
        options['down_key'] = hex_convert(downshift)
    else:
        error_window = Toplevel(app)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = Frame(error_window)
        error_frame.pack()
        error_label = Label(error_frame, text = "Downshift key error. Repeated or not a to z char")
        error_label.grid(row = 0, column = 0)
        return
    
    rev_key = app.reverse_key_entry.get()[:1].lower() 
    if ord(rev_key) >= 97 and ord(rev_key) <= 122 and rev_key not in keys:
        options['rev_key'] = hex_convert(rev_key)
        keys.append(rev_key)
    else:
        error_window = Toplevel(app)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = Frame(error_window)
        error_frame.pack()
        error_label = Label(error_frame, text = "Reverse key error. Repeated or not a to z char")
        error_label.grid(row = 0, column = 0) 
        return 

    neut_key = app.neutral_key_entry.get()[:1].lower()
    if ord(neut_key) >= 97 and ord(neut_key) <= 122 and neut_key not in keys:
        options['neut_key'] = neut_key
        keys.append(neut_key)
    else:
        error_window = Toplevel(app)        
        error_window.title("Error")
        error_window.config(width=200, height=50)
        error_frame = Frame(error_window)
        error_frame.pack()
        error_label = Label(error_frame, text = "Neutral key error. Only one char (a to z)")
        error_label.grid(row = 0, column = 0) 
        return  
    
    options['seven_gears'] = app.seven_var.get()
    options['neutral'] = app.neutral_var.get()
    options['rev_button'] = app.rev_bool.get()
    options['nascar_mode'] = app.nascar.get()
    options['mem_mode'] = app.mem_var.get()
    process = app.process_key_entry.get()
    options['process'] = process
    db_base_addr = app.dosbase_key_entry.get()
    options['db_base_addr'] = db_base_addr
    offset = app.offset_key_entry.get()
    options['offset'] = offset
    presskey_timer = app.press_key_entry.get()
    options['presskey_timer'] = presskey_timer
    releasekey_timer = app.release_key_entry.get()
    options['releasekey_timer'] = releasekey_timer

    options['first_value'] = app.first_gear_value_entry.get()
    options['second_value'] = app.second_gear_value_entry.get()
    options['third_value'] = app.third_gear_value_entry.get()
    options['fourth_value'] = app.fourth_gear_value_entry.get()
    options['fifth_value'] = app.fifth_gear_value_entry.get()
    options['sixth_value'] = app.sixth_gear_value_entry.get()
    options['seventh_value'] = app.seventh_gear_value_entry.get()
    options['reverse_value'] = app.reverse_gear_value_entry.get()
    options['neutral_value'] = app.neutral_gear_value_entry.get()

    options['bitepoint'] = app.bitepoint_entry.get()[:2]

# Write ini file to remember current options
def write_ini():
    
    read_options_from_windows()
    
    # Store char, not hex code
    upshift = char_convert(options['up_key'])
    downshift = char_convert(options['down_key'])
    rev_key = char_convert(options['rev_key'])  
    
    ini_writer(options, upshift, downshift, rev_key)


# Update windows whem a joystick button is configured
def windows_updater():
    
    global options
    # configure
    app.first_gear_value.config(text = options['first'])
    app.second_gear_value.config(text = options['second'])
    app.third_gear_value.config(text = options['third'])
    app.fourth_gear_value.config(text = options['fourth'])
    app.fifth_gear_value.config(text = options['fifth'])
    app.sixth_gear_value.config(text = options['sixth'])
    app.seventh_gear_value.config(text = options['seventh'])
    app.reverse_gear_value.config(text = options['reverse'])
    
       
    app.clutch_axis_value = Label(app.gears_selection_frame, text = options['clutch_axis'])  
    app.clutch_axis_value.grid(row = 3, column = 4, padx=(25,10))

    app.upshift_key_entry.delete(0, 4)  
    app.upshift_key_entry.insert(0, options['up_key'])

    app.downshift_key_entry.delete(0, 4)  
    app.downshift_key_entry.insert(0, options['down_key'])

    app.reverse_key_entry.delete(0, 4)  
    app.reverse_key_entry.insert(0, options['rev_key'])

    app.neutral_key_entry.delete(0, 2) 
    app.neutral_key_entry.insert(0, options['neut_key'])

    # Update checks in window 
    app.neutral_var = StringVar(value = options['neutral'])
    app.neutral_check = Checkbutton(app.options_selection_frame, text= "Detect Neutral",
                                variable=app.neutral_var, onvalue="True", offvalue="False")
    app.neutral_check.grid(row=0, column=0)
    
    app.seven_var = StringVar(value = options['seven_gears'])
    app.seven_check = Checkbutton(app.options_selection_frame, text= "Use seventh gear",
                                  variable=app.seven_var, onvalue="True", offvalue="False")
    app.seven_check.grid(row=1, column=0)
    
    app.rev_bool = StringVar(value = options['rev_button'])
    app.rev_check = Checkbutton(app.options_selection_frame, text= "Reverse is a button",
                                  variable=app.rev_bool, onvalue="True", offvalue="False")
    app.rev_check.grid(row=0, column=1)
    
    app.nascar = StringVar(value = options['nascar_mode'])
    app.nascar_check = Checkbutton(app.options_selection_frame, text= "Nascar mode",
                                  variable=app.nascar, onvalue="True", offvalue="False")
    app.nascar_check.grid(row=1, column=1)
    
    app.mem_var = StringVar(value = options['mem_mode'])
    app.mem_check = Checkbutton(app.memory_selection_frame, text= "Active",
                                  variable=app.mem_var, onvalue="True", offvalue="False")                                  
    app.mem_check.grid(row=0, column=0)

    # Update entries
    app.press_key_entry.delete(0, 5)
    app.press_key_entry.insert(0, options['presskey_timer'])
    app.release_key_entry.delete(0, 5)
    app.release_key_entry.insert(0, options['releasekey_timer'])
    app.process_key_entry.delete(0, 30)
    app.process_key_entry.insert(0, options['process'])
    app.dosbase_key_entry.delete(0, 12)
    app.dosbase_key_entry.insert(0, options['db_base_addr'])
    app.offset_key_entry.delete(0, 12)
    app.offset_key_entry.insert(0, options['offset'])

    # Update gear values
    app.first_gear_value_entry.delete(0, 12)
    app.first_gear_value_entry.insert(0, options['first_value'])
    app.second_gear_value_entry.delete(0, 12)
    app.second_gear_value_entry.insert(0, options['second_value'])
    app.third_gear_value_entry.delete(0, 12)
    app.third_gear_value_entry.insert(0, options['third_value'])
    app.fourth_gear_value_entry.delete(0, 12)
    app.fourth_gear_value_entry.insert(0, options['fourth_value']) 
    app.fifth_gear_value_entry.delete(0, 12)
    app.fifth_gear_value_entry.insert(0, options['fifth_value'])
    app.sixth_gear_value_entry.delete(0, 12)
    app.sixth_gear_value_entry.insert(0, options['sixth_value'])
    app.seventh_gear_value_entry.delete(0, 12)
    app.seventh_gear_value_entry.insert(0, options['seventh_value'])
    app.reverse_gear_value_entry.delete(0, 12)
    app.reverse_gear_value_entry.insert(0, options['reverse_value'])
    app.neutral_gear_value_entry.delete(0, 12)
    app.neutral_gear_value_entry.insert(0, options['neutral_value'])


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


# Run anyshift joystick loop                       
def run_any():   

    # Read the actual configuration displayed
    read_options_from_windows()
    
    # Update button text
    app.run_button.config(text="Anyshift running. Press 'End' to stop")
    app.update()    

    if options['mem_mode'] == 'True':
        # Open DosBox process and check for process opened
        rwm = ReadWriteMemory()
        try:
            process = rwm.get_process_by_name(options['process'])
            process.open()        
        except:
            error_window = Toplevel(app)        
            error_window.title("Error")
            error_window.config(width=200, height=50)
            error_frame = Frame(error_window)
            error_frame.pack()
            error_label = Label(error_frame, text = "Process not found. Open it before Anyshift")
            error_label.grid(row = 0, column = 0)
            app.run_button.config(text="Run Anyshift")
            return
        joystick_loop_mem(options)
        app.run_button.config(text="Run Anyshift")  # Return button to normal text
    else:
        joystick_loop_keys(options)
        app.run_button.config(text="Run Anyshift")  # Return button to normal text   
   

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

        self.seven_var = StringVar(value = options['seven_gears'])
        self.seven_check = Checkbutton(self.options_selection_frame, text= "Use seventh gear",
                                        variable=self.seven_var, onvalue="True", offvalue="False")
        self.seven_check.grid(row=1, column=0)

        self.rev_bool = StringVar(value = options['rev_button'])
        self.rev_check = Checkbutton(self.options_selection_frame, text= "Reverse is a button",
                                        variable=self.rev_bool, onvalue="True", offvalue="False")
        self.rev_check.grid(row=0, column=1)

        self.nascar = StringVar(value = options['nascar_mode'])
        self.nascar_check = Checkbutton(self.options_selection_frame, text= "Nascar mode",
                                        variable=self.nascar, onvalue="True", offvalue="False")
        self.nascar_check.grid(row=1, column=1)

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