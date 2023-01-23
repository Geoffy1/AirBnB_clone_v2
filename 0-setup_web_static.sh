#!/usr/bin/env bash
# Setup servers `web_static` deployment.

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Emediong Francis" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
update="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "38i $update" /etc/nginx/sites-available/default
service nginx restart
exit 0
