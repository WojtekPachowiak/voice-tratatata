# Text-to-speech using letter-phone ([phonetics term](https://en.wikipedia.org/wiki/Phone_(phonetics)), not "telephone"!) mapping. 

I'm inspired by:
- Undertale (https://www.youtube.com/watch?v=gGROjaIw5Xw) 
- Animal Crossing (https://www.youtube.com/watch?v=YekLRkiIW4Y)
- Banjo-Kazooie (https://www.youtube.com/watch?v=lPeuuCbc55c)

Implementation is inspired by the following videos:
- by Mizizizizi: https://www.youtube.com/watch?v=Eu7BcyyQsXs
- by Blipsounds: https://www.youtube.com/watch?v=4W57Wy6veUM

# TODO
1. types of letter-phone mapping:
    - random
    - letter-to-phone (k -> k, g-> g)
    - letters-to-phone (k, g -> k)
    - letter-to-syllable (t -> ta)
2. phone types
    - only vowels
    - only consonants
    - both vowels and consonants
    - exotic sounds (clicks)
    - fricatives, plosives, trills
    - non-human sounds (mechanical, industrial, animal)
3. pitch
    - uniform
    - variable
      - random
      - based on real vowel properties
4. Character/phone coverage:
    - single phone
    - Latin alphabet characters
    - [International Phonetic Alphabet](https://www.ipachart.com/) (IPA) characters
5. Adding procedural variation to pronunciation (people's voices differ, right?):
    - pitch
    - speed
    - "nasalness"
    - signal processing:
        - delay
        - reverb
        - phaser
        - bass & treble
        - ...


