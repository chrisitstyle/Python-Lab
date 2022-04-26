class Triangle:
    number_of_sides=3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        self.suma=angle1+angle2+angle3
    def __eq__(self,o):
        return self.suma == o
    def check_angles(self):
        if self == 180:
            return True
        else:
            return False
        
class Drink:
    def __init__(self,name,percent,price,capacity):
        self.name=name
        self.price=price
        self.percent=percent
        self.capacity=capacity
    def dod(self,o):
        __init__(self,)

        
my_triangle = Triangle(30,60,90)
print(my_triangle.check_angles())
print(my_triangle.number_of_sides)

Wódka = Drink("wódka",40,8,50)
Rum = Drink("rum",60,9,50)
Cola = Drink("cola",0,2,100)
Lód = Drink("lód",0,0,30)
wodrum = Drink(
    Wódka.name + " z " + Rum.name,
    ((Wódka.percent*Wódka.capacity)+(Rum.percent*Rum.capacity))/(Wódka.capacity+Rum.capacity),
    Wódka.price + Rum.price,
    Wódka.capacity + Rum.capacity
    )
print(wodrum.percent)
