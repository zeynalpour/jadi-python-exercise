"""
حل تمرین‌های دوره «آموزش پایتون جامع» تدریس شده توسط جادی در وب‌سایت مکتبخونه.
لینک دوره: https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk346/

این راه‌حل‌ها در بهار ۱۴۰۴ ارائه شده و موفق به کسب نمره کامل (۱۰۰) شده‌اند.

لطفاً از این کدها تنها در راستای یادگیری استفاده نمایید.
در صورت اعلام هرگونه نارضایتی از سوی جادی یا مکتبخونه، این مخزن به حالت خصوصی (Private) درخواهد آمد و از دسترس خارج می‌شود.

ارادتمند،  
سعید زینل‌پور
"""

class Animal:
    zoo_name ='Central Zoo'
    def __init__ (self, name, species, age, sound = 'miu miu'):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
    
    def make_sound (self):
        print(self.sound)
        
    def __str__ (self):
         return f"This is a {self.species} with name {self.name} at {Animal.zoo_name} with {self.age} y.o and it make {self.sound} sound."
        
    def info(self):
        print(f'Name: {self.name}')
        print(f'Species: {self.species}')
        print(f'Age: {self.age}')
        print(f'Sound: {self.sound}')
        print(f'Zoo: {Animal.zoo_name}')
        
class Bird(Animal):
    def __init__ (self, name, species, age, wing_span = 10, sound = 'Jik Jik'):
        Animal.__init__(self, name, species, age, sound)
        self.wing_span = wing_span
        
    def make_sound(self):
       print(f"This is a bird and make sound {self.sound}")

    def info(self):
        super().info()
        print(f'Wing span: {self.wing_span}')

       

lion = Animal("Shir", "big cat", 12)
house_sparrow = Bird("Gonjishk",age= 1,species= "domesticus")

house_sparrow.info()
print(house_sparrow)
print()
lion.info()
print(lion)