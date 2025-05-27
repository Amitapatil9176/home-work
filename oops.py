class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
def modify_number(n):
    n = 20
    print (n)

num = 10
modify_number(num)
print(num)  # Output: 10
def add_item(my_list):
    my_list.append(4)

nums = [1, 2, 3]
add_item(nums)
print(nums)  # Output: [1, 2, 3, 4] ✅ (changed!)
