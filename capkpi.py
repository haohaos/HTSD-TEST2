import csv
import sys
import os

path = sys.argv[1]
output_path = sys.argv[2]
path_list = os.listdir(path)
for filename in os.listdir(path):
    writer = open(output_path + filename,'w')
    writer.write("timestamp,value\n")    
    with open(os.path.join(path,filename), "r") as f:
        print filename
        csvreader = csv.reader(f)
        for line in csvreader:
            ts = int(line[0]) / 1000
            value = float(line[1])
            writer.write("%d,%.4f\n" % (ts,value))
        writer.close()