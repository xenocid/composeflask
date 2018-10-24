FROM python:3.6

ADD . /backend
WORKDIR /backend

RUN pip install -r requirements.txt
ENV FLASK_APP oisapi.py
ENV FLASK_ENV development
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["oisapi/oisapi.py"]
