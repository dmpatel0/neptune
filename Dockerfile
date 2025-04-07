FROM debian:12

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
    apt-utils \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    git \
    build-essential \
    autoconf \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY install-odbc-driver.sh /tmp/install-odbc-driver.sh

RUN chmod +x /tmp/install-odbc-driver.sh && /tmp/install-odbc-driver.sh && rm /tmp/install-odbc-driver.sh

# Install TA-Lib using the .deb package
RUN curl -L -o ta-lib_0.6.4_amd64.deb https://github.com/ta-lib/ta-lib/releases/download/v0.6.4/ta-lib%5F0.6.4%5Famd64.deb && \
    dpkg -i ta-lib_0.6.4_amd64.deb && \
    rm ta-lib_0.6.4_amd64.deb 

RUN python3 -m venv /venv

WORKDIR /neptune

COPY requirements.txt /neptune/

RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

COPY ./ /neptune

EXPOSE 5000

CMD ["/venv/bin/python3", "src/run.py"]