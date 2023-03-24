# from pydantic import BaseModel, validator, root_validator
# from pathlib import Path
# import wave 
# from typing import Literal, NewType



# ##### Base types #####

# class Sound(BaseModel):
#     path: str
#     wave: wave.Wave_read | None

#     @validator('wave', always=True, pre=True)
#     def set_cs(cls, v, values):
#         with wave.open(values["path"], 'rb') as w:
#             return w

#     class Config:
#         arbitrary_types_allowed = True

    

# class Token(BaseModel):
#     __root__ : str

# class Tokens(BaseModel):
#     __root__: tuple[Token]

# ######################

# ##### Sound maps #####

# class RandomMap(BaseModel):
#     __root__ : list[Sound]

# class OrderedMap(BaseModel):
#     __root__ : list[Sound]

# class ConcreteMap(BaseModel):
#     __root__ : dict[Tokens,Sound]

# ######################

# ##### AUDIO PROCESSING #####

# class NamedBaseModel(BaseModel):
#     'used for inheriting only. adds the name of the class as a field'
#     name: str

#     @root_validator(pre=True)
#     def set_name(cls, values):
#         values['name'] = cls.__name__
#         return values

# class Delay(NamedBaseModel):
#     pass
# class Reverb(NamedBaseModel):
#     pass
# class Phaser(NamedBaseModel):
#     pass
# class BassTreble(NamedBaseModel):
#     pass
# class Pitch(NamedBaseModel):
#     type: Literal["uniform", "variable"]
#     value: int
    
# class Speed(NamedBaseModel):
#     value: int

# EffectChain = list[Pitch, Speed, BassTreble, Delay, Reverb, Phaser]

# Tokens2EffectChains = NewType("Tokens2EffectChains", dict[Tokens, EffectChain])

# class AudioProcessing(BaseModel):
#     general: EffectChain
#     specific: Tokens2EffectChains | None = None

# ######################


