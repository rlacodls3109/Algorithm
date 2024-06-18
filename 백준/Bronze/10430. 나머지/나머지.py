input = input()
input2 = input.split()
A =int(input2[0])
B =int(input2[1])
C =int(input2[2])


print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)