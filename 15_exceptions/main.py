a = input("Enter a number: ")
try:
    for i in range(1,11):
        print(f'{int(a)} * {i} = {int(a) * i}')
except:
    print("An error occurred:")

print("The code block after the except block will still run.")

b = int(input("Enter your number: "))
lst = [4,5,6,3]

try:
    print(a[b])
except ValueError:
    print("Only numbers are allowed")
except IndexError:
    print("Index out of range")