FROM python:2
WORKDIR /opt/

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD election_reminder.py data.json ./

CMD ["python", "election_reminder.py"]
