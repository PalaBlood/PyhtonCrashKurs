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


#multiply2(2,11,3,2) # => 122




#Statt Zeilenumbruch mit end sagen was passiert
#print("Hallo", end=", ") 
#print("Welt")   # => Hallo, Welt




#print("Hallo", "Welt", "Und", "Ja") # => Hallo Welt Und JA
#print("Hallo", "Welt", "Und", "Ja", sep="-") # => Hallo-Welt-Und-Ja
#print("Hallo", "Welt", "Und", "Ja", sep="_") # => Hallo_Welt_Und_Ja




#Globale und lokale Variablen

test = 12 #Lokal

def print_test():
    test = 22
    print(test)

print(test) # => 12
print_test() # => 22 




def print_global_test():
    global test
    test = 80
    print(test)
    
print_global_test()  #=> 80
print(test)  # => 80

#Mit global greifen wir immer auf die globale Var zu und können sie auch manipulieren