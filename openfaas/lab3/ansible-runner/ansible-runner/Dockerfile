FROM ghcr.io/openfaas/classic-watchdog:0.1.4 as watchdog

#FROM alpine:3.12
FROM centos:8

RUN mkdir -p /home/app

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog

RUN chmod +x /usr/bin/fwatchdog

# Add non root user
# RUN addgroup -S app && adduser app -S -G app
RUN useradd --system app && usermod --groups app --append app
RUN chown app /home/app

WORKDIR /home/app

RUN yum update && yum install -y \
    python36 \
    python36-devel \
    gcc && pip3 install ansible


# Populate example here - i.e. "cat", "sha512sum" or "node index.js"
ADD ./runner.sh .
ADD ./site.yaml .
RUN chmod +x /home/app/runner.sh
ENV fprocess="/home/app/runner.sh"
# Set to true to see request in function logs
ENV write_debug="true"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

USER app
CMD ["fwatchdog"]
