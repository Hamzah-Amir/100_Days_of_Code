import os  

path = 'C:/Users/hamza/Documents'
found = False
for file in os.listdir(path):
    if file.endswith('.temp'):
        full_path = os.path.join(path, file)
        try:
            os.remove(full_path)
            print(f"Deleted: {full_path}")
        except Exception as e:
            print(f"Error deleting {full_path}: {e}")

if not found:
    print("No .temp files found in the directory.")