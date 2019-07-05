from pytube import YouTube
from bs4 import BeautifulSoup as bs
import requests

yt = YouTube("https://www.youtube.com/watch?v=nuATgekXHtY&t=174s")

video = yt.streams.first()
video.download()
