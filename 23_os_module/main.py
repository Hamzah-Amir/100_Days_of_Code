import os
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

folders = os.listdir(current_dir)
# List all folders in the current directory
for folder in folders:
    print(folder)
    print(os.listdir(f"{current_dir}/{folder}"))

# Simple example: Create a directory and list its contents
try:
    # Create a new directory
    os.mkdir("example_dir")
    print("Created directory: example_dir")
    
    # List contents of current directory
    print("\nContents of current directory:")
    for item in os.listdir():
        print(f"- {item}")
        
except FileExistsError:
    print("Directory already exists!")
except Exception as e:
    print(f"An error occurred: {e}")
