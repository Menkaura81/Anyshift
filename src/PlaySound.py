################################################################################################
# PlaySound module provides all the sound playing logic to Anyshift software
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
################################################################################################
 
import random  # Randomize sound files
import os  # Path for sound files 
import sys # Path for sound files
import pygame

def play_sound():

    # Get path for .wavs location    
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    #wav_path = os.path.join(application_path, config_name)

    number = random.randint(1,3)
    #audio_file = os.path.dirname(__file__) 
    audio_file = application_path + "/Resources/" + str(number) + ".wav"
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(loops=0)
    return