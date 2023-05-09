"""Config app. This will write an .ini file with the desired config of AnyShift"""
import pygame
import configparser

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
joy = int(input("Wich joystick do you want to use as shifter?: "))

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
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

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
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

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
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

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
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

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
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

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
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        sixth_gear = i
                        print(f"Button {sixth_gear} saved for sixth gear")
                        done = True

# Selection for reverse
print("Put the shifter in position for reverse")
done = False
while not done:
        # Event processing step.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

            if event.type == pygame.JOYBUTTONDOWN:
                for i in range(num_buttons):
                    if shifter.get_button(i) == True:
                        reverse = i
                        print(f"Button {reverse} saved for reverse")
                        done = True                                                                      

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
                   'first gear': first_gear,
                   'second gear': second_gear,
                   'third gear': third_gear,
                   'fourth gear': fourth_gear,
                   'fifth gear': fifth_gear,
                   'sixth gear': sixth_gear,
                   'reverse button': reverse,
                   'neutral position': neutral}

config['KEYS'] = {'upshift': upshift,
                'downshift': downshift}

# Write the file
with open("Anyshift.ini", "w") as configfile:
    config.write(configfile)