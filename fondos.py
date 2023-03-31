#!/usr/bin/bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin"
import os
import datetime
os.environ['DBUS_SESSION_BUS_ADDRESS'] = 'unix:path=/run/user/1000/bus'

today = datetime.date.today()

if today.strftime("%A") == "Monday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")

if today.strftime("%A") == "Tuesday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")
    
if today.strftime("%A") == "Wednesday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")

if today.strftime("%A") == "Thursday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")
    
if today.strftime("%A") == "Friday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")
    
if today.strftime("%A") == "Saturday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")
  
if today.strftime("%A") == "Sunday":
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/path/to/the/image")
