import shutil

# 1. Copy a file from source to destination
# shutil.copy('source.txt', 'destination.txt')

# 2. Copy an entire directory tree
# shutil.copytree('source_folder', 'destination_folder')

# 3. Move a file or directory
# shutil.move('old_location.txt', 'new_location.txt')

# 4. Remove an entire directory tree
# shutil.rmtree('folder_to_delete')

# 5. Get disk usage statistics about the given path
total, used, free = shutil.disk_usage('.')
print(f"Total: {total // (2**30)} GiB")
print(f"Used: {used // (2**30)} GiB")
print(f"Free: {free // (2**30)} GiB")

# EXERCISE: Practice with the shutil Module
# 1. Create a text file named 'testfile.txt' with some content in the current directory.
# 2. Use shutil to copy 'testfile.txt' to 'copied_testfile.txt'.
# 3. Move 'copied_testfile.txt' to a new name 'moved_testfile.txt'.
# 4. Delete 'moved_testfile.txt' using shutil.
# (Hint: Use shutil.copy, shutil.move, and os.remove or shutil for deletion.)
