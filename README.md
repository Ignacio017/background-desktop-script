# background-desktop-script
A simply script in python that change the desktop background depending on the day using cron

## Crontab:

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/bin/python3
 0 0 * * * export DISPLAY=:0 && /usr/bin/python3 path/to/the/script
