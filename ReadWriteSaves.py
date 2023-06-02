###################################################################################################
# IniParser provides functions for reading and writing ini files for Anyshift software. Also 
# includes hex values for compatible keys
#
# 2023 Menkaura Soft
###################################################################################################

import configparser  # Write and read ini files

def ini_reader():

    options = {}
    # Create a config objet and read config values
    config = configparser.ConfigParser()
    config.read('Anyshift.ini')
    
    # Save values into dictionay
    options['nascar_mode'] = config['OPTIONS']['nascar racing mode']
    options['seven_gears'] = config['OPTIONS']['seven gears']
    options['rev_button'] = config['OPTIONS']['reverse is button']
    options['neutral'] = config['OPTIONS']['neutral detection']
    options['clutch'] = config['OPTIONS']['require clutch']
    options['clutch_id'] = config['SHIFTER']['clutch id']
    options['clutch_axis'] = config['SHIFTER']['clutch axis']
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

    return options


def ini_writer(options, upshift, downshift, rev_key):
    
    # Create object config
    config = configparser.ConfigParser(allow_no_value=True)

    config['SHIFTER'] = {'; This is the id number of the shifter you want to use': None,
                         'Joystick id': options['joy_id'],
                         '; This is the id number of the controller you wanth to use for clutch': None,
                         'clutch id': options['clutch_id'],
                         '; Selected controller axis for the clutch': None,
                         'clutch axis': options['clutch_axis'],
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

    config['KEYS'] = {'; Upshift, downshift, neutral and reverse key': None,
                      'upshift': upshift,
                      'downshift': downshift,
                      'reverse': rev_key,
                      'neutral key': options['neut_key']
                    }

    config['OPTIONS'] = {'; True if you have a shifter with seven gears. Seventh gear button must be configured or anyshift will crash ': None,
                         'seven gears': options['seven_gears'],
                         '; True if you want to change to neutral if no gear is selected in shifter. Most old games doesnt support this': None,
                         'neutral detection': options['neutral'],
                         '; True if clutch is needed to change gears': None,
                         'require clutch': options['clutch'],
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


# Convert keys char into hex code
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


def char_convert(key):

    # Dictionary for converting hex values to char
    keys = {
        '0x02': '1',
        '0x03': '2',
        '0x04': '3',
        '0x05': '4', 
        '0x06': '5',
        '0x07': '6',
        '0x08': '7',
        '0x09': '8',
        '0x0A': '9',
        '0x0B': '0',
        '0x10': 'q',
        '0x11': 'w',
        '0x12': 'e',
        '0x13': 'r',
        '0x14': 't',
        '0x15': 'y',
        '0x16': 'u',
        '0x17': 'i',
        '0x18': 'o',
        '0x19': 'p', 
        '0x1E': 'a', 
        '0x1F': 's',
        '0x20': 'd',
        '0x21': 'f',
        '0x22': 'g',
        '0x23': 'h',
        '0x24': 'j',
        '0x25': 'k',
        '0x26': 'l',
        '0x2C': 'z',
        '0x2D': 'x',
        '0x2E': 'c', 
        '0x2F': 'v', 
        '0x30': 'b',
        '0x31': 'n',
        '0x32': 'm'
    }

    # Convert input keys to hex values. Cheks if the key is in the dictionary and return its hex value
    if key in keys:
        result = keys[key]
    return result