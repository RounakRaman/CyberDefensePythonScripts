import threading
import socket
def get_target_host():
    return input("Enter the target host ip address")

def is_port_open(target_host,port):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.timeout(1)
            s.connect((target_host,port))
        return True
    except(socket.timeout,ConnectionRefusedError):
        return False

def check_port(target_host,target_port,open_ports):
    if is_port_open(target_host,target_port):
        open_ports.append(target_port) 

def perform_port_scans(target_host,ports):
    open_ports=[]
    threads=[]
    for port in ports:
        t=threading.Thread(target=check_port,args=(target_host,port,open_ports))
        threads.append(t)
        t.start()
        for t in threads:
            t.join()

    return open_ports

if __name__ == "__main__":
    target_host=get_target_host()
    common_ports=[21,22,80,443]
    perform_port_scans(target_host=target_host,ports=common_ports)


