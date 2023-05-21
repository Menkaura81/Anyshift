"""Config app. This will write an .ini file with the desired config of AnyShift"""

import os  # Removal of pygame message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # Joystick support
import configparser  # Read and write ini files
import time  # Delays
from sys import exit  # Finish execution in some cases
import csv


def main():

    # Define console windows size (rows, lines)
    #os.system("mode con cols=70 lines=13") NOT WORKING RIGHT NOW

    # Initialize joystick module
    pygame.joystick.init()

    # Joystick id selection
    joy = joystick_selection()

    # Joystick buttons for gears selection
    gears = gears_selection(joy)
    first_gear = gears[0]
    second_gear = gears[1]
    third_gear = gears[2]
    fourth_gear = gears[3]
    fifth_gear = gears[4]
    sixth_gear = gears[5]

    # Options for use seven gears and save selection
    seventh_gear = 88 # random value so it doesn´t conflict with other settings if not configured 
    seven_gears = configure_seven()
    if seven_gears == True:
        seventh_gear, gears = seventh_selection(joy, gears)

    # Remaining reverse gear selection
    reverse = reverse_selection(joy, gears)

    # Ask for game preset load
    presets(joy, first_gear, second_gear, third_gear, fourth_gear, fifth_gear, sixth_gear, seventh_gear, reverse)

    # Key wanted to be pressed for shifts selection
    keys = keys_selection()
    upshift = keys[0]
    downshift = keys[1]
    neut_key = keys[2]

    # Reverse press a key option
    rev_bool, rev_key = reverse_is_button(keys)

    # Neutral position in shifter detection option
    neutral = neutral_detection()

    # Save all config into the .ini file
    save_configuration(joy, first_gear, second_gear, third_gear, fourth_gear, fifth_gear, sixth_gear, seven_gears, seventh_gear,
                       reverse, rev_bool, rev_key, upshift, downshift, neut_key, neutral)


def joystick_selection():

    # Number of joystick connected to the pc
    num_joy = pygame.joystick.get_count()
    if num_joy == 0:
        print("No joysticks connected to the pc")
        print("Please connect joystick and then run the config util again")
        time.sleep(5)
        exit(1)
    else:
        print(f"There are {num_joy} joysticks conected to the pc")

    # Print every joystick and its id
    for i in range(num_joy):
        joy = pygame.joystick.Joystick(i)
        print(f"Joystick {i}: ", joy.get_name())
        joy.quit()

    # Promp user for desired joystick
    joy = '111'
    while len(joy) != 1 or (ord(joy) < 48 or ord(joy) > 57) or int(joy) > (num_joy -1):
        joy = input("Wich joystick do you want to use as shifter?: ")
    joy = int(joy)

    return joy


