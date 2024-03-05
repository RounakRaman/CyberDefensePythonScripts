from ipwhois import IPwhois
# this module helps to extract the ip and its owner and other relevant details associated with that particular ip

def perform_ip_whois(ip_address):
    try:
        ip=IPwhois(ip_address)
        ip_info=ip.lookup_rdap()
        print(ip_info)
    #the output is in form of json
    except Exception as e:
        print("Error",str(e))

if __name__ =="__main__":
    ip_address="13.155.156.118" #replace with the IP address you want to look up
    perform_ip_whois(ip_address=ip_address)