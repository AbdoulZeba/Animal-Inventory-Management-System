#
# Abdoul Hamid Zeba
# Comp163/ section 04
# 04/10/22
# Farm App.
#

class Animals:
    def __init__(self,age):
        
        self.name = ''
        self.age = age
        self.color = ''
        self.gender = ''
    def set_gender(self,gender):
        self.gender = gender
    def get_gender(self):
        return self.gender
        
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color  
    def set_age(self,age):
        self.age = age  
    def get_age(self):
        return self.age  
    def set_name(self,name):
        self.name = name 
    def get_name(self):
        return self.name
    
class Sheep(Animals):
    def __init__(self):
        
        self.set_name('Sheep')
        self.set_age(0)
        self.hair = 'normal'
        self.horn = ''
        
    def set_horn(self,horn):
        self.horn = horn
    def get_horn(self):
        if self.horn == 'Yes'.lower():
            self.horn = "Horn"
            return self.horn
        else:
            self.horn = "Hornless"
        return self.horn
    def get_gender_name(self):
        if self.gender == 'M'.lower():
            return 'Rams'
        else:
            return 'Ewe'
        
    def set_hair(self,hair):
        self.hair = hair
    def get_hair(self):
        if self.hair == 'B':
            self.hair = 'Bushy hair'
            return self.hair
        else:
            self.hair = 'Normal'
        return self.hair
    
class Cattle(Animals):
    
    def __init__(self):
        self.set_name('Cattle')
        self.gender = ''
        self.set_age(0)
        self.horn = 'Hornless'
    
    def set_horn(self,horn):
        self.horn = horn
    def get_horn(self):
        if self.horn == 'Yes':
             self.horn = 'Horn'
        else:
             self.horn = 'Hornless'
        return self.horn
    def get_gender_name(self):
        if self.gender == 'M'.lower():
            return 'Bull'
        else:
            return 'Cow'
    
class Goat(Animals):
    
    def __init__(self):
        
        self.set_name('Goat')
        self.set_age(0)
        self.gender = ''
        self.horn = ''
        self.beard = ''
    def set_horn(self,horn):
        self.horn = horn
    def get_horn(self):
        if self.horn == 'Yes'.lower():
            self.horn = "Horn"
            return self.horn
        else:
            self.horn = "Hornless"
        return self.horn
        
    def set_beard(self,beard):
        self.beard = beard
    def get_beard(self):
        if self.beard == 'Yes'.lower():
            self.beard = 'Bearded'
        else:
            self.beard = 'no beard'
        return self.beard
    def get_gender_name(self):
            if self.gender == 'M'.lower():
                return 'Buck'
            else:
                return 'Nanny'
        
class Chicken(Animals):
    
    def __init__(self):
        self.set_name('Chicken')
        self.set_age(1)
        self.gender = ''
        self.body_shape = ''
        self.beak = ''
    def set_body_shape(self,shape):
        self.body_shape = shape
    def get_body_shape(self):
        if self.body_shape == 'R'.lower():
            self.body_shape = 'Rounded body'
        else:
            self.body_shape = 'Normal body'
        return self.body_shape
    
    def set_beak(self,beak):
        self.beak = beak
    def get_beak(self):
        if self.beak == 'L'.lower():
            self.beak = 'Long beak'
        else:
            self.beak = 'Normal beak'
        return self.beak
    
    def get_gender_name(self):
        if self.gender == 'M'.lower():
            return 'Cock'
        else:
            return 'Hen'
    
class Horse(Animals):
    
    def __init__(self):
        self.set_name('Horse')
        self.set_age(1)
        self.gender = ''
        self.mane = 'no mane'
        self.speed =  '55 mph'
    def set_mane(self,mane):
            self.mane = mane
    def get_mane(self):
        if self.mane == 'B'.lower():
            self.mane = 'Bushy mane'
        else:
            self.mane = 'small mane'
        return self.mane
    
    def set_speed(self,speed):
            self.mane = speed
    def get_speed(self):
        return self.speed
    def get_gender_name(self):
        if self.gender == 'M'.lower():
            return 'Stallion'
        else:
            return 'Mare'
    
    
class Donkey(Animals):
    def __init__(self):
        
        self.set_name('Donkey')
        self.set_age(0)
        self.gender = ''
        self.stubborness = ''
    def set_mstubborness(self,stubborness):
            self.stubborness = stubborness
    def get_stubborness(self):
        return self.stubborness
    def set_age(self,age):
        self.age = age
    def get_age(self):
        return self.age
    def get_gender_name(self):
        if self.gender == 'M'.lower():
            return 'Jack'
        else:
            return 'Jenny'
        
def MenuPrompt():
    
    print()
    print("1-Sheep\n2-Horse")
    print()
    print("3--Goat\n4-Chicken")
    print()
    print("5-Cattle\n6-Donkey")
    print()
    return ''

MenuPrompt()

inventory_list = [[],[],[],[],[],[]]

