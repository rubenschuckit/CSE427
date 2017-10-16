# Script to determine extra credit for sentiment feedback for CSE427
# Created by Ruben Schuckit rschuckit@wustl.edu
# Feel free to make modifications and document them below
#
# Date:
# Change Description

import sys
import os

if len(sys.argv) != 5:
    print("Usage: extra_credit.py <hw number> <root directory> <output file> <order file with wustl keys>")
    sys.exit()

hw_num = sys.argv[1]
start_dir = sys.argv[2]
out_file = sys.argv[3]
order_file = sys.argv[4]

ec_dic = {}

for root, dirs, files in os.walk(start_dir, topdown=False):
    for name in files:
        if "hw" + hw_num + "_review.txt" == name:
            wustl_key = root.split('\\')[1]
            review_length = ''
            with open(os.path.join(root, name), 'r') as fin:
                review_length = len(fin.read().split())

            ec_dic[wustl_key] = 5 if review_length >= 50 else 0

order = open(order_file)
output_grades = open(out_file, "w")
for line in order:
    wustl_key = line.replace('\n', '')
    if wustl_key in ec_dic:
        output_grades.write(str(ec_dic[wustl_key]) + '\n')
    else:
        output_grades.write("0\n")

output_grades.close()