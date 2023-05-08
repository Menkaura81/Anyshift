"""Main Anyshift executable"""
import pygame
import keyboard
import configparser

up_key = 's'
down_key = 'z'

def main():

    # Create a config objet and read config values
    config = configparser.ConfigParser()
    config.read('Anyshift.ini')
    neutral = config['SHIFTER']['neutral position']
    joy_id = config['SHIFTER']['joystick id']
    global up_key
    up_key = config['KEYS']['upshift']
    global down_key 
    down_key = config['KEYS']['downshift']
    
    # Initialize joystick module
    pygame.joystick.init()
    pygame.init()   
        
    # Create a joystick object and initialize it
    shifter = pygame.joystick.Joystick(int(joy_id))
    shifter.init()

    # Cool window design ;)    
    print("    ___                _____ __    _ ______              ___  ____  ")
    print("   /   |  ____  __  __/ ___// /_  (_) __/ /_   _   __   <  / / __ \ ")
    print("  / /| | / __ \/ / / /\__ \/ __ \/ / /_/ __/  | | / /   / / / / / / ")
    print(" / ___ |/ / / / /_/ /___/ / / / / / __/ /_    | |/ /   / /_/ /_/ /  ")
    print("/_/  |_/_/ /_/\__, //____/_/ /_/_/_/  \__/    |___/   /_/(_)____/   ")
    print("             /____/                            ©2022 Menkaura Soft  ")    
    print()
    print("Active shifter: ",shifter.get_name())

    gear_selected = 0
    actual_gear = 0
    #neutral = False  # This will be readed from ini to deactivate neutral position or not

    done = False
    while not done:
            # Event processing step.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  # Flag that we are done so we exit this loop.

                if event.type == pygame.JOYBUTTONDOWN:
                    #print("Joystick button pressed.")
                    if shifter.get_button(0) == True:
                        gear_selected = 1
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(1) == True:
                        gear_selected = 2
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(2) == True:
                        gear_selected = 3
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(3) == True:
                        gear_selected = 4
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(4) == True:
                        gear_selected = 5
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(5) == True:
                        gear_selected = 6
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(6) == True:
                        gear_selected = 7
                        actual_gear = update_gear(gear_selected, actual_gear)
                    if shifter.get_button(7) == True: 
                        gear_selected = -1
                        actual_gear = update_gear(gear_selected, actual_gear)        
                    print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")            

                if event.type == pygame.JOYBUTTONUP:
                    if neutral == True:
                        #print("Joystick button released.")
                        gear_selected = 0
                        actual_gear = update_gear(gear_selected)
                        print(f"Gear in joystick: {gear_selected} -- Actual gear: {actual_gear}   ",  end="\r")


def update_gear(gear_selected, actual_gear):

    act_gear = actual_gear
    while act_gear != gear_selected:
        if act_gear < gear_selected:
            act_gear += 1
            #aqui iria la simulacion de pulsacion de tecla
            keyboard.press_and_release(up_key)
        if act_gear > gear_selected:
            act_gear -= 1
            #simulacion de pulsacion de tecla
            keyboard.press_and_release(down_key)
    
    return act_gear


if __name__ == "__main__":
    main()
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()