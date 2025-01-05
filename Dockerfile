FROM ghcr.io/dmpatel0/neptune-amd64:1.1

WORKDIR /usr/neptune
 
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "./src/run.py"]