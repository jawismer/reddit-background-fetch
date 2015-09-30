#!/usr/bin/python

# Created by John Wismer
# Reddit Background Fetch

subreddit = "earthporn" # image subreddit 
dir = "/Users/johnwismer/Pictures/Backgrounds/" # directory where images are stored

import urllib
import urllib2
import json
import os
from collections import namedtuple

fileList = os.listdir(dir)
for fileName in fileList:
	os.remove(dir+"/"+fileName)

f = urllib2.urlopen("http://www.reddit.com/r/"+subreddit+"/top/.json")
text = json.loads(f.read(), object_hook=lambda d: namedtuple('X', d.keys(), rename=True)(*d.values()))

postNum = 0
for post in text.data.children:
	if "imgur" in post.data.url:
		if ".jpg" in post.data.url:
			urllib.urlretrieve(post.data.url, dir+post.data.id+".jpg")
		else:
			urllib.urlretrieve(post.data.url+".jpg", dir+post.data.id+".jpg")
		postNum = postNum + 1;
	if postNum >= 10:
		break