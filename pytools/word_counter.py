"""
Copyright (c) 2024 Arturo Gutierrez Loza

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__author__ = "Arturo Gutierrez Loza"
__copyright__ = "Copyright (c) 2024 Arturo Gutierrez Loza"
__license__ = "MIT"

"""
Changelog:

2024-02-09 - 1.0 - Arturo Gutierrez Loza
- Word counter on a file using python.

"""

import sys
import string

def count_words(filename):
    word_counts = {}
    
    # Read the file
    with open(filename, 'r') as file:
        text = file.read()
    
    # Tokenize the text into words
    words = text.split()
    
    # Remove punctuation from the words and count occurrences
    for word in words:
        word = word.strip(string.punctuation).lower()
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

def print_report(word_counts):
    print("Word\t\tCount")
    print("--------------------")
    for word, count in word_counts.items():
        print(f"{word.ljust(15)}\t{count}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 word_counter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    word_counts = count_words(filename)
    print_report(word_counts)

if __name__ == "__main__":
    main()

