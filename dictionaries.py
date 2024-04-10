alien_0 = {"color": "green", "points": 5}
#print(alien_0["color"]) # => green
#print(alien_0["points"]) # => 5

color = alien_0["color"] 
points = alien_0["points"]

#print(color) # => green
#print(points) # => 5




alien_0["x_position"] = 0
alien_0["y_position"] = 25

#print(alien_0) # => {'color': 'green', 
                    #'points': 5, 'x_position': 0, 'y_position': 25}

alien_0["color"] = "yellow"
#print(f"the alien color is now {alien_0["color"]}") # => the alien color is now yellow




alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':    
    x_increment = 1
elif alien_0['speed'] == 'medium':    
    x_increment = 2
else:    
    # Dies muss ein schnelles Schiff sein.    
    x_increment = 3

alien_0["speed"] = "fast"




#entfernen von dics
del alien_0["x_position"] 




#ähnliche Werte für verschiedene Objekte
favorite_languages = {'jen': 'python',    
                      'sarah': 'c',    
                      'edward': 'rust',    
                      'phil': 'python',}



#Überprüfen, ob ein Key vorhanden ist
alien_value = alien_0.get("points", 'Der Key "points" existiert nicht')
#Die Textnachricht erscheint nur, wenn der Key nicht existiert

#print(alien_value) #Der Key "points" existiert nicht



#Schleifen mit dictionaries
user_0 = {
    "first": "Michel",
    "last": "Finger"
}

#for key,value in user_0.items():
    #print(f"Key: {key}")
    #print(f"Value: {value}\n")
    
    
favorite_languages = {'jen': 'python',    
                      'sarah': 'c',    
                      'edward': 'rust',
                      'phil': 'python',}


for name,fav in favorite_languages.items():
    print(f"the favorite language of {name} is {fav}")




#Auf Keys zugreifen
skyrim_weapons = {
    "2": "breitschwert",
    "1": "basdartschwert",
    "3": "daedraschwert"
} 

for key in skyrim_weapons.keys():
    print(key) # => 2,1,3
    
for key in sorted(skyrim_weapons.keys()):
    print(key) # => 1,2,3
    
    

#Nur Values erhalten

getränke = {"1": "cola",
            "2": "fanta",
            "3": "pepsi"}

for name in getränke.values():
    print(name.title()) # => Cola, Fanta, Pepsi
