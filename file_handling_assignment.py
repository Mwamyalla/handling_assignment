# File Creation and Writing
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is the first line.\n")
        file.write("The number following 1 is 2.\n")
        file.write("This is the third line, including a number: 3.\n")
except Exception as e:
    print(f"An error occurred while creating/writing to the file: {e}")
else:
    print("File created and initial content written successfully.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("\nReading from file:")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file you are trying to read does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending a fourth line.\n")
        file.write("And here goes the fifth.\n")
        file.write("Finally, this is the sixth line of text.\n")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
else:
    print("Additional lines appended successfully.")

# Displaying Updated Content
try:
    with open("my_file.txt", "r") as file:
        print("\nDisplaying updated file content:")
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred while reading the updated file: {e}")

