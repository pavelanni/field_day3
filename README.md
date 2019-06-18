# Field Day Registration

This small app will help to register visitors at our NFARL Field Day. 

Normally it runs on a Raspberry Pi with keyboard, display, and mouse connected to it.
No need for Internet connection because it runs as a local web application.
You just have to point the browser to http://rpi-01/visitors/new and ask visitors to fill the form.

The application is configured to use `nginx` and `gunicorn` together with Django.
I used the instructions from here: https://www.alibabacloud.com/blog/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04_594319
or from here: http://rahmonov.me/posts/run-a-django-app-with-nginx-and-gunicorn/

Here is my config:

`/etc/systemd/system/gunicorn.service`:

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=pavel
Group=www-data
WorkingDirectory=/home/pavel/Projects/field_day3
ExecStart=/home/pavel/.virtualenvs/field_day2018/bin/gunicorn --access-logfile  - --workers 3 --bind unix:/home/pavel/Projects/field_day3/field_day.sock field_day.wsgi:application

[Install]
WantedBy=multi-user.target
```

`/etc/nginx/sites-available/field_day`

```
server {
    listen 80;
    server_name rpi-01;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/pavel/Projects/field_day3;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/pavel/Projects/field_day3/field_day.sock;
    }
}
```


