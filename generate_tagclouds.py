#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import json, nltk, re
from pprint import pprint
from nltk.corpus import stopwords
from operator import itemgetter

def import_data(source):
    with open('bluecrawler/out/'+source+'.json') as data_file:    
        return json.load(data_file)

def process(source):
    data = import_data(source)
    
    content_array = []

    for con in data:
        content_array.append(con['content'])

    stop_spanish = map(lambda x: unicode(x, 'latin1'),stopwords.words('spanish'))
    content = "\n".join(content_array)

    tokens = nltk.word_tokenize(content)
    important_tokens = filter(lambda x: x.lower() not in stop_spanish, tokens)
    pprint(important_tokens)
    #pprint(important_tokens)
    text = nltk.Text(important_tokens)

    amountwords = len(text)
    distinctwords = set(text)
    words_importance = map(lambda x: {'count':(text.count(x)/amountwords)*100, 'word':x}, distinctwords)
    pprint(stop_spanish)
    pprint(sorted(words_importance, key=itemgetter('count')))

process('lanacion')