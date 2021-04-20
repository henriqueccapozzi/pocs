FROM henriqueccapozzi/anpbits:controller-1.0.2
RUN \
    python3 -m pip install pika --upgrade && \
    yum install openssh-clients -y
WORKDIR /work