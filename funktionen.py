#Beliebig viele Parameter entgegeben nehmen
def mulitply(*numbers): 
    sum = 1
    for i in numbers:
        sum *= i
    return sum
 
 
#mulitpli(2,2,3) # => 12


#beliebig viele Paramter aber mindestens
def multiply2(number1, number2, *numbers):
    sum = number1 * number2
    for i in numbers:
        sum *= i
    return sum


#multiply2(2,11,3) # => 66 