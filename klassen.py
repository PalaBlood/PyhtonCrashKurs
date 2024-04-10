class Car:
    def __init__(self) -> None:
        self.__car_brand = None
        self.__horse_power = None
        self.__color = None
        self.__x_position = int
        self.__y_position = int
    
    #getter setter
    def get_car_brand(self):
        return self.__car_brand
    
    def set_car_brand(self,brandname):
        self.__car_brand = brandname
    
    
    def get_horse_power(self):
        return self.__horse_power
    
    def set_horse_power(self, integer):
        self.__horse_power = integer
        
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        
        
        
        #weitere methoden
    def print_brand_name(self):
        print(f"Die Automarke der aktuellen Instanz lautet {self.__car_brand}")
        
    def move_car(self,x,y):
        self.__x_position += x
        self.__y_position += y  
    
    def get_car_position(self):
        print(f"Die aktuelle x-position lautet {self.__x_position} und die y-position {self.__y_position}")
    
       
    

car1 = Car()
car1.set_car_brand("Audi")
car1.set_horse_power(300)
car1.set_color("White")
car1.print_brand_name()

car2 = Car()
car2.set_car_brand("Mercedes")
car2.set_horse_power(280)
car2.set_color("Black")
car2.print_brand_name()



#Speicherreferenzen
print(Car) # => <class '__main__.Car'>
print(car1) # => 0x000001F88B57D1F0>
print(car2) # => 0x000001F88B57D250>

car3 = car2
print(car3) # => 0x000001F88B57D250> //liegt auf dem selben Speicherort wie car2


