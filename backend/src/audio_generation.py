from tones import SINE_WAVE
from tones.mixer import Mixer
import random

class AudioGenerator():

    # notes frequency
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

    # Create mixer, set sample rate and amplitude   
    mixer = Mixer(44100, 1)

    def generate_melody(self, melody):
        self.mixer.create_track(0, SINE_WAVE, attack=0.5, decay=1.3)
        for elem in range(len(melody)):

            # chords creation
            self.mixer.add_note(0, note=melody[elem][random.randint(0,6)], octave=random.randint(3,4), duration=1)
            # self.mixer.add_note(0, note='e', octave=random.randint(3,4), duration=1)
            # self.mixer.add_note(0, note='g', octave=random.randint(3,4), duration=1)

        self.mixer.write_wav('../res/audio/tones.wav')
        # add more notes or tracks to get chords and more variance