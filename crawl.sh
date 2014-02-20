#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR/bluecrawler
. $DIR/bin/activate
scrapy crawl lanacion -o out/lanacion.json -t json
scrapy crawl clarin -o out/clarin.json -t json
