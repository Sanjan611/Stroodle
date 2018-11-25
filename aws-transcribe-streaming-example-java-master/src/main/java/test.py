import time
# import boto3
import json
# import requests
# from PIL import Image
import io
import os, sys
import pygame
from urllib.request import urlopen

filename = "story.txt"

file = open(filename, 'r')

subscription_key = "52e2c8faa1144077b4f44ef952f761db"
assert subscription_key
search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

image_url = urlopen(
"https://media-waterdeep.cursecdn.com/avatars/thumbnails/0/26/482/315/636238962276510242.jpeg?fbclid=IwAR2I-3-KfXwcqg0ISHiqzK2DBr9rQABaHgwfazFguacIJQ0pLwXiJgi_yDI").read()
print(search_urls)
print("Got here 0")
image_file = io.BytesIO(image_url)
print("Got here 1")
image = pygame.image.load(image_file)
print("Got here 2")
screen.blit(image, (0, 0))
print("Got here 3")
pygame.display.flip()
print("Got here 4")


