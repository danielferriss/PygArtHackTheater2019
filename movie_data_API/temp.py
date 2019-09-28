import pandas as pd
import numpy as np
import sys
import requests
from lxml import html
from bs4 import BeautifulSoup
import urllib.parse

'''
url = "https://www.boxofficemojo.com/movies/?id=marvel0518.htm"
url = "https://www.boxofficemojo.com/movies/?id=marvel2019.htm"
'''

df = pd.read_csv(filepath_or_buffer = r'C:\Users\Solomon\Desktop\movie_with_data_API_new.csv')\

df = df[df['ID']==0]

df.to_csv(r'C:\Users\Solomon\Desktop\movie_with_data_API_box_office_gen.csv')

print(df['ID'])

