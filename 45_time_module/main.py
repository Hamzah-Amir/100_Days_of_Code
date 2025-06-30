import time

def usingwhile():
    i = 0
    while i < 5000:
        i += 1
        print(i)

def usingfor():
    for i in range(5000):
        print(i)

init = time.time()
usingfor()
end1 = (time.time() - init)
init = time.time()
usingwhile()
end2 = (time.time() - init)
print(f"For loop time: {end1}") # Time taken by for loop
print(f"While loop time: {end2}") # Time taken by while loop

current_time = time.localtime()
print(current_time) # Local time

# Seek method

print("Working")
time.sleep(4)
print("This will print after 4 seconds of previous lines")

# Formatting the local time to well defined

formatted_time = time.strftime("%y-%m-%d-%H-%M-%S")
print(formatted_time)