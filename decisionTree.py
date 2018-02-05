import csv
import sys
import math

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
                predict_field = reader.fieldnames[-1] # get the key of the last column from csv file
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


class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

def entropy(p1,p2):
    return (-1) * p1 * math.log(p1, 2.0) - p2 * math.log(p2, 2.0)

def mutual_info(entro1,entro2):
    return entro1 - entro2
    


MAX_DEPTH = sys.argv[3] # receive max depth from command line

def main():
    if MAX_DEPTH == 0:




main()


case = Label(sys.argv[1])
print case.label_possitive
print case.label_negative
print case.label_pos_count
print case.label_neg_count
print case.p_pos
print case.p_neg
