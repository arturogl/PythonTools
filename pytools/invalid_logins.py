#!/usr/bin/env python3
import subprocess

def get_failed_logins():
    # Run journalctl command to get the output for failed SSH login attempts
    process = subprocess.Popen(["journalctl", "_SYSTEMD_UNIT=ssh.service"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()

    # Decode the output and split it into lines
    output_lines = output.decode().split('\n')

    # Filter lines containing "Failed" or "Failure"
    failed_lines = [line for line in output_lines if "Failed" in line or "Failure" in line]

    # print(failed_lines)

    # Extract IP addresses and usernames from the failed attempts
    ip_user_count = {}
    for line in failed_lines:
        parts = line.split()
        if "user" in parts: 
            parts = line.split()
            user_index = parts.index("user")
            ip_index = parts.index("from")
            user = parts[user_index + 1]
            ip = parts[ip_index + 1]
            ip_user = ip + "_" + user
            if ip_user not in ip_user_count:
               ip_user_count[ip_user] = 1
            else: 
               ip_user_count[ip_user] += 1

    return ip_user_count

def generate_report(ip_user_count):
    # Prepare the report
    report = "Hostname_user with invalid logins\n"
    report += "-----------------------------------------------\n"
    for ip_user, count in ip_user_count.items():
        report += f"{ip_user}: {count}\n"
    return report

def main():
    # Get failed logins
    failed_logins = get_failed_logins()

    # Generate report
    report = generate_report(failed_logins)
   
    # Print report
    print(report)

if __name__ == "__main__":
    main()
