from math import pi

figure = str (input())
area = 0.0

# •	Ако фигурата е квадрат (square):
# на следващия ред се чете едно дробно число - дължина на страната му
if figure == "square":
    a = float (input())
    area = a * a

# •	Ако фигурата е правоъгълник (rectangle):
# на следващите два реда четат две дробни числа - дължините на страните му
elif figure == "rectangle" :
    a = float (input())
    b = float (input())
    area = a * b
# •	Ако фигурата е кръг (circle):
# на следващия ред чете едно дробно число - радиусът на кръга
elif figure == "circle":
    r = float (input())
    area = pi * (r * r)

# •	Ако фигурата е триъгълник (triangle):
# на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея
elif figure == "triangle":
    a = float (input())
    ha = float (input())
    area = (a * ha) / 2

else:
    print (f"{figure} not found")

print (f"{area:.3f}")