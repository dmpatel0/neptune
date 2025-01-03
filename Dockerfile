FROM ghcr.io/dmpatel0/neptune-base-fix:0.1

WORKDIR /usr/neptune

COPY requirements.txt ./
COPY ta-lib ./
COPY compile-ta-lib.sh ./

RUN chmod +x ./compile-ta-lib.sh && ./compile-ta-lib.sh

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "./src/run.py"]