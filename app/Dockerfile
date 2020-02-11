FROM python:3.7.2

ADD . /
EXPOSE 80

WORKDIR [ "/etc/ansible" ]
CMD [ "ansible-playbook", "apache.yml" ]
