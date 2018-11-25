import time
import boto3
import json
import requests
import json
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

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
#    b=json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)

    aa=json.loads(a)
#    bb=json.loads(b)
#    print(aa)
    try:
        aaa=aa["KeyPhrases"][0]["Text"]
#    sentiment_analysis = bb["SentimentScore"]
        print("Keyword: " + aaa)
#    print(sentiment_analysis["Negative"])
        return(aaa)#fo
    except:
        pass

#if __name__ == "__main__":
#
#    count = 0
#
#    while True:
#
##        list = ""
#
#        text = file.readline()
#
#        if text=="":
#            print("Waiting")
#            time.sleep(1)
#
#        else:
##            list = list + text
##            list = list.replace('\n', ' ')
#            count = count + 1
#            print(count)
#            if (count == 10):
#
#                print("Phrase to be analyzed: " + text)
#
#                try:
#                    print(text)
#                    search_term = text_analyse(text)
#                    phrase_to_image(search_term + " cartoon")
#                except:
#                    pass
#                count = 0
#
#            else:
#
#                pass


if __name__ == "__main__":
    
    previous_text = ""
    previous_search_term = ""
    
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
                search_term = text_analyse(text)
                if search_term == previous_search_term:
                    pass
                else:
                    previous_search_term = search_term
                    phrase_to_image(search_term + " cartoon")
            except:
                pass

