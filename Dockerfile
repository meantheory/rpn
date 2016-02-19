FROM ubuntu:latest

# prep system
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git
# ideally we would commit the above as a base image for faster builds
RUN pip3 install flask
RUN git clone https://github.com/meantheory/rpn /var/rpn

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/rpn
EXPOSE 5000
CMD ["python3", "api.py"]
