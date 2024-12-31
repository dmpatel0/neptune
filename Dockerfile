FROM --platform=$BUILDPLATFORM dmpatel0/neptune-base:latest

WORKDIR /usr/neptune

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "./run.py"]