#Write a Python program that asks for a number, n, and then prints out all the numbers between 1 and n, inclusive, and the numbers' squares and cubes.

print("Can you give me a number?")

# variable = cast to integer ( number input from the user)
input_number = int(input())

print()

a = 1
while a <= input_number:

    number_square = a * a

    number_cube = a * number_square

    print("The number is " + str(a) + ", its square is " + str(number_square) + " and its cube is " + str(number_cube) + ".")

    a = a + 1

print()