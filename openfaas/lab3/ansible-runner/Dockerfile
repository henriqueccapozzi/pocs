FROM centos:8

ADD https://github.com/openfaas/faas/releases/download/0.18.10/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

# Define your binary here
ENV fprocess="/usr/local/bin/ansible-playbook"

RUN yum update && yum install -y \
    python36 \
    python36-devel \
    gcc && pip3 install ansible

CMD ["fwatchdog"]