FROM centos:7

ENV CLIENT_PASS uAdWnsCP^Nu2LY

RUN echo "=====> Configure EPEL repo" && \
    yum install -y epel-release && \
    echo "=====> Install packages" && \
    yum install -y openssh openssh-clients rssh && \
    useradd --uid 1500 --no-create-home --shell /usr/bin/rssh client && \
    usermod -a -G rsshusers client && \
    mkdir /home/client && \
    chown client:client /home/client && \
    chmod 0700 /home/client && \
    echo "=====> Generate SSH Keys" && \
    ssh-keygen -A && \
    mkdir /var/run/sshd && chmod 0755 /var/run/sshd && \
    echo "=====> Configure RSSH" && \
    echo "allowscp" >> /etc/rssh.conf && \
    echo "allowsftp" >> /etc/rssh.conf && \
    echo "${CLIENT_PASS}" > /client_pass && \
    chmod 0400 /client_pass && \
    cat /client_pass | passwd --stdin client && \
    yum clean all

ENV TZ UTC+3

COPY ./hook.sh /hook.sh

RUN echo "session [default=ignore] pam_exec.so /hook.sh" >> /etc/pam.d/sshd && \
    chmod 555 /hook.sh

CMD [ "/usr/sbin/sshd", "-e", "-D", "-p", "20000" ]
