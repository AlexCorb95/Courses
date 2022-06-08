import csv

with open('employee_file3.csv', mode='w') as csf_file:
    fieldnames = ['employee_name', 'department', 'birth_month']
    writer = csv.DictWriter(csf_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'employee_name': 'john smith', 'department': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'employee_name': 'erika', 'department': 'IT', 'birth_month': 'May'})
    writer.writerow({'employee_name': 'smith', 'department': 'HR', 'birth_month': 'April'})
    writer.writerow({'employee_name': 'jack wilson', 'department': 'Accounting', 'birth_month': 'December'})
    writer.writerow({'employee_name': 'john smith2', 'department': 'IT', 'birth_month': 'March'})
