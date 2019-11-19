arguments = input()
arguments_as_list = arguments.split(" ")
list_to_integer = list(map(int, arguments_as_list))
apples_pieces = list_to_integer[0]*3
pieces = list_to_integer[1]


print(int((apples_pieces + pieces)//2))

