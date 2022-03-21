# from func_create_csv import *
from fn_create_csv import create_csv
# field names
# lst_h = ['Name', 'Fruit', 'Color', 'Score']
lst_h = []

# data rows of csv file
lst_r = [['Jose', 'apple', 'red', '9.0'],
         ['Jhon', 'banana', 'blue', '9.1'],
         ['Neal', 'watermelon', 'gray', '9.3'],
         ['Andres', 'pineapple', 'black', '9.5']]

lst_r.append(['pepito', 'apple', 'red', '9.0'])

create_csv('superarchivo', lst_h, lst_r, ';')
