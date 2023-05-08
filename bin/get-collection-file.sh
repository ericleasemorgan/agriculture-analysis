#!/usr/bin/env bash

# get-collection-file.sh

URL='https://babel.hathitrust.org/cgi/mb?c=833789670&a=download&source=hathifiles&format=text'
TSV='./collection.tsv'

curl $URL > $TSV

