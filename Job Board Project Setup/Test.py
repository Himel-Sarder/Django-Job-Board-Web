import os
import jupytext

def convert_py_to_ipynb(source_dir, target_dir):
    # Create the target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.py'):
            # Define the full file paths
            py_file_path = os.path.join(source_dir, filename)
            ipynb_file_path = os.path.join(target_dir, filename.replace('.py', '.ipynb'))

            # Convert the .py file to a .ipynb file
            jupytext.write(jupytext.read(py_file_path), ipynb_file_path)
            print(f"Converted {py_file_path} to {ipynb_file_path}")

# Define the source and target directories
source_dir = ('Pandas Data Analysis/Task1')
target_dir = 'Output'

# Call the conversion function
convert_py_to_ipynb(source_dir, target_dir)
