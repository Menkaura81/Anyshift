# Anyshift
## A python app to convert joystick inputs into key strokes so you can play vintage driving games with a H-Shifter

Anyshift is a software written in Python. It uses pygame joystick module to read inputs from the selected device, applies the shifter to sequential logic changes and send keyboard presses so you can use your H-Shifter with your favorite old racing game.

if you enjoy this app, you can buy me a coffee to keep me awake coding cool apps: https://www.buymeacoffee.com/Menkaura

### How to use AnyShift

You can uncompress Anyshift in any directory you want. Included in the zip comes an ini file that can be edited manually but it is preferable that you run 'Anyshift_config.exe' so you know exactly wich id has your shifter assigned. You can choose wich joystick is used to select gears, wich keys are pressed for upshift and downshift, and if you want the gear to be neutral if there is no gear selected in the shifter (this won´t work in old games, but i included the option, just in case). 

First of all you have to configure the game keys for upshift and downshift. Then you have to run Anyshift_config.exe to configure button imputs from your shifter. Then choose the same keys in anyshift than you did in the game. There are more options to choose depending on the game you want to use anyshift with. We´ll cover them later.

Two video examples of Anyshift running:

Gran Turismo 4:
https://www.youtube.com/watch?v=ijPjmBfR4QU

Nascar Racing:
https://www.youtube.com/watch?v=WRI1p6f5Af8

### Setups for games

GRAN TURISMO 4 pcsx2

Tested with pcsx2 1.6.0 and NTSC american version of the game (supports native 1080 resolution and 60 fps). Support force feedback, 900º wheel rotation and independent pedals.
You have to set your keys in the gamepad control setup of the emulator:
    L2 = Downshift (Default key s)
    R2 = Upshift (Default key z)
    Triangle = reverse key (Default key c)
Select manual shifting ingame.
On the rolling starts you have to select the right position on the shifter before crossing start line to avoid desynchronization.
Neutral not detected and reverse is a button.

ENTHUSIA pcsx2

Tested with pcsx2 1.6.0 and PAL version of the game. Support force feedback, 900º wheel rotation and independent pedals. 
You have to set your keys in the gamepad control setup of the emulator:
    L2 = Downshift (Default key s)
    R2 = Upshift (Default key z)
Select manual shifting ingame. 
You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a gear.

GRAN TURISMO duckstation

Tested with duckstation and PAL version of the game. Doesn´t support force feedback. You need negcon controller settings to use steering wheel. Pedals must be combined.
Recomended wheel rotation degrees 720º
You have to set your keys in the neGcon control setup of the emulator:
    DPad Right = Upshift (Default key s)
    DPad Lef = Downshift (Default key z)
    B = Reverse (Default key c)
Select manual shifting ingame. 
You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Neutral not detected and reverse is a button.

NASCAR RACING DosBox

Tested with dosbox 0.74-3. Doesn´t support force feedback and you must set combined pedals mode in your wheel config app. 
Recomended wheel rotation degrees 400º. 
You can choose controls ingame. Default keys are:
    S = Upshift
    Z = Downshift
    C = Reverse
You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a button and Nascar Mode required to work properly. 
Game glitches a bit if you leave a gear selected in the menus. 

NASCAR RACING 2 DosBox

Tested with dosbox 0.74-3. Doesn´t support force feedback and you must set combine pedals mode in your wheel config app. 
You can choose controls ingame. Default keys are:
    A = Upshift
    Z = Downshift
    C = Reverse
You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a button and Nascar Mode required to work properly. 
Use S key to display gears hud. 

GRAND PRIX 2 DosBox

Tested with dosbox 0.74-3. Doesn´t support force feedback and you must set combine pedals mode in your wheel config app.
Controls are forced ingame:
    SPACE = Upshift (0x39)
    ALT = Downshift (0x38)
Neutral detected and reverse is a gear. Memory write mode True. Seven gear is used for the "spin" gearbox position.
Not compatible with key presses mode. Added the option of write to memory gear values. Still not fully functional. 
Memory option not supported for more games, i added it only because this is the game of my childhood, the one got me hooked with simracing.

COLIN MCRAE RALLY pc

Tested with base game on Windows 11. Support force feedback and independent pedals. 
Recomended wheel rotation degrees 540º. 
Change controls ingame. Default keys in given profile:
    S = Upshift
    Z = Downshift
Select manual shifting ingame. 
Select first gear just after the start countdown finnish otherwise game will glitch and select reverse. 
Neutral detected and reverse is a gear. 

INDIANAPOLIS 500

Tested with model 2 emu. Support force feedback and independent pedals. 
Recomended wheel rotation degrees 400º. 
Configure controls in the emulator. 
    Button 2 = Downshift (Default s)
    Button 3 = Upshift (Default z)
Select right position on the shifter before you gain control on the car to avoid desynchronization. 
Neutral not detected and no reverse gear. 


### References 

https://stackoverflow.com/questions/6620637/writing-comments-to-files-with-configparser  -- Comments in configparser
https://linuxhint.com/string-to-hexadecimal-in-python/ -- To convert strings to hex
https://www.scaler.com/topics/how-to-clear-screen-in-python/ -- Clear console command
https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/  -- Send key strokes to games using ctypes
https://www.pygame.org/docs/ref/joystick.html -- Pygame joystick library 


