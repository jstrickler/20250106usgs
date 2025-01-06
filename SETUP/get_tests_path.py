"""Create a .env file that points to EXAMPLES/tests so that the 
    pytest tools in VSCode will work correctly
"""
import os

root_folder = os.path.dirname(os.getcwd())

print(f"root_folder: {root_folder}")


for folder in 'examples', 'EXAMPLES':
    examples_folder = os.path.join(root_folder, folder)
    if os.path.exists(examples_folder):
        test_folder = os.path.join(root_folder, 'EXAMPLES', 'tests')
        print(test_folder)
        break
else:
    print("EXAMPLES folder not found")
    exit(1)

