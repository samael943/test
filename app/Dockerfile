FROM ubuntu:18.04

ADD . /
EXPOSE 80

WORKDIR [ "/etc/ansible" ]
CMD [ "ansible-playbook", "apache.yml" ]
