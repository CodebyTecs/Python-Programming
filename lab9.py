def print_matrix(matrix):
    for i in matrix:
        for elem in i:
            print(elem, end=" ")
        print()

# Задание 1

def func(x):
    return  x**2
a = 0
b = 1
n = 1000
h = (b - a)/n
f = []
i =a
integral = (func(a) + func(b))/2
for i in range(n):
    integral += func(a + i*h)
print(integral * h)

# Задание 2

from random import *

def f(a):
    if a[0][2]+a[1][2]+a[2][2] == a[0][1]+a[1][1]+a[2][1] == a[0][0]+a[1][0]+a[2][0] == a[0][0]+a[1][1]+a[2][2] == a[0][2]+a[1][1]+a[2][0] == 15:
        return 1
    else:
        return 0
def random():
    rand = list(range(1, 10))
    a = []
    shuffle(rand)
    for i in range(0, 9, 3):
        a.append(rand[i:i + 3])
    return a
n = 3
a = random()
while not(f(a)):
    a = random()
else:
    print_matrix(a)

# Задание 3

def find(cords, treasure_map):
    map = []
    for i in range(n):
        map.append(((int(cords[0]) - int(treasure_map[i][0]))**2 + (int(cords[1]) - int(treasure_map[i][1]))**2)**0.5)
    for i in range(n):
        if map[i] == min(map):
            res = f"{treasure_map[i][0]} {treasure_map[i][1]}"
            return res

treasure_map = []
n = int(input("Введите количество сокровищ: "))
print("Добавьте координаты сокровищ в формате x y")
for i in range(n):
    a = input()
    treasure_map.append(a.split())
cord = input("Введите координаты Александрав в формате x y: ")
cords = cord.split()
print(find(cords, treasure_map))

# Задание 4

def check_menu():
    for i in range(len(menu)):
        print(menu[i][0], end=" - ")
        elem = menu[i][1]
        for j in range(len(elem)):
            print(elem[j], end=" ")
        print(" - ", end="")
        print(menu[i][-1])

def find():
    name = input("Введите название блюда: ")
    for i in range(len(menu)):
        if name == menu[i][0]:
            elem = menu[i][1]
            for j in range(len(elem)):
                print(elem[j], end=" ")
            print(" - ", end="")
            print(menu[i][-1])

def add():
    add = []
    name = input("Введите название блюда: ")
    things = []
    while 1:
        thing = input("Введите ингридиенты: ")
        if thing == "":
            break
        things.append(thing)
    price = int(input("Введите цену: "))
    add.append(name)
    add.append(things)
    add.append(price)
    menu.append(add)
    print(menu)

def replace():
    name = input("Введите название блюда: ")
    price = int(input("Введите новую цену: "))
    for i in range(len(menu)):
        if name == menu[i][0]:
            menu[i][-1] = price
    print(menu)

menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

print("Какое действие вы хотите сделать?")
act = input()
if act == "Меню":
    check_menu()
elif act == "Найти блюдо":
    find()
elif act == "Добавить блюдо":
    add()
elif act == "Изменить цену":
    replace()
else:
    print("Ошибка")

# Задание 5

from random import randint

n = int(input("Введите количество строк:"))
m = int(input("Введите количество столбцов:"))

matrix_1 = [[0]*m for i in range(n)]
matrix_2 = [[0]*n for i in range(m)]

for i in range(n):
    for j in range(m):
        matrix_1[i][j] = randint(1,10**2)

matrix_1 = [[11,12,13,14],[21,22,23,24],[31,32,33,34]]
for i in range(n):
    for j in range(m):
        matrix_2[j][i] = matrix_1[i][j]
print_matrix(matrix_1)
print()
print_matrix(matrix_2)

# Задание 6

n = int(input("Введите размер матрицы: "))
matrix_1 = []

a = list(range(1, n*n+1))
for i in range(0, n*n, n):
    matrix_1.append(a[i:i + n])
print_matrix(matrix_1)

matrix_2 = matrix_1

matrix_2[0][0], matrix_2[-1][0] = matrix_2[-1][0], matrix_2[0][0]
matrix_2[0][n-1], matrix_2[-1][-1] = matrix_2[-1][-1], matrix_2[0][n-1]
print_matrix(matrix_2)



# Задание 7

from random import randint

n = int(input("Введите количество рядов: "))
m = int(input("Введите количество мест в ряду: "))
k = int(input("Введите количество необходимых мест: "))
matrix = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = randint(0, 1)

s = " "
for i in range(n):
    for j in range(m):
        s += " ".join(str(matrix[i][j]))
    if "0"*k in s:
        print(f"Места есть, ряд {i+1}")
        break
else:
    print("Мест нет")



# Задание 8 

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix[0][j] = 1
        matrix[i][0] = 1
        matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
for i in matrix:
    print(" ".join(f"{elem:6}" for elem in i))


# Задание 9

from random import *

matrix = [["."]*4 for i in range(4)]

matrix_ships = [0]*4
coordinates = [(i,j) for i in range(2) for j in range(4)]
shuffle(coordinates)
bomb = coordinates[0]
coordinates.remove(coordinates[0])
n = 6
c = 0
b = 0

for i in range(4):
    matrix_ships[i] = coordinates[n]
    coordinates.remove(coordinates[n])
    n -= 1

print_matrix(matrix_ships)
print(bomb)

while c < 4:
    print_matrix(matrix)
    z = input("Введите координаты: ").split(",")
    for i in range(4):
        if int(z[0]) == matrix_ships[i][0] and int(z[1]) == matrix_ships[i][1]:
            matrix[int(z[0])][int(z[1])] = "X"
            c += 1
        elif int(z[0]) == bomb[0] and int(z[1]) == bomb[1]:
            print("Бомба")
            c = 4
            b = 1
            break
else:
    if b != 1:
        print("Вы выиграли!")


