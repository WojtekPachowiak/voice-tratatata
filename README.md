# :loudspeaker: Text-to-speech using letter-phone ([phonetics term](https://en.wikipedia.org/wiki/Phone_(phonetics)), not "telephone"!) mapping. 

**Provide some text, *Tratatata* will pronounce it.**

There's a default map which maps latin letters to pronunciations of vowels and consonants (recorded by myself! :D). The letters not in this map will be ignored. \
You can also provide your own yaml file containing a mapping from your letters/characters to your sounds.

TODO: implement applying audio processing globally and to individual sounds. 

# Usage:

`python main.py "hello world!"`

`python main.py "jak dak chuju" --output-path "/path/to/output.mp3" --no-play-to-speakers`

`python main.py "cing ciang ciong" --l2pm-path "path/to/your/custom/letter/to/phone/map"`

`python main.py "lalalalala" --gapm-path "path/to/your/custom/global/audio/processing/map"`

`python main.py "he he ha ha" --sapm-path "path/to/your/custom/specific/audio/processing/map"`

# Examples of maps

Example of a letter-to-phone map:
```
{
    "a": "path/to/a/sound/file",
    "b": "path/to/b/sound/file",
    ...,
    "z": "path/to/z/sound/file"
}
```

Example of a global audio processing map:
```
{
    "speed" : 1.5,
    "pitch" : 2,
    ...
}
```

Example of specific audio processing map (they override global options):
```
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
```

# Inspirations

I'm inspired by:
- Undertale (https://www.youtube.com/watch?v=gGROjaIw5Xw) 
- Animal Crossing (https://www.youtube.com/watch?v=YekLRkiIW4Y)
- Banjo-Kazooie (https://www.youtube.com/watch?v=lPeuuCbc55c)
- video by Polygon: https://www.youtube.com/watch?v=xYZMWkmXX3k 
- video by Mizizizizi: https://www.youtube.com/watch?v=Eu7BcyyQsXs
- video by Blipsounds: https://www.youtube.com/watch?v=4W57Wy6veUM

## TODO
+ pitch
    - uniform
    - variable
      - random
+ Adding procedural variation to pronunciation (people's voices differ, right?):
    - pitch 
    - speed
    - "nasalness"
    - signal processing:
        - delay
        - reverb
        - phaser
        - bass & treble
        - ...
+ allo for trimming start and end of audio files (to reduce gaps between pronuncing each letter)


