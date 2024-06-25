FROM nginx:latest
# COPY ./html/index.html /usr/share/nginx/html/index.html
COPY ./html/ /usr/share/nginx/html/
RUN apt-get update && apt-get install -y procps
RUN mkdir -p /home/app/staticfiles