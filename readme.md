docker build -t fastapi .
sudo docker run -v "$(pwd)":/fastapi --rm -p 0.0.0.0:19527:5000/tcp fastapi uvicorn main:app --reload  --host=0.0.0.0 --port=5000

use acme with zerossl and nginx:

https://www.rmedgar.com/blog/using-acme-sh-with-nginx/
folder /var/www/le_root/.well-known/acme-challenge needs a chmod +R 777 so acme has write access to it;

after issue cert is done, make a folder and install cert to that folder; do not use the .acme.sh/cert displayed after cert is issued, make acme copy certs to your specified folder instaed.

then nano nginx config to use ssl to your installed certs. 
also make a systemctl reload nginx in the /etc/crontab file to run as root, if acme cant run it for you.