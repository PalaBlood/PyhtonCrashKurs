bicycles = ['trek', 'cannondale', 'redline', 'specialized']


#print(bicycles[0].title()) # => Trek

#print(bicycles[-1]) # => specialized

message = f"my first bicycle was a {bicycles[0]}!"
#print(message)


bicycles[0] = "honda"

#print(bicycles[0]) # => honda

bicycles.insert(1, "Porsche") #an Stelle 1 

#print(bicycles) # => ['honda', 'Porsche', 'cannondale', 'redline', 'specialized'] 

bicycles.pop(1)

#print(bicycles) # => ['honda', 'cannondale', 'redline', 'specialized']




#choose_remove = input("Wähle eine Marke, die du entfernen möchtest")

#bicycles.remove(choose_remove) #Nur das erste Element!

#print(bicycles)



sport_brand = ["Adidas", "Adidas", "Nike", "Adidas", "Nike", "Nike"]

#alle ausgewählten Elemente aus einer Liste entfernen

x = 0
while x < len(sport_brand):
        if sport_brand[x] == "Nike":
            sport_brand.pop(x)
        else:
            x +=1
        
print(sport_brand)
        

