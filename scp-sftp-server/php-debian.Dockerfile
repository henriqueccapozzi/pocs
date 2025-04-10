FROM php:7.4.33-zts-bullseye
# Install vsftpd and necessary tools
RUN apt-get update && \
    apt-get install -y vsftpd openssl openssh-server

# Create a user for FTP access
RUN useradd -ms /bin/bash ftpuser

# Create the FTP directory and set permissions
RUN touch /etc/vsftpd.conf && \
    chown root:root /etc/vsftpd.conf && \
    chmod 644 /etc/vsftpd.conf && \
    mkdir -p /var/run/vsftpd/empty && \
    chown root:root /var/run/vsftpd/empty && \
    chmod 0755 /var/run/vsftpd/empty && \
    mkdir -p /home/ftpuser/ftp && \
    chown ftpuser:ftp /home/ftpuser/ftp && \
    chmod 755 /home/ftpuser/ftp

RUN echo "ftpuser" > /etc/vsftpd.chroot_list

# Expose the FTP port and passive ports
EXPOSE 21 30000-30100

# Set a password for the ftpuser
ARG FTP_PASS
RUN echo "ftpuser:$FTP_PASS" | chpasswd

# Start vsftpd
CMD ["vsftpd","/etc/vsftpd.conf"]
