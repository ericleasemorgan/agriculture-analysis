#!/usr/bin/env bash

# copy.sh - copy 'Trust files to the local file system

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# May 15, 2023 - first cut


# configure
TXT='/shared/sandbox/htid2books/txt'
ORIGINALS='/shared/projects/tonkel-agriculture-2023/corpus/originals'

# do the work, and done
cp $TXT/*.txt $ORIGINALS
exit
