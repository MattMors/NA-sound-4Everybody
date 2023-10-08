from tones import SINE_WAVE, SAWTOOTH_WAVE
from tones.tone import Tone
from tones.mixer import Mixer
from tones.mixer import Track
from tones import *
import random
import time


class AudioGenerator():

    # C = 261.63
    # C_SH = 277.18
    # D = 293.66
    # D_SH = 311.13
    # E = 329.63
    # F = 349.23
    # F_SH = 369.99
    # G = 392.00
    # G_SH = 415.30
    # A = 440.0
    # A_SH = 466.16
    # B = 493.88

    C_SCALE = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    C_SH_SCALE = ['c#', 'd#', 'f', 'f#', 'g#', 'a#', 'c']
    D_SCALE = ['d', 'e', 'f#', 'g', 'a', 'b', 'c#']
    D_SH_SCALE = ['d#', 'f', 'g', 'g#', 'a#', 'c', 'd']
    E_SCALE = ['e', 'f#', 'g#', 'a', 'b', 'c#', 'd#']
    F_SCALE = ['f', 'g', 'a', 'a#', 'c', 'd', 'e']
    F_SH_SCALE = ['f#', 'g#', 'a#', 'b', 'c#', 'd#', 'f']
    G_SCALE = ['g', 'a', 'b', 'c', 'd', 'e', 'f#']
    G_SH_SCALE = ['g#', 'a#', 'c', 'c#', 'd#', 'f', 'g']
    A_SCALE = ['a', 'b', 'c#', 'd', 'e', 'f#', 'g#']
    A_SH_SCALE = ['a#', 'c', 'd', 'd#', 'f', 'g', 'a']
    B_SCALE = ['b', 'c#', 'd#', 'e', 'f#', 'g#', 'a#']

    SCALES = [C_SCALE, C_SH_SCALE, D_SCALE, D_SH_SCALE, E_SCALE, F_SCALE, F_SH_SCALE, G_SCALE, G_SH_SCALE, A_SCALE, A_SH_SCALE, B_SCALE]

    # OCTAVE = 3
    

    # Create mixer, set sample rate and amplitude   
    mixer = Mixer(44100, 1)
    # samples = []


    def generate_melody(self, melody):
        self.mixer.create_track(0, SINE_WAVE, attack=0.5, decay=1.3)
        for elem in range(len(melody)):
            
            # if melody[elem]!=melody[len(melody)-1] and melody[elem]==melody[elem+1]:
            #     decay = 2.4

            # tone = Tone(44100, 1, SINE_WAVE)
            # self.mixer.create_track(elem+1, SINE_WAVE, attack=1, decay=decay)
            # self.mixer.create_track(elem+2, SINE_WAVE, attack=1, decay=decay)

            # Add a 1-second tone on track 0, slide pitch from c# to f#)
            self.mixer.add_note(0, note=melody[elem][random.randint(0,6)], octave=random.randint(3,4), duration=1)
            # self.mixer.add_note(elem+1, note='e', octave=self.OCTAVE, duration=0.1)
            # self.mixer.add_note(elem+2, note='g', octave=self.OCTAVE, duration=0.1)

            # self.mixer.add_samples(trackname = track, samples = self.samples)
            
            # track.append_samples(self.samples)
            # self.mixer.add_samples(elem, samples)

        self.mixer.write_wav('../res/audio/tones.wav')
        # samples = self.mixer.mix()
            
        
        
        # 

# Mix all tracks into a single list of samples scaled from 0.0 to 1.0, and
# return the sample list



        
        # Add a 1-second tone on track 1, slide pitch from f# to g#)
        # mixer.add_note(1, note='f#', octave=5, duration=1.0, endnote='g#')

        # Mix all tracks into a single list of samples and write to .wav file
        # Mix all tracks into a single list of samples scaled from 0.0 to 1.0, and
        # return the sample list