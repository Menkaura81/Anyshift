"""Config app. This will write an .ini file with the desired config of AnyShift"""
import pygame
import configparser

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

# Initialize joystick module
pygame.joystick.init()
pygame.init()  

# Number of joystick connected to the pc
num_joy = pygame.joystick.get_count()
print(f"There are {num_joy} joysticks conected to the pc")

# Print every joystick and its id
for i in range(num_joy):
    joy = pygame.joystick.Joystick(i)
    print(f"Joystick {i}: ", joy.get_name())
    joy.quit()

# Promp user for desired joystick
joy = '111'
while len(joy) != 1 or (ord(joy) < 48 or ord(joy) > 57) or int(joy) > num_joy:
     joy = input("Wich joystick do you want to use as shifter?: ")
joy = int(joy)

# Initialize selected joystick
shifter = pygame.joystick.Joystick(int(joy))
shifter.init()

num_buttons = shifter.get_numbuttons()  # For the range of the loop when selecting buttons

# Selection for first gear
print("Put the shifter in position for first gear")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        first_gear = i
                        print(f"Button {first_gear} saved for first gear")
                        done = True

# Selection for second gear
print("Put the shifter in position for second gear")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        second_gear = i
                        print(f"Button {second_gear} saved for second gear")
                        done = True

# Selection for third gear
print("Put the shifter in position for third gear")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        third_gear = i
                        print(f"Button {third_gear} saved for third gear")
                        done = True

# Selection for fourth gear
print("Put the shifter in position for fourth gear")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        fourth_gear = i
                        print(f"Button {fourth_gear} saved for fourth gear")
                        done = True

# Selection for fifth gear
print("Put the shifter in position for fifth gear")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        fifth_gear = i
                        print(f"Button {fifth_gear} saved for fifth gear")
                        done = True  

# Selection for sixth gear
print("Put the shifter in position for sixth gear")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        sixth_gear = i
                        print(f"Button {sixth_gear} saved for sixth gear")
                        done = True

# Selection for seventh gear
seven_gears = ''
while seven_gears != 'n' and seven_gears != 'no' and seven_gears != 'y' and seven_gears != 'yes':
    seven_gears = input("Does the selected joystick has seven gears? (y/n): ")
    seven_gears = seven_gears.lower()
if seven_gears == 'y' or seven_gears == 'yes':
    print("Put the shifter in position for seventh gear")
    seven_gears = True
    done = False
    while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        seventh_gear = i
                        print(f"Button {seventh_gear} saved for sixth gear")
                        done = True
else:
    seven_gears = False                        

# Selection for reverse
print("Put the shifter in position for reverse")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        reverse = i
                        print(f"Button {reverse} saved for reverse")
                        done = True                                                                      

# Selection for up, down and neutral keys with input security checks
up = 'F'
while len(up) != 1 or ((ord(up) < 97 or ord(up) > 122) and (ord(up) < 48 or ord(up) > 57)):
    up = input("Wich key do you want to be pressed for upshifts?: ")
    up = up.lower()
down = 'R'
while len(down) != 1 or ((ord(down) < 97 or ord(down) > 122) and (ord(down) < 48 or ord(down) > 57)) or down == up:
    down = input("Wich key do you want to be pressed for downshifts?: ")
    down = down.lower()    
neut_key = 'F'
while len(neut_key) != 1 or ((ord(neut_key) < 97 or ord(neut_key) > 122) and (ord(neut_key) < 48 or ord(neut_key) > 57)) or neut_key == up or neut_key == down:
    neut_key = input("Wich key do you want to use for neutral?: ")
    neut_key = neut_key.lower()

# Convert input keys to hex values
if up in keys:
    upshift = keys[up]
if down in keys:
    downshift = keys[down]

# Neutral detection configuration
neutral = ''
while neutral != 'n' and neutral != 'no' and neutral != 'y' and neutral != 'yes':
    neutral = input("Do you want to detect neutral position? (y/n): ")
    neutral = neutral.lower()
if neutral == 'y' or neutral == 'yes':
    neutral = True
else:
    neutral = False

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