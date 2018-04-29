
# python script to bulk insert data from CSV file into Elastic-Search
# Usage: python ingest-data.py CSV_FILE INDEX_NAME

# importing libraries
import csv
import sys
import os

if len(sys.argv) < 3:
	print "Usage: ingest-data.py CSV_FILE INDEX_NAME"
	exit(1)

# input CSV file
filename = sys.argv[1]
# index name
index_name = sys.argv[2]

counter = 0
col_names = []

# read CSV file
with open(filename, 'rb') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		# first row contains column names
		if counter == 0:
			col_names = row
		else:
			text = "{ \"index\" : { \"_index\" : \"" + index_name + "\", \"_type\" : \"data\", \"_id\" : \"" + str(counter) + "\" } }\n"
			text = text + "{ "
			for j in range(len(row)):
				if j > 0:
					text = text + ", "
				text = text + "\"" + col_names[j] + "\" : \"" + row[j] + "\""
			text = text + " }\n"
			#print text
			command = "curl -s -XPOST localhost:9200/_bulk?pretty -H \'Content-Type: application/json\' -d \'" + text + "\'"
			os.system(command)
		counter += 1
