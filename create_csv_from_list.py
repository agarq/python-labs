import csv

# field names
lst_headers = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
lst_rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

with open('some.csv', 'w', newline='') as f:
    wr = csv.writer(f, delimiter=';')

    wr.writerow(lst_headers)
    wr.writerows(lst_rows)
