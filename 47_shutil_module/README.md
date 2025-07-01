# shutil Module Examples

This folder demonstrates how to use Python's built-in `shutil` module for common file and directory operations. The `main.py` file contains example code for the following tasks:

## Examples Included

1. **Copying a File**
   - Use `shutil.copy('source.txt', 'destination.txt')` to copy a file from one location to another.

2. **Copying a Directory**
   - Use `shutil.copytree('source_folder', 'destination_folder')` to copy an entire directory tree.

3. **Moving a File or Directory**
   - Use `shutil.move('old_location.txt', 'new_location.txt')` to move a file or directory to a new location.

4. **Removing a Directory Tree**
   - Use `shutil.rmtree('folder_to_delete')` to delete a directory and all its contents.

5. **Getting Disk Usage Statistics**
   - The script prints the total, used, and free disk space for the current directory using `shutil.disk_usage('.')`.

## How to Use

- Uncomment the example you want to run in `main.py` and provide the appropriate file or directory names.
- Run the script using:
  ```bash
  python main.py
  ```

## Note
- Be careful with operations like `shutil.rmtree` and `shutil.move`, as they can permanently delete or move files and directories.

For more information, see the [official Python documentation for shutil](https://docs.python.org/3/library/shutil.html). 