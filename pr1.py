#1
var_int = 10
var_float = 8.4
var_str = 'No'

print(f"Завдання 1 \n var_int = {var_int}, var_float = {var_float}, var_str = {var_str}")

#2
big_int = var_int * 3.5

print(f"Задання 2 \n big_int = {big_int}")
#3
var_float -= 1
print ("Завдання 3 \n", var_float)
#4
print("Завдання 4 \n", var_int / var_float)
print(big_int / var_float)

#5
print("завдання 5 \n", var_str*2+"Yes"*3)

#6

a = int(input("Введіть змінну а1 ")) 
b = int(input("Введіть змінну b1 "))
c = int(input("Введіть змінну а2 "))
e = int(input("Введіть змінну b2 "))
d = int(input("Введіть змінну t "))

result = (a*b-c*e)/(d*a-c)

print(f"Завдання 6 \n Змінні: \n a1 = {a} \n b1 = {b} \n a2 = {c} \n b2 = {e} \n t ={d} \n Результат: \n Pезультат = {int(result)}")
