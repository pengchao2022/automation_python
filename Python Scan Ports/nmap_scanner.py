import nmap # type: ignore

scanner = nmap.PortScanner()

# Define target IP address or hostname
target = input("Please enter your host name here:")
#target = "scanme.nmap.org"

# Run a basic scan on the target
scanner.scan(target)

# Print the scan results
for host in scanner.all_hosts():
    print("Host IP: ", host)
    print("Server State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])
