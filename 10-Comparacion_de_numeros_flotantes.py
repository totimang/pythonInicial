x = 3.3
print(x)

y = 1.1 + 2.2
print(y)

print(x == y)

#cortamos la precisiones a "y" y luego lo igualamos con "x"
y_str = format(y, ".2g")
print("str ->", y_str)
print(y_str == str(x))

#forma matemática de resolver la igualación x = y, para que de True. 
print('x' * 10)
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)