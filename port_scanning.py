import socket
def get_target_host():
    """to get the taregt host by name"""
    try:

        target_ip=socket.gethostbyname(target_host)
    except socket.herror:
        return
    try:
        target_name=socket.gethostbyaddr(target_ip)
    except socket.herror:
        return 
def is_port_open(target_host,port):
    """This function will deal with the potential error that might occur when trying/attempting to connect to a port"""
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: #This is a context manager that will ultimately close the file when the operation is performed and is used to handle the errors
        #AF_INET is used for the IP v4 Scanning 
        #SOCK_STREAM it is used for the TCP
            s.settimeout(1) #setting a timeout for the connection attempt
            s.connect((target_host,port))

        return True #if the connection is made succesfful the try block will return True 
    except(socket.timeout,ConnectionRefusedError) as e:
        return False
# if __name__ == "__main__" defines the entry point of the python block
if __name__=="__main__":
    target_host=get_target_host()
    common_ports=[21,22,80,443]
    open_ports=[]
    for port in common_ports:
        if is_port_open(target_host,port):
            open_ports.append[port]
    print(f"The open ports in{target_host} are {open_ports}")

