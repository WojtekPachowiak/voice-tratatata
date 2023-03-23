from typing import Literal, Optional
from pydantic import BaseModel
import pyaudio
import wave
import sys
from schema import *

CHUNK = 1024


############################################################################################################

# class LetterToPhoneMap(dict):
#     def __init__(self, global_options: dict = {}) -> None:
#         self.global_map = global_options
#         # self.__load_sounds()
#         self.__apply_global_to_spec()

#     def __apply_global_to_spec(self):
#         'applies global options to every sound file in letter-specific options'
#         #audio processing (pitch shift, reverb, delay...)
#         pass

#     def __load_sounds(self):
#         'loads the sound files whose paths are listed in specific options'
#         assert "wave" not in list(self.spec_map.items())[0][1]
#         for k, v in self.spec_map:
#             v["wave"] = AudioFile(v["path"])
#         assert "wave" in list(self.spec_map.items())[0][1]
        

############################################################################################################

"""
Example of a letter-to-phone map:
{
    "a": "path/to/a/sound/file",
    "b": "path/to/b/sound/file",
    ...,
    "z": "path/to/z/sound/file"
}

Example of an audio processing options:
{
    "speed" : 1.5,
    "pitch" : 2,
    ...
}

Example of specific audio processing options (they override global options):
{
    "b": {
            "speed" : 0.4,
            "pitch" : 3.5,
            ...
        },
    "f": {
            "speed" : 0.2,
            "pitch" : 1.5,
            ...
        },
    ...,
    "z": {
            "speed" : 1.,
            "pitch" : 2.,
            ...
        }
}
"""

default_l2pm = {
    "a": "sounds/a.wav",
    "b": "sounds/b.wav",
    "c": "sounds/c.wav",
    "d": "sounds/d.wav",
    "e": "sounds/e.wav",
    "f": "sounds/f.wav",
    "g": "sounds/g.wav",
    "h": "sounds/h.wav",
    "i": "sounds/i.wav",
    "j": "sounds/j.wav",
    "k": "sounds/k.wav",
    "l": "sounds/l.wav",
    "m": "sounds/m.wav",
    "n": "sounds/n.wav",
    "o": "sounds/o.wav",
    "p": "sounds/p.wav",
    "q": "sounds/q.wav",
    "r": "sounds/r.wav",
    "s": "sounds/s.wav",
    "t": "sounds/t.wav",
    "u": "sounds/u.wav",
    "v": "sounds/v.wav",
    "w": "sounds/w.wav",
    "x": "sounds/x.wav",
    "y": "sounds/y.wav",
    "z": "sounds/z.wav"
}

default_gapm = {
    "speed": 1.,
    "pitch": 1.,
    "reverb": 0.
}

class Tratatata:
    def __init__(self,
                letter_to_phone_map: Optional[dict] = None, 
                global_audio_processing_map: Optional[dict] = None, 
                specific_audio_processing_map: Optional[dict] = None,
                ) -> None:
        """
        Args:
            letter_to_phone_map (Optional[dict]): Letter-to-phone map (keys are letters, values are paths to soundfiles). If left empty, the default map will be used. 
            global_audio_processing_map (Optional[dict]): Global audio processing options (keys are audio processing options, values are their values). If left empty, the default map will be used.
            specific_audio_processing_map (Optional[dict]): Specific audio processing options (keys are letters, values are dicts with audio processing options).
        """
        self.l2pm = default_l2pm if default_l2pm == None else letter_to_phone_map
        self.gapm = default_l2pm if default_gapm == None else global_audio_processing_map
        self.sapm = specific_audio_processing_map

        self.__replace_l2pm_paths_with_audios()
        self.__apply_audio_processing_maps()
    

    ####################################################

    def say(self, text:str, output_path: Optional[str] = None, play_to_speakers: Optional[bool] = True):
        '''
        loop over characters contained in a given text and pronounce them
        
        Args:
            text (str): text to be pronounced
            output_path (Optional[str]): path to a file where the output will be saved. If left empty, the output will not be saved.
            play_to_speakers (Optional[bool]): if True, the output will be played to speakers. If False, the output will not be played to speakers.
        '''
        for letter in text:
            if self.l2p_map.get(letter) != None:
                self.__say_letter(letter)
                


    def __say_letter(self, letter: str):
        'parse options associated with a given character and, after that, play a sound associated with the character'

        self.__play_sound()
        pass
    

    def __play_sound(self, path: str):
        'play a sound associated with a character'

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


    def __write_sound_to_file(self, s: AudioFile):
        'write a sound associated with a character to a file'

        board = Pedalboard([Chorus(), Reverb(room_size=0.25)])

        # Open an audio file to write to:
        with AudioFile('output.wav', 'w', s.samplerate, s.num_channels) as o:
        
            # Read one second of audio at a time, until the file is empty:
            while s.tell() < s.frames:
                chunk = s.read(int(s.samplerate))
                
                # Run the audio through our pedalboard:
                effected = board(chunk, s.samplerate, reset=False)
                
                # Write the output to our output file:
                o.write(effected)


    ####################################################

    def __apply_audio_processing_maps(self):
        'apply audio processing options to all sounds in l2pm'
        pass


    def __replace_l2pm_paths_with_audios(self):
        'replace soundfile paths in letter-to-phone map with the sounds themselves'
        for k, v in self.l2pm.items():
            map[k] = AudioFile(v)


    ####################################################

    def __validate_l2pm(self, map: dict):
        'validate a letter-to-phone map'
        pass


    def __validate_gapm(self, map: dict):
        'validate a global audio processing map'
        pass


    def __validate_sapm(self, map: dict):
        'validate a specific audio processing map'
        pass


        



############################################################################################################

from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile

# Make a Pedalboard object, containing multiple audio plugins:
board = Pedalboard([Chorus(), Reverb(room_size=0.25)])

# Open an audio file for reading, just like a regular file:
with AudioFile('some-file.wav') as f:
  
  # Open an audio file to write to:
  with AudioFile('output.wav', 'w', f.samplerate, f.num_channels) as o:
  
    # Read one second of audio at a time, until the file is empty:
    while f.tell() < f.frames:
      chunk = f.read(int(f.samplerate))
      
      # Run the audio through our pedalboard:
      effected = board(chunk, f.samplerate, reset=False)
      
      # Write the output to our output file:
      o.write(effected)
        


