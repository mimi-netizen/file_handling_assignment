def write_to_file(filename, content):
  """
  Writes content to a text file in write mode.

  Args:
      filename: The name of the file to write to.
      content: The data to write to the file (string or list of strings).
  """
  try:
    with open(filename, 'w') as file:
      if isinstance(content, list):
        file.writelines(content)  # Write multiple lines efficiently for lists
      else:
        file.write(content)  # Write a single line
      print(f"Successfully wrote to {filename}")
  except (IOError, OSError) as e:
    print(f"Error writing to {filename}: {e}")

def read_from_file(filename):
  """
  Reads the contents of a text file and displays them on the console.

  Args:
      filename: The name of the file to read from.
  """
  try:
    with open(filename, 'r') as file:
      contents = file.read()
      print(f"Contents of {filename}:\n{contents}")
  except FileNotFoundError:
    print(f"File {filename} not found.")
  except (IOError, OSError) as e:
    print(f"Error reading from {filename}: {e}")

def append_to_file(filename, content):
  """
  Appends content to a text file in append mode.

  Args:
      filename: The name of the file to append to.
      content: The data to append to the file (string or list of strings).
  """
  try:
    with open(filename, 'a') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content + '\n')  # Add newline for clarity
      print(f"Successfully appended to {filename}")
  except (IOError, OSError) as e:
    print(f"Error appending to {filename}: {e}")

# Create the file
write_to_file("my_file.txt", ["Line 1: This is some text.\n", "Line 2: You can write numbers too: 42\n", "Line 3: And mix data types!\n"])

# Read the contents
read_from_file("my_file.txt")

# Append more lines
append_to_file("my_file.txt", ["Line 4: Appending some more content.\n", "Line 5: This is in append mode.\n", "Line 6: Enjoy file handling!\n"])

# Try reading a non-existent file (demonstrates error handling)
read_from_file("non_existent_file.txt")
