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
import os


path = '/Users/ollie/Desktop/output2.txt'


def fizz_buzz(num):
    output = []
    for i in range(int(num)):
        new_num = i + 1
        if new_num % 3 == 0 and new_num % 5 == 0:
            output.append('fizzbuzz')
        elif new_num % 5 == 0:
            output.append('buzz')
        elif new_num % 3 == 0:
            output.append('fizz')
        else:
            output.append(new_num)

    with open(path, 'a+') as f:
        f.writelines(str(output))


number_to_reach = input('How high should we go? ')
fizz_buzz(number_to_reach)
