# Script to help with mapping GradeScope grades to Blackboard for CSE427
# Created by Ruben Schuckit rschuckit@wustl.edu
# Feel free to make modifications and document them below
#
# Date:
# Change Description

import csv
import sys

if len(sys.argv) != 4:
    print("Usage: grades.py infile (the gradescope file) order " \
          "(the order of student IDs in grade doc) outfile (name of output file)")
    sys.exit()

grade_scope_grade_file = sys.argv[1]
order_file = sys.argv[2]
output_file = sys.argv[3]

grade_dict = {}
with open(grade_scope_grade_file) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    csvDataFile.readline() # Ignore header row in CSV
    for row in csvReader:
        # map student id to grade
        grade_dict[row[1]] = row[3] if row[3] != '' else '0'

csvDataFile.close()

order = open(order_file)
output_grades = open(output_file, "w")
for line in order:
    student_id = line.replace('\n', '')
    if student_id in grade_dict:
        output_grades.write(grade_dict[student_id] + '\n')
    else:
        output_grades.write("0\n")

output_grades.close()