doloop = True
while doloop:
    print()
    user_input = input("Make a selection or q to quit: ")
    print()
    
    if user_input == 'Q'.lower():
        doloop = False
        
    #geting sheep attributes from the user choice
    elif user_input == '1':
        sheep  = Sheep()
        sheep.get_name()
        inventory_list[0].append(sheep.get_name()) 
        print("Please enter your sheep attributes.")
        sheep.set_age(input("  Enter sheep age: "))
        inventory_list[0].append(sheep.get_age())
        sheep.set_horn(input("  Enter (No) for Hornless or (Yes) for horn: ").lower())
        sheep.set_gender(input("     Enter sheep gender (M or F): ").lower())
        inventory_list[0].append(sheep.get_gender_name())
        sheep.set_hair(input("   Hairsyle: enter (N) for Normal or (B) for Bushy: ").lower())
        inventory_list[0].append(sheep.get_hair())
        
    #geting horse attributes from the user choice
    elif user_input == '2':
        horse  = Horse() 
        print("Please enter your Horse's attributes.")
        horse.set_age(input("     Enter Horse age: "))
        inventory_list[4].append(horse.get_age())
        horse.set_gender(input("  Enter horse's gender (M or F): ").lower())
        inventory_list[4].append(horse.get_gender_name())
        horse.set_color(input("    Enter horse's color (Ex: Black): ").lower())
        inventory_list[4].append(horse.get_color())
        horse.set_mane(input("    Horse mane type. Enter (B) for bushy or (N) for normal:  "))
        inventory_list[4].append(horse.get_mane())
        horse.set_speed(input("   Enter horse's speed (ex: 55mhp): "))
        inventory_list[4].append(horse.get_speed())
        
    #geting goat attributes from the user choice
    elif user_input == '3':
        goat  = Goat() 
        print("Please enter your Goat's attributes.")
        goat.set_age(input("  Enter Goat age: "))
        inventory_list[2].append(goat.get_age())
        goat.set_horn(input("  Enter (No) for Hornless or (Yes) for horn: ").lower())
        gender = goat.set_gender(input("     Enter goat's gender (M or F): ").lower())
        inventory_list[2].append(goat.get_gender_name())
        goat.set_beard(input("Enter (Yes) for beard or (No) for no beard: ").lower())
        inventory_list[2].append(goat.get_beard())
        goat.set_color(input("  Enter goat's color (Ex: Black): ").lower())
        inventory_list[2].append(goat.get_color())
        print()
        
    #geting chicken attributes from the user choice
    elif user_input == '4':
        chicken  = Chicken() 
        print("Please enter your Chicken's attributes.")
        chicken.set_age(input("  Enter Chicken age: ").lower())
        inventory_list[3].append(chicken.get_age())
        chicken.set_gender(input("     Enter Chicken's gender (M or F): ").lower())
        inventory_list[3].append(chicken.get_gender_name())
        chicken.set_color(input("  Enter Chicken's color (Ex: Black): ").lower())
        inventory_list[3].append(chicken.get_color())
        chicken.set_beak(input("Enter Chicken's beak type (L) for long or (N) for normal: ").lower())
        inventory_list[3].append(chicken.get_beak())
        chicken.set_body_shape(input("Enter Chicken body sahpe (R) for rounded or (N) for normal: ").lower())
        inventory_list[3].append(chicken.get_body_shape())
        print()
        
    #geting cattle attributes from the user choice
    elif user_input == '5':
        cattle  = Cattle()
        print("Please enter your Cattle's attributes.")
        cattle.set_age(input("  Enter Cattle age: "))
        inventory_list[1].append(cattle.get_age())
        cattle.set_horn(input("  Enter (No) for Hornless or (Yes) for horn: ").lower())
        cattle.set_gender(input("   Enter Cattle's gender (M or F): ").lower())
        inventory_list[1].append(cattle.get_gender_name())
        cattle.set_color(input("  Enter cattle's color (Ex: Brown-white): ").lower())
        inventory_list[1].append(cattle.get_color())
        print()
    #geting donkey attributes from the user choice
    elif user_input == '6':
        donkey  = Donkey() 
        print("Please enter your Donkey's attributes.")
        donkey.set_age(input("     Enter Donkey age: "))
        inventory_list[5].append(donkey.get_age())
        donkey.set_gender(input("  Enter donkey's's gender (M or F): ").lower())
        inventory_list[5].append(donkey.get_gender_name())
        donkey.set_color(input("    Enter donkey's color (Ex: Black): ").lower())
        inventory_list[5].append(donkey.get_color())
        donkey.set_mstubborness(input("    How stubborn is your donkey? (0-100%): "))
        inventory_list[5].append(donkey.get_stubborness())
        print()
        
# printing all animals inventoried.
print("Inventory List:")

if len(inventory_list[0]) > 0:
    print(f'    1) Sheep({inventory_list[0][2]})')
    print(f'        Age: {inventory_list[0][1]}')
    print(f'        Hairstyle: {inventory_list[0][3]}')
    print()
if len((inventory_list[4])) > 0:
    
    print(f'    2) Horse({inventory_list[4][1]})')
    print(f'        Age: {inventory_list[4][0]}')
    print(f'        Color: {inventory_list[4][2]}')
    print(f'        Horse mane type: {inventory_list[4][3]}')
    print(f'        Horse\'s speed: {inventory_list[4][4]}')
    print()

if len((inventory_list[2])) > 0:
    print(f'    3) Goat({inventory_list[2][1]})')
    print(f'        Age: {inventory_list[2][0]}')
    print(f'        Color: {inventory_list[1][2]}')
    print(f'        {inventory_list[2][2]}')
    print()
if len((inventory_list[3])) > 0:
    
    print(f'    4) Chicken({inventory_list[3][1]})')
    print(f'        Age: {inventory_list[3][0]}')
    print(f'        Color: {inventory_list[3][2]}')
    print(f'        {inventory_list[3][4]}')
    print()

if len((inventory_list[1])) > 0:
    print(f'    5) Cattle({inventory_list[1][1]})')
    print(f'        Age: {inventory_list[1][0]}')
    print(f'        Color: {inventory_list[1][2]}')
    print()
if len((inventory_list[5])) > 0:
    
    print(f'    6) Donkey({inventory_list[5][1]})')
    print(f'        Age: {inventory_list[5][0]}')
    print(f'        Color: {inventory_list[5][2]}')
    print(f'        Sutubbornness level:{inventory_list[5][3]}')
    print()