#from bs4 import BeautifulSoup
from pymongo import MongoClient
#import certifi
#import urllib3
import json
import csv
import re

username = "scrumlords"
password = ""

client = MongoClient("mongodb+srv://scrumlords:"+password+"@cluster0-4ef7e.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["scraping"]
tweetCol = db["movies_test"]    
for x in tweetCol.find({},{ "_id": 0 }):
  print("new line")  
  print(x)