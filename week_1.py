import random  # importing libraries

# comments are preceded by a hashtag and run to the end of the line

#### setting a variable
sum_of_fives = 5 + 5

#### simple arithmetic

ten_plus_five = sum_of_fives + 5  # addition
ten_minus_two = sum_of_fives - 2  # subtraction
ten_times_two = sum_of_fives * 2  # multiplication
ten_divided_by_two = sum_of_fives / 2  # division
mod_four_of_ten = sum_of_fives % 4  # modulo sets the remainder after division
# mod_four_of_ten evaluates as 2 (remainder)

#### calling a function from a library
# we imported this library up top
# libraries are code that someone else has written and we can use

random_integer = random.randint(0, 5)
# random_integer variable will be a whole number between 0 and 5

# floats are decimal points

random_float = random.random()
# random_float variable is set to some random decimal between 0 and 1

### lists
make_a_list = ['to make a list', 'use square brackets']
make_a_list_on_separate_lines = [  # start the list
    'each value inside the list',
    'is kept together'
]  # end the list

call_a_list = make_a_list[0]
# lists are zero index based

#### printing to the command line
# to run this in the command line type 'python week_1.py'
print(sum_of_fives)
print(ten_plus_five)
print(ten_minus_two)
print(ten_divided_by_two)
print(mod_four_of_ten)
print(random_integer)
print(random_float)
print(call_a_list)

# for loop
for list_item in make_a_list_on_separate_lines:
    print('yay!')
    print(list_item)
