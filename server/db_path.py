import os

# Replace 'app.db' with your actual SQLite database file name
db_filename = 'app.db'

# Get the current working directory
current_dir = os.getcwd()

# Construct the absolute path to the database file
absolute_path = os.path.join(current_dir, 'instance', db_filename)

# Print the absolute path
print("Absolute path to SQLite database:", absolute_path)
