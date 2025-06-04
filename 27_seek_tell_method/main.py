# The code opens a file named 'sample.txt', seeks to the 12th byte, and reads the rest of the file from that point.
with open('sample.txt') as f:
    f.seek(12)
    data = f.read()
    print(data)
    print('\n')

# I can also tell program to read only a specific number of bytes
print('-----Example 2-----')
with open('sample.txt') as f:
    f.seek(12)
    data = f.read(20)  # Read only 20 bytes
    print(data)
    print('\n')

# Tell function returns the current position of the file pointer
print('-----Example 3-----')
with open('sample.txt') as f:
    f.seek(12)
    position = f.tell()  # Get the current position
    print(f'Current file pointer position: {position}')
    print('\n')

# truncate function used to specify the size of the file
with open('file.txt','w') as f:
    f.write('Hello, world! This is a test file.\n')
    f.truncate(20)  # Truncate the file to the first 20 bytes