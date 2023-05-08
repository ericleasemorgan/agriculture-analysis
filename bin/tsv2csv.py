#!/usr/bin/env python

# tsv2csv.py - given a few configurations, output a metadata file suitable for the Reader

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# September 23, 2022 - first cut; first full day of autumn
# September 24, 2022 - got it working, I think
# April     18, 2023 - tweaked for a HathiTrust collection file

# configure
COLLECTION      = './etc/collection.tsv'
SPLITS          = './corpus/splits'
SPLITSPATTERN   = '*.txt'
BASENAMEPATTERN = '-\d\d\d\.txt'

# require
from pathlib import Path
import re
import pandas as pd
import sys

# read and augment the given TSV file
collection           = pd.read_csv( COLLECTION, sep='\t')
collection[ 'date' ] = collection[ 'rights_date_used' ].astype( str )
collection[ 'file' ] = ''

# get and process each file matching the given pattern; create and fill metadata dataframe
metadata = pd.DataFrame( columns=collection.columns )
for index, filename in enumerate( Path( SPLITS ).glob( SPLITSPATTERN ) ) :

	# get the basename (root) of the given file
	file     = str( filename.name )
	basename = re.sub( BASENAMEPATTERN, '', file )
	
	# get the one and only row matching basename; tricky
	row = pd.DataFrame( collection[ collection[ 'htid' ] == basename ] )
	
	# update the row and update the metadata
	row[ 'file' ] = file	
	metadata      = pd.concat( [ metadata, row ] )
			
# output, and done
print( metadata.to_csv( index=False ) )
exit()

	
	
	