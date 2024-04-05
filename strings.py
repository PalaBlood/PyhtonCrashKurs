first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print_mesage = f"Hello, {full_name.title()}!"
#print(print_mesage)




favorite_language = "Python   "

favorite_language = favorite_language.rstrip() #rechten weißraum entfernen
#print(favorite_language)

favorite_language2 = "  Python"

favorite_language2 = favorite_language2.lstrip() #linken weißraum entfernen
#print(favorite_language2)

favorite_language3 = "  Python  "

favorite_language3 = favorite_language3.strip() #Weißraum von beiden Seiten entfernen
#print(favorite_language3)








großer_text = "HaLlo Welt"
großer_text = großer_text.lower()
#print(großer_text)

kleiner_text = "ich bin ein kleiner text"

kleiner_text = kleiner_text.upper()
print(kleiner_text)





#Präfix / entfernen 
nostarch_url = "https://nostarch.com"
only_url = nostarch_url.removeprefix("https://")
#print(only_url) # => nostarch.com

