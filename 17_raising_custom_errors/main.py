a = input("Enter a value between 6 and 10: ")

if  (a == 'quit'):
    print("Quitting the program.")
elif (int(a)<6 or int(a)>10):
    raise print('Value should be between 6 and 10')
else:
    print("Program runs successfully.")