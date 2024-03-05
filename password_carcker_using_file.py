from crypto import crypt

def read_dictionary(filepath):
    with open(filepath,'r') as f:
        return [word.strip('\n') for word in f.readlines()]

def test_case(target_password):
    salt=target_password[:2]
    for word in read_dictionary(filepath):
        cryptpass=crypt(word,salt)

        if cryptpass==target_password:
            return word
    return None


if __name__ =="__main__":
    filepath="file.txt" #Enter the path of the file in which the hash target password is stored alon with the username
    file=open(filepath,'r')
    for lines in file.readlines():
        if ':' in lines:
            user=lines.split(':')[0]
            target_password=lines.split(':')[1].strip()
            cracked_password=test_case(target_password)
            print(f"The user is:{user}")
            if cracked_password:
                print(f"The password is:{cracked_password}")
            else:
                print("The password is not found")
        