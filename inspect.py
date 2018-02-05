import csv
import sys
import math

with open (sys.argv[1]) as csv_file:
    reader = csv.DictReader(csv_file,delimiter = ",") # read in csv file as rows of dictionaries
    label_1 = None
    label_2 = None
    total_count = 0.0 # count how many total rows are there
    label_1_count = 0.0
    label_2_count = 0.0

    for row in reader:
        predict_field = reader.fieldnames[-1] # get the key of the last column from csv file
        label = row[predict_field]
        if label_1 == None:
            label_1 = label
            label_1_count = label_1_count + 1
        elif label != label_1:
            label_2 = label
            label_2_count = label_2_count + 1
        else:
            label_1_count = label_1_count + 1
        total_count = total_count + 1
    # print label_1 + ":",label_1_count, label_2 + ":", label_2_count, "Total:", total_count
    p1 = label_1_count/total_count
    p2 = label_2_count/total_count
    cal_entropy = (-1) * p1 * math.log(p1, 2.0) - p2 * math.log(p2, 2.0)
    cal_error = min(label_1_count, label_2_count)/total_count

#print "entropy:", cal_entropy
#print "error:", cal_error
output = open(sys.argv[2],"w")
output.write("entropy: " + str(cal_entropy) + "\n" + "error: " + str(cal_error))
output.close
