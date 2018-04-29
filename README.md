
This directory contains tools and utilities for use with Elastic-Search and Kibana

	[1] ingest-data.py: Python script to bulk-insert data from CSV file into Elastic-Search

		Usage: ingest-data.py CSV_FILE INDEX_NAME

	The script takes 2 parameters: 
		- Input file in CSV format with column-names on the first line.
		- Name of the elastic-search index into which data should be inserted from CSV.
		  It is assumed that the index is already created with appropriate mappings,
		  otherwise, a new index will be created with default mappings.


Stay Tuned, more stuff to come soon..
