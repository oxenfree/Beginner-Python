import os
import shelve

ollie = {
    'name': 'ollie',
    'job': 'pixel pusher',
    'work': 'roadbotics',
    'past jobs': ['cashier', 'receptionist', 'writer']
}

with shelve.open('ollie', writeback=True) as db:  # open a file (db) to write the dict out
    db['data'] = ollie  # writing out ollie dict to db

with shelve.open('ollie', writeback=True) as db_2:  # open the file again, to read this time
    # create a new dictionary from the db file we read in
    new_input_dict = db_2['data']

new_input_dict['job'] = 'code monkey'  # change the values

for item in new_input_dict.items():  # iterate through dicts by keys, values, or items (both)
    print(item)
