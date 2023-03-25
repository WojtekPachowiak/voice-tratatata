from typing import Literal, Optional
import numpy as np
from pedalboard import Pedalboard, Chorus, Reverb
from pedalboard.io import AudioFile, ReadableAudioFile, WriteableAudioFile
import sounddevice as sd
import yaml


class Tratatata:
    def __init__(self,
                letter_to_phone_map: Optional[dict[str, str]] = None, 
                global_audio_processing_map: Optional[dict[str,float]] = None, 
                specific_audio_processing_map: Optional[dict[str,dict]] = None,
                ) -> None:
        """
        Args:
            letter_to_phone_map (Optional[dict]): Letter-to-phone map (keys are letters, values are paths to soundfiles). If left empty, the default map will be used. 
            global_audio_processing_map (Optional[dict]): Global audio processing options (keys are audio processing options, values are their values). If left empty, the default map will be used.
            specific_audio_processing_map (Optional[dict]): Specific audio processing options (keys are letters, values are dicts with audio processing options).
        """

        self.__load_l2pm(letter_to_phone_map)
        self.__load_gapm(global_audio_processing_map)
        self.__load_sapm(specific_audio_processing_map)

        self.__determine_samplerate_and_numchannels()
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
        
        # Create a pedalboard with our effects:
        # board = Pedalboard([Chorus(), Reverb(room_size=0.25)])

        # array for storing the output:
        full_speech = np.array([]).reshape(1,-1)
        
        # Loop over the letters in the to-say text:
        for letter in text:
            # Get the sound associated with the letter:
            s = self.l2pm.get(letter)

            # If the letter is not in the map, skip it:
            if s == None:
                continue
            
            # Loop over the sound's frames:
            while s.tell() < s.frames:
                chunk = s.read(int(s.samplerate))

                # Run the audio through our pedalboard:
                # effected = board(chunk, s.samplerate, reset=False)

                full_speech = np.hstack([full_speech, chunk])
            
            # Reset the sound's position to the beginning (so that it can be played again):
            s.seek(0)

        # Play the output to speakers:
        if play_to_speakers:
            sd.play(full_speech.reshape(-1), self.samplerate, blocking=True)
        
        # Save the output to a file:
        if output_path != None:
            o = AudioFile(output_path, 'w', self.samplerate, self.num_channels)
            o.write(full_speech)
                


    ####################################################

    def __apply_audio_processing_maps(self):
        'apply audio processing options to all sounds in l2pm'
        pass


    def __determine_samplerate_and_numchannels(self):
        'determine sample rate and number of channels of all sounds in l2pm'
        sounds = list(self.l2pm.values())
        assert all(
            sounds[0].samplerate == s.samplerate and 
            sounds[0].num_channels == s.num_channels 
            for s in sounds), 'all sounds in l2pm must have the same sample rate and number of channels'
        self.samplerate = sounds[0].samplerate
        self.num_channels = sounds[0].num_channels

    ####################################################

    def __replace_l2pm_paths_with_audios(self, pre_l2pm: dict[str,str]) -> dict[str,ReadableAudioFile]:
        'replace soundfile paths in letter-to-phone map with the sounds themselves'
        for k, v in pre_l2pm.items():
            pre_l2pm[k] = AudioFile(v)
        return pre_l2pm 
    

    def __load_l2pm(self, letter_to_phone_map: Optional[dict[str, str]]):
        'decides whether to use a default or custom l2pm + replaces paths with sounds'
        if letter_to_phone_map == None:
            with open('default_maps/default_l2pm.yaml') as f:
                l2pm = yaml.load(f, Loader=yaml.FullLoader)
        else:
            l2pm = letter_to_phone_map

        self.l2pm = self.__replace_l2pm_paths_with_audios(l2pm)


    def __load_gapm(self, global_audio_processing_map : Optional[dict[str, float]]):
        'decides whether to use a default or custom gapm'
        if global_audio_processing_map == None:
            with open('default_maps/default_l2pm.yaml') as f:
                gapm = yaml.load(f, Loader=yaml.FullLoader)
        else:
            gapm = global_audio_processing_map

        self.gapm = gapm


    def __load_sapm(self, specific_audio_processing_map : Optional[dict[str, dict]]):
        'load a specific audio processing map'
        self.sapm = specific_audio_processing_map
        

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






