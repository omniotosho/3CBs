import os

# Directories to create
dirs = [
    'myapp/management',
    'myapp/management/commands'
]

# Files to create
files = [
    'myapp/management/__init__.py',
    'myapp/management/commands/__init__.py'
]

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create files
for file in files:
    with open(file, 'w') as f:
        pass

print("Directories and files created successfully.")
