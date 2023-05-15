#!/usr/bin/env bash

# restore.sh - clean and re-initialize cached plain text books to htid2books

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 15, 2023 - first cut


# configure
ORIGINALS='/shared/projects/tonkel-agriculture-2023/corpus/originals'
TXT='/shared/sandbox/htid2books/txt'
HTID2BOOKS='/shared/sandbox/htid2books'

# make sane, clean, do the work, and done
cd $HTID2BOOKS
./bin/clean.sh
cp $ORIGINALS/*.txt $TXT
exit