def gears_selection(joy):

    gears = []  # For storing already used buttons

    # Initialize selected joystick
    shifter = pygame.joystick.Joystick(int(joy))
    shifter.init()

    num_buttons = shifter.get_numbuttons()  # For the range of the loop when selecting buttons

    # Selection for first gear
    os.system('cls')
    print("Put the shifter in position for first gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        gears.append(i)
                        print(f"Button {i} saved for first gear")
                        done = True

    # Selection for second gear
    print("Put the shifter in position for second gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            gears.append(i)
                            print(f"Button {i} saved for second gear")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for second gear")
                            break

    # Selection for third gear
    print("Put the shifter in position for third gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            gears.append(i)
                            print(f"Button {i} saved for third gear")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for third gear")
                            break

    # Selection for fourth gear
    print("Put the shifter in position for fourth gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            gears.append(i)
                            print(f"Button {i} saved for fourth gear")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for fourth gear")
                            break

    # Selection for fifth gear
    print("Put the shifter in position for fifth gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            gears.append(i)
                            print(f"Button {i} saved for fifth gear")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for fifth gear")
                            break

    # Selection for sixth gear
    print("Put the shifter in position for sixth gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            gears.append(i)
                            print(f"Button {i} saved for sixth gear")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for sixth gear")
                            break
    shifter.quit()
    return gears


def configure_seven():

    # Selection for seventh gear
    seven_gears = ''
    while seven_gears != 'n' and seven_gears != 'no' and seven_gears != 'y' and seven_gears != 'yes':
        seven_gears = input("Does the selected joystick has seven gears?. Do you want to use it? (y/n): ")
        seven_gears = seven_gears.lower()
    if seven_gears == 'y' or seven_gears == 'yes':
        seven_gears = True
    else:
        seven_gears = False

    return seven_gears


def seventh_selection(joy, gears):

    # Initialize selected joystick
    shifter = pygame.joystick.Joystick(int(joy))
    shifter.init()

    num_buttons = shifter.get_numbuttons()  # For the range of the loop when selecting buttons

    print("Put the shifter in position for seventh gear")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            seventh_gear = i
                            gears.append(i)
                            print(f"Button {seventh_gear} saved for seventh gear")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for seventh gear")
                            break
    time.sleep(2)
    shifter.quit()
    return seventh_gear, gears


def reverse_selection(joy, gears):

    # Initialize selected joystick
    shifter = pygame.joystick.Joystick(int(joy))
    shifter.init()

    num_buttons = shifter.get_numbuttons()  # For the range of the loop when selecting buttons

    # Selection for reverse
    print("Put the shifter in position for reverse")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        if i not in gears:
                            reverse = i
                            print(f"Button {reverse} saved for reverse")
                            done = True
                        else:
                            print(f"Conflict detected button already in use: {gears}")
                            print("Put the shifter in position for reverse")
                            break
    shifter.quit()
    time.sleep(1)
    return reverse


def presets(joy, first_gear, second_gear, third_gear, fourth_gear, fifth_gear, sixth_gear, seventh_gear, reverse):
    
    os.system('cls')
    preset = ''
    while preset != 'n' and preset != 'no' and preset != 'y' and preset != 'yes':
        preset = input("Do you want to load a saved game preset? (y/n): ")
        preset = preset.lower()
    if preset == 'y' or preset == 'yes':
        # Load csv in a list of dictionaries
        with open("presets.csv", "r") as file:
            reader = csv.DictReader(file)
            juegos = []
            counter = 0
            for row in reader:  # Load csv in a list of dictionaries
                print(row['id'], row['name'])
                juegos.append(row)
                counter += 1
        
            id = -1
            while int(id) < 0 or int(id) > counter:
                id = input("What profile do you want to load?: ")

            # Load variables from dictionary
            upshift = hex_convert(juegos[int(id)]['upshift'])  # Read and converted to hex
            downshift = hex_convert(juegos[int(id)]['downshift'])
            rev_key = hex_convert(juegos[int(id)]['reverse'])
            neut_key = juegos[int(id)]['neutral key']
            seven_gears = juegos[int(id)]['seven gears']
            neutral = juegos[int(id)]['neutral detection']
            rev_bool = juegos[int(id)]['reverse is button']
            nascar = juegos[int(id)]['nascar racing mode']
            presskey_timer = juegos[int(id)]['presskey timer']
            releasekey_timer = juegos[int(id)]['releasekey timer']
            mem_mode = juegos[int(id)]['memory write mode']
            db_base_addr = juegos[int(id)]['dosbox base address']
            offset = juegos[int(id)]['offset'] 

        # Create object config
        config = configparser.ConfigParser(allow_no_value=True)

        # Set configuration
        config['SHIFTER'] = {'; This is the id number of the joystick you want to use': None,
                             'Joystick id': joy,
                             '; Joystick buttons for each gear': None,
                             'first gear': first_gear,
                             'second gear': second_gear,
                             'third gear': third_gear,
                             'fourth gear': fourth_gear,
                             'fifth gear': fifth_gear,
                             'sixth gear': sixth_gear,
                             'seventh gear': seventh_gear,
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

        exit(0)
    else:
        return


def keys_selection():

    keys = []

    # Selection for up, down and neutral keys with input security checks
    os.system('cls')
    up = 'F'
    while len(up) != 1 or ((ord(up) < 97 or ord(up) > 122) and (ord(up) < 48 or ord(up) > 57)):
        up = input("Wich key do you want to be pressed for upshifts?: ")
        up = up.lower()
    keys.append(up)

    down = 'R'
    while len(down) != 1 or ((ord(down) < 97 or ord(down) > 122) and (ord(down) < 48 or ord(down) > 57)) or down in keys:
        down = input("Wich key do you want to be pressed for downshifts?: ")
        down = down.lower()
    keys.append(down)

    neut_key = 'F'
    while len(neut_key) != 1 or ((ord(neut_key) < 97 or ord(neut_key) > 122) and (ord(neut_key) < 48 or ord(neut_key) > 57)) or neut_key in keys:
        neut_key = input("Wich key do you want to use for neutral?: ")
        neut_key = neut_key.lower()
    keys.append(neut_key)
    
    # Convert after key selection so the check for selected key already in use works properly
    keys[0] = hex_convert(up)
    keys[1] = hex_convert(down)

    return keys


def reverse_is_button(keys):

    # Reverse configuration
    os.system('cls')
    rev_bool = ''
    while rev_bool != 'n' and rev_bool != 'no' and rev_bool != 'y' and rev_bool != 'yes':
        print("Some games do not have a reverse gear, instead is a button press")
        rev_bool = input("Do you want reverse position to press a key? (y/n): ")
        rev_bool = rev_bool.lower()
    if rev_bool == 'y' or rev_bool == 'yes':
        rev_bool = True
    else:
        rev_bool = False

    rev = 'null'
    if rev_bool == True:
        while len(rev) != 1 or ((ord(rev) < 97 or ord(rev) > 122) and (ord(rev) < 48 or ord(rev) > 57)) or rev in keys:
            rev = input("Wich key do you want to be pressed for reverse?: ")
            rev = rev.lower()
    rev = hex_convert(rev)

    return rev_bool, rev


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


def neutral_detection():

    # Neutral detection configuration
    neutral = ''
    while neutral != 'n' and neutral != 'no' and neutral != 'y' and neutral != 'yes':
        neutral = input("Do you want to detect neutral position? (y/n): ")
        neutral = neutral.lower()
    if neutral == 'y' or neutral == 'yes':
        neutral = True
    else:
        neutral = False
    return neutral


def save_configuration(joy, first_gear, second_gear, third_gear, fourth_gear, fifth_gear, sixth_gear, seven_gears, seventh_gear,
                       reverse, rev_bool, rev_key, upshift, downshift, neut_key, neutral):

    # Create object config
    config = configparser.ConfigParser(allow_no_value=True)

    # Set configuration
    config['SHIFTER'] = {'; This is the id number of the joystick you want to use': None,
                          'Joystick id': joy,
                          '; Joystick buttons for each gear': None,
                          'first gear': first_gear,
                          'second gear': second_gear,
                          'third gear': third_gear,
                          'fourth gear': fourth_gear,
                          'fifth gear': fifth_gear,
                          'sixth gear': sixth_gear,
                          'seventh gear': seventh_gear,
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
                         'nascar racing mode': False,
                         '; Instead of key presses it writes data to memory. I only included it because of Grand Prix 2': None,
                         '; Each game has different memory values. No offical support for this one': None,
                         'memory write mode': False,
                         '; DosBox version base address. Ex: 0.74 = 0x01D3A1A0 ': None,
                         'DosBox Version base address': 0,
                         '; Memory value offset from base addres ': None,
                         'Memory value offset': 0,
                         '; Delays for key presses and releases. Tinker with this if game doesnt detect key presses': None,
                         'presskey timer': 0.1,
                         'releasekey timer': 0.3,
                        } 

    # Write the file
    with open("Anyshift.ini", "w") as configfile:
        config.write(configfile)


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()