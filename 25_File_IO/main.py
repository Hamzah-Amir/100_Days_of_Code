f = open("myfile.txt", 'r')
t = f.read()
print(t)
f.close()

# Another approach to open files
with open('myfile.txt','a') as f:
    f.write('\nThis is a new line.\n')
    f.write('This is another new line.\n') # By using this approach we do not have to close file manually