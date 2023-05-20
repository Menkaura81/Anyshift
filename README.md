# Anyshift
## A python app to convert joystick inputs into key strokes so you can play vintage driving games with a H-Shifter

Anyshift is a software written in Python. It uses pygame (https://www.pygame.org/news) joystick  module to read inputs from the selected device, applies the shiter to sequential logic changes and send keyboard presses so you can use your H-Shifter with your favorite old racing game.

### How to use AnyShift

First of all you have to configure the game keys for upshift and downshift. Then you have to run Anyshift_config.exe to configure button imputs from your shifter. Then choose the same keys in anyshift than you did in the game. There are more options to choose depending on the game you want to use anyshift with. We´ll cover the later.

You can uncompress Anyshift in any directory you want. Included in the .rar comes an ini file that can be edited manually but it is preferable that you run 'config.exe' so you know exactly wich id has your shifter assigned. You can choose wich joystick is used to select gears, wich keys are pressed for upshift and downshift, and if you want the gear to be neutral if there is no gear selected in the shifter (this won´t work in old games, but i included the option, just in case) 


###Setups for games

GRAN TURISMO 4 pcsx2

900 degrees

ENTHUSIA pcsx2

NASCAR RACING DosBox

Combined pedals mode

NASCAR RACING 2 DosBox

Combined pedal mode

### References 

https://stackoverflow.com/questions/6620637/writing-comments-to-files-with-configparser  -- Managing comments in configparser
https://linuxhint.com/string-to-hexadecimal-in-python/ -- To convert strings to hex
https://www.scaler.com/topics/how-to-clear-screen-in-python/ -- Clear console command
https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/  -- Send key strokes to games using ctypes
https://www.pygame.org/docs/ref/joystick.html -- Pygame joystick library 


