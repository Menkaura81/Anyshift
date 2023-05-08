"""Config app. This will write an .ini file with the desired config of AnyShift"""
import pygame
import configparser

# Initialize joystick module
pygame.joystick.init()

# Number of joystick connected to the pc
num_joy = pygame.joystick.get_count()
print(f"There are {num_joy} joysticks conected to the pc")

# Print every joystick and its id
for i in range(num_joy):
    joy = pygame.joystick.Joystick(i)
    print(f"Joystick {i}: ", joy.get_name())
    joy.quit()

# Promp user for desired config
joy = int(input("Wich joystick do you want to use as shifter?: "))
upshift = input("Wich key do you want to be pressed for upshifts?: ")
downshift = input("Wich key do you want to be pressed for downshifts?: ")

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
                   'Neutral position': neutral}

config['KEYS'] = {'Upshift': upshift,
                'Downshift': downshift}

# Write the file
with open("Anyshift.ini", "w") as configfile:
    config.write(configfile)