# Website-blocker
Website blocker developed in python

The project was developed following the course "The Python Mega Course" on Udemy. It provides you a script that will stop the possibility to connect to websites selected by you by overriding the /etc/hosts file, during specific working hours.

To run the script in background (without the need to have a terminal open), follow the commands:

```
 sudo crontab -e
 At the end of the file add:
 @reboot python3 /path/to/blocker.py
 
```

Enjoy!
