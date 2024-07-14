

# Description			: This very simple script opens the file server_list.txt and then does a nslookup for each one to check the DNS entry

import subprocess  # Import the subprocess module

for server in open("D:/serverlist.txt"):  # Open the file and read each line
    subprocess.Popen(
        ("nslookup " + server)
    )  # Run the nslookup command for each server in the list
