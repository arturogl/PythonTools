# Prompt the user for a file name
fname = input("Enter file name: ")

try:
    # Attempt to open the file
    with open(fname, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            print(line.upper())
except FileNotFoundError:
    print(f"File '{fname}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
