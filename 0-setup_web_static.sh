#!/usr/bin/env bash                                
# sets up web servers for the deployment of web_static

#apt-get update                                    
#apt-get -y install nginx                          

testConf=~/bre_conf
defConf=/etc/nginx/sites-available/default
fakeHtml=/data/web_static/releases/test/index.html

echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
echo "Holberton School" | sudo tee /var/www/html/index.html

#-p no error if existing, make parent directories as needed
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
fakeHtml=/data/web_static/releases/test/index.html
echo "meow" > $fakeHtml

#-f force removes existing destination file
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/

echo "server {
              add_header X-Served-By $HOSTNAME;
 			  listen 80 default_server;
 			  listen [::]:80 default_server;

 			  root /var/www/html;
 			  index index.html index.htm index.nginx-debian.html;

			  server_name _;

  			  location /redirect_me {
  			    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
 			  }

  			  location /hbnb_static {
  			    alias /data/web_static/current/;
                index index.html index.htm;
 			  }

              error_page 404 /404.html;
              #location /404 {
              #    root /var/www/html;
              #    internal;
              #}
	  }" | tee "$testConf";

sudo cp "$testConf" "$defConf"
sudo service nginx restart;
