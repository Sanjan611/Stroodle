import pygame
import time

audio1 = "Storm_exclamation_wav.wav"
audio2 = "European_Dragon_Roaring_and_breathe_fire-daniel-simon_wav.wav"

#pygame.mixer.init(channels = 2)
pygame.mixer.init(frequency = 100, size = -16, channels = 1, buffer = 2**12) 
pygame.init()
#pygame.mixer.set_num_channels(2)
print(pygame.mixer.get_num_channels())


"""
pygame.mixer.music.load(audio1)
pygame.mixer.music.play(1)
time.sleep(6)
pygame.mixer.music.stop() 
"""
print(audio2)

aud1 = pygame.mixer.Sound(audio1)

channel0 = pygame.mixer.Channel(0)
channel0.play(pygame.mixer.Sound(audio1))

#pygame.mixer.Channel(0).stop()
pygame.mixer.Channel(1).play(pygame.mixer.Sound(audio2))

#pygame.mixer.Channel(1).stop() 


time.sleep(8)

pygame.mixer.Channel(1).stop() 
pygame.mixer.Channel(0).stop()

"""

                    #  checking if there is a change in sentiment forr the background music
                    if text_analyse(text)[1][1] == previous_sentiment[1]:
                        pass
                    else:
                        audio_background = sound_stuff.which_background_audio(sentiment)
                        pygame.mixer.Channel(0).stop()
                        #pygame.mixer.music.load(audio_background)
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(audio_background))
                        #pygame.mixer.music.play(1)

                    previous_sentiment = sentiment

                    # sound effects checked every time
                    audio_sound_effects = sound_stuff.which_sound_effect(search_term)

                    if(audio_sound_effects！= None)：
                        pygame.mixer.Channel(1).stop() 
                        #pygame.mixer.music.load(audio_sound_effects)
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(audio_sound_effects))
            """