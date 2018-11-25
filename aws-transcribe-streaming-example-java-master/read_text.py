
import time
import boto3
import json
import requests
import json
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import sound_stuff
import pygame

filename = "story.txt"

file = open(filename, 'r')

subscription_key = "52e2c8faa1144077b4f44ef952f761db"
assert subscription_key
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"


def phrase_to_image(search_term):
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    #    search_urls=search_results["value"][0]["thumbnailUrl"]
    search_urls=search_results["value"][0]["thumbnailUrl"]
    image_data = requests.get(search_urls)
    image_data.raise_for_status()
    image = Image.open(BytesIO(image_data.content))
    image.show()



def text_analyse(text):
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    #    print('Calling DetectKeyPhrases')
    a=json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    b=json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    
    aa=json.loads(a)
    bb=json.loads(b)
    #    print(aa)
    try:
        aaa=aa["KeyPhrases"][0]["Text"]
        aaa=sound_stuff.remove_unwanted_words(aaa)
        sentiment_analysis = bb["SentimentScore"]
        ccc=max(zip(aa['SentimentScore'].values(),aa['SentimentScore'].keys()))
        print("Keyword: " + aaa)
        print("Max_Sentiment"+ccc)
        #    print(sentiment_analysis["Negative"])
        return([aaa,ccc])#fo
    except:
        pass



if __name__ == "__main__":
    
    previous_text = ""
    previous_search_term = ""
    
    # initialise the sentiment
    previous_sentiment = (0.9, 'Negative')
    
    
    
    while True:
        
        text = file.readline()
        
        if text=="":
            print("Waiting")
            time.sleep(1)
        
        
        
        else:
            
            if "time" in text:
                print("found")
                text = text.replace("time", "")
            
            if "One day" in text:
                print("found")
                text = text.replace("One day", "")
        
            print("Phrase to be analyzed: " + text)
            
            try:
                print("Text before " + text)
                text = text.replace(previous_text[:-2], "")
                text = text.replace(previous_text[:-5], "")
                text = text.replace(previous_text[:-10], "")
                print("Text to be excluded " + previous_text)
                print("Text after " + text)
                previous_text = text
                search_term = text_analyse(text)[0]
                sentiment=text_analyse(text)[1][1]
                
                if search_term == previous_search_term:
                    pass
                else:
                    previous_search_term = search_term
                    phrase_to_image(search_term + " cartoon")
                    
                    # SOUND STUFF
                    
                    pygame.mixer.init()
                    
                    #  checking if there is a change in sentiment forr the background music
                    if text_analyse(text)[1] == previous_sentiment:
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
                    
                    if(audio_sound_effects_result！= None)：
                        pygame.mixer.Channel(1).stop()
                        #pygame.mixer.music.load(audio_sound_effects)
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(audio_sound_effects))
                    """
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(audio_sound_effects)
                        pygame.mixer.music.play(1)
                        """
                            
                            
                            
                            
                            
            except:
                        pass
