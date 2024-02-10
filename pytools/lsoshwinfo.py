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
- List operating system and hardware information - Linux using python.

"""

import platform

def display_system_info():
    # Operating System Information
    system_info = platform.uname()
    print("Operating System Information:")
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

    # Hardware Information
    print("\nHardware Information:")
    with open('/proc/cpuinfo', 'r') as cpuinfo_file:
        cpuinfo = cpuinfo_file.read()
        print(cpuinfo)

    with open('/proc/meminfo', 'r') as meminfo_file:
        meminfo = meminfo_file.read()
        print(meminfo)

if __name__ == "__main__":
    display_system_info()
