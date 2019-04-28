FROM python:3.7.2

ADD requirements.txt / 
# "cashing"
RUN pip install -r requirements.txt
ADD . /
EXPOSE 5000

CMD [ "python", "./server.py" ]