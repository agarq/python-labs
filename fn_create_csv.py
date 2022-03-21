import csv


def create_csv(file_name, lst_headers=[], lst_rows=[], delimiter=','):

    file_ext = '.csv'
    file_name = file_name + file_ext

    with open(file_name, 'w', newline='') as f:
        wr = csv.writer(f, delimiter=delimiter)

        if lst_headers:
            wr.writerow(lst_headers)

        if lst_rows:
            wr.writerows(lst_rows)
