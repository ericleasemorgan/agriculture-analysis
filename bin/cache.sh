#!/usr/bin/env bash

# cache.sh - given a collection file, get content from the 'Trust

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 15, 2023 - first cut


# configure
COLLECTION='/shared/projects/tonkel-agriculture-2023/etc/collection.tsv'
HTID2BOOKS='/shared/sandbox/htid2books'

# make sane, do the work, and done
cd $HTID2BOOKS
./bin/collection2books.sh $COLLECTION
exit
