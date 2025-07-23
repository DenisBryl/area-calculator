print("==================")
print("📐AREA CALCULATOR 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

area = 0
shape = 0
base = 0
height = 0

while shape != 1 and shape != 2 and shape != 3 and shape != 4 and shape != 5:
    shape = int(input("Which shape: "))
    if shape != 1 and shape != 2 and shape != 3 and shape != 4 and shape != 5:
        print ("Wrong input. Try again.")
    
if shape == 5:
    exit()

while base <= 0:
    base = int(input("Base: "))
    if base <= 0:
        print ("Wrong input. Try again")

if shape==1 or shape==2:
    height = int(input("Height: "))

if shape == 1:
    area = 0.5 * base * height
elif shape == 2: 
    area = base * height
elif shape == 3:
    area = base ** 2
elif shape == 4:
    area = 3.14 * base**2

print("The area is ", area)