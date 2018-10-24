FROM python:3.6

ADD . /backend
WORKDIR /backend

RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["oisapi.py"]
