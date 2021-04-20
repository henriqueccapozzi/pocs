FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY hccapozzi.com.crt /etc/ssl/hccapozzi.com.crt
COPY hccapozzi.com.key /etc/ssl/hccapozzi.com.key
