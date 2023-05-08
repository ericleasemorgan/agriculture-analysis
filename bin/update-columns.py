#!/usr/bin/env python

# update-columns.py - given a specifically shaped CSV file, update a database

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# August 9, 2021 - first investigations


# configure
METADATA = './study-carrel/metadata.csv'
DB       = './study-carrel/etc/reader.db'
UPDATE   = "UPDATE bib SET %s='%s' WHERE id='%s';"

# require
import sys
import pandas  as pd
import sqlite3 

# get input
if len( sys.argv ) != 2 : sys.exit( 'Usage: ' + sys.argv[ 0 ] + " <field>" )
field = sys.argv[ 1 ]

# initialize and connect to the database
metadata   = pd.read_csv( METADATA )
connection = sqlite3.connect( DB )

# loop through each row
for index, row in metadata.iterrows() :
	
	# parse
	value = str( row[ field ] )
	file  = row[ 'file' ]
	
	# create key and create sql
	key = file.replace( '.txt', '' )
	value = value.replace( "'", "''" )
	sql = ( UPDATE % ( field, value, key ) )
	
	# debug
	# sys.stderr.write( '\t'.join( [ str( key ), field, value ] ) + '\n' )
	sys.stderr.write( sql + '\n' )
	
	# do the work
	connection.execute( sql )
	connection.commit()

# done
exit

	