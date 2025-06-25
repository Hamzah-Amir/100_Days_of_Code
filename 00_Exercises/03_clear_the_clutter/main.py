import os, shutil  

path = 'C:\\Users\\hamza\\AppData\\Local\\Temp'
found = False  # Start as False

for file in os.listdir(path):
    full_path = os.path.join(path,file)
    try:
        if os.path.isfile(full_path) or os.path.islink(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
    except Exception as e:
        print(e)
        break

print("Temp folders cleaned.")