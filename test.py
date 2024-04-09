def mulitpli(*numbers): 
    sum = 1
    for i in numbers:
        sum *= i
        print(sum)
    return sum
 
 
mulitpli(2,2,3)