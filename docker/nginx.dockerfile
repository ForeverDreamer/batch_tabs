FROM nginx
COPY assets /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/nginx.conf