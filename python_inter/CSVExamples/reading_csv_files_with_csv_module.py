import csv

# name,department,birthday month
# john smith,Accounting,November
# erica mayer,IT,March

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    # print(csv_reader)
    for row in csv_reader:
        # print(row)
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} deparment, and was born in {row[2]}.')
            line_count += 1

    print(f'Processed {line_count} lines.')


