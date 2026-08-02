filename = input("Enter file path and name (e.g. C:/folder/myfile.txt): ")
content = input("Enter content to write: ")

# WRITE mode - creates file and writes
try:
    with open(filename, "w") as file:
        file.write(content)
    print("File created and written successfully")
except Exception as e:
    print("Write Error:", e)

# READ mode - reads the file
try:
    with open(filename, "r") as file:
        data = file.read()
    print("Read content:", data)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Read Error:", e)

# APPEND mode - adds more content
try:
    with open(filename, "a") as file:
        file.write("\nThis is appended content")
    print("Content appended successfully")
except Exception as e:
    print("Append Error:", e)

# READ again to verify append
try:
    with open(filename, "r") as file:
        data = file.read()
    print("Final content:\n", data)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Read Error:", e)

# CREATE mode - only creates if file does NOT exist
try:
    with open(filename, "x") as file:
        file.write("Created with x mode")
    print("File created with x mode")
except FileExistsError:
    print("Create Error: File already exists (x mode only works on new files)")
except Exception as e:
    print("Create Error:", e)