#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import json, nltk, re, os
from unidecode import unidecode
from pprint import pprint
from nltk.corpus import stopwords
from operator import itemgetter
from string import Template

from extra_stopwords import extra_stopwords

def import_data(source):
    with open('bluecrawler/out/'+source+'.json') as data_file:    
        return json.load(data_file)[:10]

def process(sources, out):

    content_array = []

    for source in sources:
        data = import_data(source)

        for con in data:
            content_array.append(con['content'])

    stop_spanish = map(lambda x: unidecode(unicode(x, 'latin1')),stopwords.words('spanish'))
    stop_spanish = stop_spanish + extra_stopwords

    content = unidecode("\n".join(content_array))

    tokens = nltk.word_tokenize(content.lower())
    important_tokens = filter(lambda x: x not in stop_spanish and not len(x) < 3, tokens)

    text = nltk.Text(important_tokens)

    amountwords = len(text)
    distinctwords = set(text)
    words_importance = map(lambda x: (x, text.count(x)), distinctwords)

    tag_counts = sorted(words_importance, key=itemgetter(1), reverse=True)[:15]

    with open(os.path.join('words', out+'.json'), 'w') as output:
        output.write(json.dumps(tag_counts))



process(['pagina12', 'diarioregistrado'] , 'oficialistas')
process(['lanacion', 'clarin'] , 'oposicion')
