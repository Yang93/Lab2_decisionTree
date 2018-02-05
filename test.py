import math
import sys
import csv


attribute_indx = -4
# while case.label_possitive != None :

class Label:
    def __init__(self,data):
        with open (data) as csv_file:
            reader = csv.DictReader(csv_file,delimiter = ",")
            self.label_possitive = None
            self.label_negative = None
            self.label_pos_count = 0.0
            self.label_neg_count = 0.0
            self.total_count = 0.0
            for row in reader:
                predict_field = reader.fieldnames[attribute_indx] # get the key of the last column from csv file
                label = row[predict_field]
                if self.label_possitive == None:
                    self.label_possitive = label
                    self.label_pos_count = self.label_pos_count + 1
                elif label != self.label_possitive:
                    self.label_negative = label
                    self.label_neg_count = self.label_neg_count + 1
                else:
                    self.label_pos_count = self.label_pos_count + 1
                self.total_count = self.total_count + 1
            self.p_pos = self.label_pos_count/self.total_count
            self.p_neg = self.label_neg_count/self.total_count
            self.entropy = (-1) * (self.p_pos) * math.log(self.p_pos, 2.0) - self.p_neg * math.log(self.p_neg, 2.0)


case = Label(sys.argv[1])
# print str(case.label_possitive) + ": " + str(case.label_pos_count)
# print str(case.label_negative) + ": " + str(case.label_neg_count)
# print "entropy: " + str(case.entropy)

print case.label_possitive
