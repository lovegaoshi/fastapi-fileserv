This is a simple fileserver using fastapi. this is set up for noxplayer to sync playlists as a personal server.
<br>
to build with docker:
<br>
docker build -t fastapi .
<br>
sudo docker run -v "$(pwd)":/fastapi --rm -p 0.0.0.0:**9527**:5000/tcp fastapi uvicorn main:app --reload  --host=0.0.0.0 --port=5000
<br>
this command runs at port 9527. Then in noxplayer, set personal cloud address as: **http://{your VPS IP}:9527/**
<br>
<br>
use acme with zerossl and nginx:
<br>
https://www.rmedgar.com/blog/using-acme-sh-with-nginx/
<br>
folder /var/www/le_root/.well-known/acme-challenge needs a chmod +R 777 so acme has write access to it;
<br>
after issue cert is done, make a folder and install cert to that folder; do not use the .acme.sh/cert displayed after cert is issued, make acme copy certs to your specified folder instaed.
<br>
then nano nginx config to use ssl to your installed certs. 
<br>
also make a systemctl reload nginx in the /etc/crontab file to run as root, if acme cant run it for you.
