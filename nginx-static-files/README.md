sudo docker run \
    --rm --name nginx-static-media -P \
    -v $PWD/media:/www/media \
    -v $PWD/nginx.conf:/etc/nginx/conf.d/default.conf \
    nginx