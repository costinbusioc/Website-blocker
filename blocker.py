import time
from datetime import datetime as dt

hosts_path_linux = "/etc/hosts"
hosts_path_windows = "C:\Windows\System32\drivers\etc\hosts"

#redirect IP for the sites to be blocked
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com"]

while True:
    #Block the desired websites between 8:00 and 16:00
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(hosts_path_linux, 'r+') as file:
            content = file.read()
    
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        #During the rest of the hours, allow connection to the websites
        with open(hosts_path_linux, 'r+') as file:
            content = file.readlines()

            file.seek(0)
            for line in content:
                if not any(website in line for website in
                        website_list):
                    file.write(line)
            file.truncate()

    #Check the time every 5 seconds
    time.sleep(5)
