from geoip2 import database
# we are trying to figure if a particular geolocation of particular ip address exists in the database or not
ip="96.126.113.153"
#change path accordingly to your path
database_path='/home/kali/Desktop/geolite2_city.mmdb' #it is a database object which is storing the location of the database of geoips in hex fomat or compressed binary format
# it is obtained from internet
def get_ip_location(ip_address):
    reader=database.Reader(database_path)
    try:
        response=reader.city(ip_address)
        country=response.country.name
        city=response.city.name
        latitude=response.location.latitude
        longitude=response.location.longitude
        print(f"IP:{ip_address}\nCountry:{country}\nCity:{city}\nLatitude:{latitude}\nLongitude:{longitude}")

    except Exception as e:
        print("Error",str(e))

    finally:
        reader.close()
if __name__ =="__main__":
    ip_to_lookup=ip
    get_ip_location(ip_to_lookup)

