# Reading one by one lines from a file
with open('file.txt') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

# writing a code to readline one by one and format it well
print("------Example 2------")
i = 0
with open('marks.txt','r') as f:
    while True:
        i = i + 1
        line = f.readline()
        if not line:
            break
        m1 = line.split(',')[0]
        m2 = line.split(',')[1]
        m3 = line.split(',')[2]
        print(f"Student {i} marks in English are: {m1}")
        print(f"Student {i} marks in Math are: {m2}")
        print(f"Student {i} marks in P.S.T are: {m3}")

print("------Example 3------")
# writing all line at once
with open('file2.txt','w') as f:
    lines = ['Hello\n', 'World\n', 'This is a test file.\n']
    f.writelines(lines)