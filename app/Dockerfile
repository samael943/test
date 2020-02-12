FROM ubuntu:18.04
FROM ansible

ADD . /
EXPOSE 80

WORKDIR [ "/etc/ansible" ]
CMD [ "ansible-playbook", "apache.yml" ]
