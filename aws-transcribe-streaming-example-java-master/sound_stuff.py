# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:39:16 2018

@author: Admin
"""

# Names
names = ["John", "Donald"]

# colours
colours = ["red", "blue", "green", "yellow", "orange", "pink", "purple"]

# key story phrases
story_phrases = ["Once upon a time", "time"]

# kinematic action words
kinematics = ["walking", "running", "jumping", "skipping"]

# short clip sound effects - dictionary
sound_effects = {"thunder":"Storm_exclamation.mp3", 
                 "roar":"European_Dragon_Roaring_and_breathe_fire-daniel-simon.mp3",
                 "warrior":" ",
                 "fire":" "}

# audio clips
negative_music = 'Beethoven-MoonlightSonata.mp3'    
positive_music = 'SCOTT_JOPLIN_The_Entertainer.mp3'


def which_background_audio(sentiment):
    
    # keywords is a list
    
    if sentiment < 0.4:
        audio_clip = negative_music
    elif sentiment > 0.6:
        audio_clip = positive_music    
        
    return audio_clip

def which_sound_effect(keywords):
    print(sound_effects.keys)
    for i in keywords:
        if i in sound_effects.keys():
            key = i
        
    audio_clip = sound_effects[key]
    print(audio_clip)
    
#which_sound_effect(['thunder', 'lightning'])
    