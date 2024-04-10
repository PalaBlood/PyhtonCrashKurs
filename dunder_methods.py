
class MyClass:
    def __init__(self, x):
        self.x = x
        
        
    def __str__(self):
        return f"MyClass object with x = {self.x}"
    
    
    def __repr__(self):
        return f"MyClass({self.x})"

obj = MyClass(5)
print(str(obj))  # Output: MyClass object with x = 5
print(repr(obj))  # Output: MyClass(5)




###
class MyList:
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5




###
class MyDict:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, key):
        return self.data[key]
    
    
    def __delitem__(self, key):
        del self.data[key]
        
        
my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})
print(my_dict['b'])  # Output: 2

del my_dict['b']




###
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return iter(range(self.start, self.end))

for num in MyRange(1, 5):
    print(num)  # Output: 1 2 3 4
