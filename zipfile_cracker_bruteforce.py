import zipfile
from tqdm import tqdm
import itertools

zip_file="address of the zip file here"
zip_file=zipfile.ZipFile(zip_file)

character_set="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

max_passwordlength=4

n_words=len(character_set)**max_passwordlength
print("Total password to test",n_words)

for password_length in range(1,max_passwordlength+1,1):
    for word in tqdm(itertools.product(character_set,repeat=password_length),total=len(character_set)**password_length,unit="word"):
        password="".join(word)
        try:
            zip_file.extractall(pwd=password.encode())
        except Exception:
            continue
        else:
            print("The password is:",password)
        exit(0)
    print("Unable to crack the password try longer password or different character set")
    

