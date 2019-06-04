"""
####################################################
################## FIZZ BUZZ! ######################
####################################################

The goal of Fizz Buzz:

Iterate through the natural integers up to a specified integer: number_to_reach.
If the current integer is divisible by 3 print "fizz"
If the current integer is divisible by 5 print "buzz"
If the current integer is divisible by 3 AND 5 print "fizzbuzz"
"""

# function


def fizz_buzz(num):
    for i in range(int(num)):  # int turns '9' into 9
        print(i)


number_to_reach = input('How high should we go? ')  # input
fizz_buzz(number_to_reach)
