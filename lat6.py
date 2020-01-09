class MyClass:
    nama = "Babastudio"

p1 = MyClass()
print(p1.nama)

class Person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age
    
    def myFunc(abc):
        print("Hello my name is "+ abc.name)
        print("my age is "+ str(abc.age))
    
p1 = Person("John", 36)
p1.myFunc()

# print(p1.name)
# print(p1.age)
