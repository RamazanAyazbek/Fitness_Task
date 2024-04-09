FROM python:3.10.2

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
VOLUME /app/cache

CMD ["python3", "manage.py",  "runserver", "0.0.0.0:8000", "--noreload"  ]


