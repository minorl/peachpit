import csv, sys
filename = 'sampleData/A/556 - Daily - 20140125.CSV'
with open(filename, 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    try:
        for row in reader:
            print row
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
