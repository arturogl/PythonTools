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
- New Find and repalce text on a file using python.

"""


import sys

def find_replace_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        file_data = file.read()

    # Perform the replacement
    file_data = file_data.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(file_data)

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: python3 findandreplace.py <file_path> <old_text> <new_text>")
        sys.exit(1)

    file_path = sys.argv[1]
    old_text = sys.argv[2]
    new_text = sys.argv[3]

    find_replace_in_file(file_path, old_text, new_text)

