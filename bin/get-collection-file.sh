#!/usr/bin/env bash

# get-collection-file.sh - cache a remote TSV file locally

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 15, 2023 - first documentation; could use error checking


# configure
URL='https://babel.hathitrust.org/cgi/mb?c=833789670&a=download&source=hathifiles&format=text'
TSV='./etc/collection.tsv'

# do the work and done
curl $URL > $TSV
exit
