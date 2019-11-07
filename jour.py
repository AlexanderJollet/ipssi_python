#!/usr/bin/python3

import sys
import datetime

date = datetime.datetime.now()
str(date)
print(date.day)
jour = date.day
jour = jour%2

if jour == 0 : 
     print ("PAIR")
else :
     print ("IMPAIR")
