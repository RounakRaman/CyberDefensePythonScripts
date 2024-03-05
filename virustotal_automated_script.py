# VirusTotal is a threat intelligence platform which can be used to determine whether a file or a url or a domain is safe or not
#other threat intelligence sites like virus total are no distribute.com
# from a defender's perspective it is recommended to use virus total
import requests
import csv
from bs4 import BeautifulSoup

#API KEY for virus total
APIKEY='d22da1a934acf08cda48de847c9c14e26f1d8846dce0f0b9d440b62a720b3504'

def scan_ip(ip_address): #takes ip address as an argument 
    ip_scan_endpoint='https://www.virustotal.com/vtapi/v2/ip-address/report' #hit the ip_scan_endpoint using virus total
    parameters={
        'apikey':APIKEY,
        'ip':ip_address
    }
    response=response.get(ip_scan_endpoint,parameters)
    return response.json()
# now basis of the sacn results we filter the report depending upon how many hits we got

def extract_detection_info(scan_result):
    detection_count=scan_result.get('detected_communicating_samples',0)
    scan_date=scan_result.get('scan_date','')
    return detection_count,scan_date

if __name__ =="__main__":
    ips_to_scan=['8.8.8.8','208.67.222.222']
    #mention the list of ips you want to scan

    results=[]

    for ip in ips_to_scan:
        ip_result=scan_ip(ip)
        detection_count,scan_date=extract_detection_info(ip_result)
        results.append({'IP':ip,'detection':detection_count,'Scan_date':scan_date})

        # Write results to a CSV file,converting it from json format to csv format
        # doing this so as to use pandas library for later analysis and investigation
        csv_path='ip_scan_results.csv'
        with open(csv_path,'w',newline='',encoding='utf-8') as csv_file:
            fieldnames=['IP','Detection_count','Scan Date']
            csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(results)

    print(f"IP Scan is complete save to {csv_path}")






