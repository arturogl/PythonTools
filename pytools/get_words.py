fname = input("Enter file name: ")
try:
  fh = open(fname)
  lst = list()

  for line in fh:
     words = line.split()     # Split the line into words
     for word in words:
        if word not in lst:
            lst.append(word)  # Add unique words to the list
            lst.sort()        # Sort the list of unique words

  print(lst)

except: 
    print("An error occurred.")
