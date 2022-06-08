import csv

# name,department,birthday month
# john smith,Accounting,November
# erica mayer,IT,March

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    print(csv_reader)
    for row in csv_reader:
        print(row)
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]}, and was bord in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

# Column names are name,department,birthday month
# 	john smith works in the Accounting deparment, and was born in November.
# 	erica mayer works in the IT deparment, and was born in March.
# Processed 3 lines.