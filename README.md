# Anyshift
## A python app to convert joystick inputs into key strokes so you can play vintage driving games with a H-Shifter

Anyshift is a software written in Python. It uses pygame joystick module to read inputs from the selected device, applies the shifter to sequential logic changes and send keyboard presses so you can use your H-Shifter with your favorite old racing game.

if you enjoy this app, you can buy me a coffee to keep me awake coding cool apps: https://www.buymeacoffee.com/Menkaura

### How to use AnyShift

You can uncompress Anyshift in any directory you want. Run Anyshift.exe and load a preset or create your own. Then click on Run Anyshift and it will start working. While Anyshift is active, config windows will be freezed (only this window, rest of your system will work ok), you can stop anyshift and back to config window by pressing "End" key.

Anyshift works in two modes:
    1 Simulated key pressed mode
    2 Memory write mode

In MEMORY WRITE MODE, values for gears are written directly to memory when you select a gear in the shifter. In this mode is impossible that Anyshift desynchronize with the game, but as every version of an emulator use distinct base memory addresses, and every game manages memory at his own way, this mode is only supported in DOSBox 0.74 (not 0.74-2 or 0.74-3) and with the listed games in the presets csv. You can find offsets for another games and if the game works like any of the supported games your offset will work, but i can´t support changes in code for the vast amount of games created for PC. I hope you undestand. As Anyshift is open source, you can try to make your game work changing the code. I encourage you to do it, and please share your results in the repository.

In SIMULATED KEY PRESSED MODE, you can choose wich joystick is used to select gears and wich keys are pressed for upshift, downshift and reverse. Anyshift can desynchronize with the game some times, but you can use the keyboard keys to resync. In this mode you have to configure the game keys for upshift and downshift. Then you have to run Anyshift_config.exe to configure button imputs from your shifter. Then choose the same keys in anyshift than you did in the game. There are more options to choose depending on the game you want to use anyshift with. We´ll cover them later.

Two video examples of Anyshift running:

Gran Turismo 4:
https://www.youtube.com/watch?v=ijPjmBfR4QU

Nascar Racing:
https://www.youtube.com/watch?v=WRI1p6f5Af8

### Options explained

If you take a look at anyshift.ini you can see a lot of options. Let´s explain them

First section [SHIFTER] is simple. Here you can find the windows id for the selected shifter and the number of the shifter button for each gear.

In [KEYS] you will find the hex values for the keys you selected in anyshift_config. Neutral key is in character, because this key is used in a way that doesn´t need hex code to work

And now the interesting part... [OPTIONS]. Let´s take a look at each option:

    - seven gears: This value is True if the shifter has seven gears positions
    - neutral detection: Is true if the game detects neutral position and can disengage gears (ex: Grand Prix 2 or Colin McRae Rally 2)
    - reverse is button: True if the game uses an idependent button for reverse (ex: Gran Turismo or Nascar Racing)
    - nascar racing mode: True to make anyshift follow old Papyrus games (no neutral and the game remember the gear you where in when you push reverse button)
    - memory write mode: True to change to memory write mode
    - dosbox version base address: The value of the base address of DOSBox
    - memory value offset: The ofset of the memory address for gears in the game from the base address of DOSBox
    - presskey timer: Value of the delay when pressing a key
    - releasekey timer: Same for release the key. Change this value if game doesn´t detect the simulated key presses

### Setups for games

GRAN TURISMO 4 pcsx2

Tested with pcsx2 1.6.0 and NTSC american version of the game (supports native 1080 resolution and 60 fps). Support force feedback, 900º wheel rotation and independent pedals.
You have to set your keys in the gamepad control setup of the emulator:

    - L2 = Downshift (Default key s)
    - R2 = Upshift (Default key z)
    - Triangle = reverse key (Default key c)

Select manual shifting ingame.
On the rolling starts you have to select the right position on the shifter before crossing start line to avoid desynchronization.
Neutral not detected and reverse is a button.

ENTHUSIA pcsx2

