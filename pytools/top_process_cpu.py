import psutil

# Get a list of all running processes
all_processes = list(psutil.process_iter())

# Sort the processes by CPU usage
all_processes.sort(key=lambda x: x.cpu_percent(), reverse=True)

# Print the top 10 processes
print("Top 10 processes by CPU usage:")
for process in all_processes[:10]:
    print(f"PID: {process.pid} | Name: {process.name()} | CPU Usage: {process.cpu_percent()}%")
