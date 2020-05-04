FROM nginx
# COPY assets /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf
COPY letsencrypt /etc/nginx/letsencrypt