Tested with pcsx2 1.6.0 and PAL version of the game. Support force feedback, 900º wheel rotation and independent pedals. 
You have to set your keys in the gamepad control setup of the emulator:

    - L2 = Downshift (Default key s)
    - R2 = Upshift (Default key z)

Select manual shifting ingame. 
You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a gear.

GRAN TURISMO duckstation

Tested with duckstation and PAL version of the game. Doesn´t support force feedback. You need negcon controller settings to use steering wheel. Pedals must be combined.
Recomended wheel rotation degrees 720º
You have to set your keys in the neGcon control setup of the emulator:

    - DPad Right = Upshift (Default key s)
    - DPad Lef = Downshift (Default key z)
    - B = Reverse (Default key c)

Select manual shifting ingame. 
You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Neutral not detected and reverse is a button.

NASCAR RACING DosBox

Tested with dosbox 0.74-3. Doesn´t support force feedback and you must set combined pedals mode in your wheel config app. 
Recomended wheel rotation degrees 400º. 
You can choose controls ingame. Default keys are:

    - S = Upshift
    - Z = Downshift
    - C = Reverse

You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a button and Nascar Mode required to work properly. 
Game glitches a bit if you leave a gear selected in the menus. 

NASCAR RACING 2 DosBox

Tested with dosbox 0.74-3. Doesn´t support force feedback and you must set combine pedals mode in your wheel config app. 
You can choose controls ingame. Default keys are:
    
    - A = Upshift
    - Z = Downshift
    - C = Reverse

You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a button and Nascar Mode required to work properly. 
Use S key to display gears hud. 

INDYCAR RACING DosBox

Tested with dosbox 0.74-3. Doesn´t support force feedback and you must set combine pedals mode in your wheel config app. 
You can choose controls ingame. Default keys are:
    
    - A = Upshift
    - Z = Downshift
    - T = Reverse

You have to select the right position on the shifter (first gear) before going to track to avoid desynchronization. 
Reverse is a button and Nascar Mode required to work properly. 

GRAND PRIX 2 DosBox

Only works in practice mode. In race mode, DOSBox crash
Only works with Dosbox 0.74. Doesn´t support force feedback and you must set combine pedals mode in your wheel config app.
Only works in memory write mode, not compatible with key presses mode.

    - DosBox 0.74 base address = 0x01D3A1A0
    - Memory offset for gears = 0x291BF0

Neutral detected and reverse is a gear. Memory write mode True. Seven gear is used for the "spin" gearbox position. 
Memory option is not supported, i added it only because GP2 is the game of my childhood, the one got me hooked with simracing.

COLIN MCRAE RALLY pc

Tested with base game on Windows 11. Support force feedback and independent pedals. 
Recomended wheel rotation degrees 540º. 
Change controls ingame. Default keys in given profile:

    - S = Upshift
    - Z = Downshift

Select manual shifting ingame. 
Select first gear just after the start countdown finnish otherwise game will glitch and select reverse. 
Neutral detected and reverse is a gear. 

INDIANAPOLIS 500

Tested with model 2 emu. Support force feedback and independent pedals. 
Recomended wheel rotation degrees 400º. 
Configure controls in the emulator. 
    
    - Button 2 = Downshift (Default s)
    - Button 3 = Upshift (Default z)

Select right position on the shifter before you gain control on the car to avoid desynchronization. 
Neutral not detected and no reverse gear. 

### References 

- https://stackoverflow.com/questions/6620637/writing-comments-to-files-with-configparser  -- Comments in configparser
- https://linuxhint.com/string-to-hexadecimal-in-python/ -- To convert strings to hex
- https://www.scaler.com/topics/how-to-clear-screen-in-python/ -- Clear console command
- https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/  -- Send key strokes to games using ctypes
- https://www.pygame.org/docs/ref/joystick.html -- Pygame joystick library 
- https://stackoverflow.com/questions/63442491/get-data-at-address-from-cheat-engine-with-python  -- Get data address from cheat engine
- https://pypi.org/project/ReadWriteMemory/  - Read and write memory