FROM --platform=$BUILDPLATFORM dmpatel0/neptune-base:1.4 AS build

WORKDIR /usr/neptune

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "./src/run.py"]