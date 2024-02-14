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

2024-02-14 - 1.0 - Arturo Gutierrez Loza
- List Top processes by memory usage

"""

import psutil

def get_top_processes(n=5):
    # Get all running processes
    all_processes = [(p.pid, p.memory_info().rss) for p in psutil.process_iter(['pid', 'name', 'memory_info'])]
    
    # Sort processes by memory usage
    sorted_processes = sorted(all_processes, key=lambda x: x[1], reverse=True)
    
    # Select top N processes
    top_processes = sorted_processes[:n]
    
    return top_processes

def main():
    top_processes = get_top_processes()
    
    print("Top processes by memory usage:")
    print("===============================")
    for pid, memory in top_processes:
        process = psutil.Process(pid)
        print(f"PID: {pid}, Name: {process.name()}, Memory Usage: {memory / (1024*1024):.2f} MB")

if __name__ == "__main__":
    main()
