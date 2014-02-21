#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR/bluecrawler
. $DIR/bin/activate
rm out/*.json

do_crawl () {
    scrapy crawl $1 -o out/$1.json -t json
}

do_crawl lanacion
do_crawl clarin
do_crawl pagina12
do_crawl diarioregistrado

cd $DIR
python $DIR/generate_tagclouds.py
