import os
import shelve


with shelve.open('ollie', writeback=True) as db:
    new_input_dict = db['data']  # set variable from file, read

new_input_dict['job'] = 'code monkey'


with shelve.open('ollie', writeback=True) as db:
    db['data'] = new_input_dict  # set file from variable, write

for item in new_input_dict.items():
    print(item)
