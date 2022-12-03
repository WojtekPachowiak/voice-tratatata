from typing import Literal
from pydantic import BaseModel
import pyaudio
import wave
import sys

CHUNK = 1024


{"a-z": "path/to/audiofile"}

class LetterPhoneMapping:
    def __init__(self, letter_specific_options: dict, global_options: dict) -> None:
        self.spec_map = letter_specific_options
        self.global_map = global_options

        self.__load_sounds()
        self.__apply_global_to_spec()

    def __apply_global_to_spec(self):
        'applies global options to every sound file in letter-specific options'
        #audio processing (pitch shift, reverb, delay...)
        pass

    def __load_sounds(self):
        'loads the sound files whose paths are listed in specific options'



class GlobalOptions(BaseModel):
    pitch : Literal["uniform","variable"]
    effects: 

class Pitch(BaseModel):


class CharacterSpecificOptions:
    pass


class MachineGun:
    def __init__(self, letter_phone_mapping: LetterPhoneMapping) -> None:
        pass
    


    def speak(self, text:str):
        'loop over characters contained in a given text'
        for letter in text:
            if letter == ...

    def __parse_char(self,char: str):
        'parse options associated with a given character and, after that, play a sound associated with the character'
        self.__play_sound()
        pass
    
    def __play_sound(self, char: str):
        'play a sound associated with a character'
        wf = wave.open(sys.argv[1], 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data):
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
        


