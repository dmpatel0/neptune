FROM ghcr.io/dmpatel0/neptune-base:1.1

WORKDIR /usr/neptune

#COPY ta-lib ./
#COPY compile-ta-lib.sh ./
#RUN chmod +x compile-ta-lib.sh && ./compile-ta-lib.sh

#COPY install-odbc-driver.sh ./

#RUN chmod +x ./install-odbc-driver.sh && ./install-odbc-driver.sh

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "src/run.py"]