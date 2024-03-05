import hashlib

def read_dictionary(file_path):
    with open(file_path,'r') as file:
        return [line.strip() for line in file]
    

def hashing(word):
    return hashlib.sha256(word.encode()).hexdigest()


def checking_for_match_password(target_hash,list_of_words):
    for word in list_of_words:
        hashed_word=hashing(word)
        if hashed_word == target_hash:
            return word
    return None



if __name__ =="__main__":
    target_password=str(input("Enter the target password: "))
    target_hash=hashlib.sha256((target_password.strip()).encode()).hexdigest()
    dictionary="C:\Users\raman\OneDrive\Desktop\dictionary.txt" 
    list_of_words=read_dictionary(dictionary)
    cracked_password=checking_for_match_password(target_hash,list_of_words)

    if cracked_password:
        print(f"Password is cracked! The password is {cracked_password}")
    else:
        print("Oops the password is not found.Try again")
