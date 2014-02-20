import json, nltk

def import_data(source):
    with open('bluecrawler/out/'+source+'.json') as data_file:    
    return json.load(data_file)

def process(source):
    data = import_data(source)
    print data

process('lanacion')