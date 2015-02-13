from csv import reader
with open('station_lines.csv',mode='rU') as infile:
    d = dict(reader(infile))

print d