# Create the certificate and key

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -subj '/C=BR/ST=DF/L=Brasilia/O=Home/CN=*.pocs.hcapozzi.dev' \
  -keyout ./vsftpd.key.pem -out ./vsftpd.crt.pem
```

# Build the container

```bash
docker build --build-arg FTP_PASS=12345678 -t dev-php-ftp -f php-debian.Dockerfile .
```

# Start the container
```bash
docker run -it --network host --name dev-php-sftp --rm \
    -v $PWD/vsftpd.conf:/etc/vsftpd.conf \
    -v $PWD/vsftpd.crt.pem:/etc/ssl/private/vsftpd.crt.pem \
    -v $PWD/vsftpd.key.pem:/etc/ssl/private/vsftpd.key.pem \
    dev-php-ftp
```
