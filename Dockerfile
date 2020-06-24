FROM python:3.7

COPY requirements.txt /opt/app/requirements.txt

COPY . /app



WORKDIR    /opt/oracle
RUN        apt-get update && apt install -y libaio1 wget unzip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
            && unzip instantclient-basiclite-linuxx64.zip \
            && rm -f instantclient-basiclite-linuxx64.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig
        

WORKDIR /app
COPY . /app

RUN  pip install --upgrade pip --no-cache-dir -r requirements.txt 


ENTRYPOINT ["python"]

CMD ["src/run.py"]