import whois
#whois is quering and request protocol that queries a database for the assignee or owner of that domain,its registration details and other useful information about that domain name

def perform_whois(domain_name):
    try:
        whois_Info=whois.whois(domain_name)
        print(whois_Info)
    except Exception as e:
        print("Error",str(e))

if __name__ =="__main__":
    domain_name="96.126.113.153" #replace with the domain name you want to look up
    perform_whois(domain_name=domain_name)