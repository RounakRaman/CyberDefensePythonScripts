import socket
import argparse #this module is used if we want to pass some argument from python directly from the terminal
import ipaddress
from concurrent.futures import ThreadPoolExecutor
#next we will define and parse the command-line arguments to specify the target ip address or range and the number of threads for parallel scanning
def parse_arguments():
    parser=argparse.ArgumentParser(description="Basic Network Scanner")
    parser.add_argument("target",help="Target IP address or IP range")
    parser.add_argument("-t","--threads",type=int,default=10,help="Number of threads for parallel scanning")
    args=parser.parse_args()
    return args.target,args.threads

def scan_port(ip,port):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result=s.connect_ex((ip,port))
            if result == 0:
                print(f"Port {port} is open on {ip}")

    except socket.error:
        print("Error while connecting to port")

def validate_target(target):
    try:
        ipaddress.ip_network(target)
    except ValueError:
        print("Invalid IP address or range")
        exit(1)
"""Now we will create a function to perform the network scan by iterating through a range of ports for each target IP address"""

def network_scan(target,threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for ip in ipaddress.IPv4Address(target):
            for port in range(1,1025):
                executor.submit(scan_port,str(ip),port)

def main():
    target,threads=parse_arguments()
    validate_target(target)
    network_scan(target,threads)

if __name__ == "__main__":
    main()



