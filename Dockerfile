FROM quay.io/astronomer/ap-airflow:2.2.4-onbuild
USER root
RUN apt-get -y update \
     && apt-get -y autoremove \
     && apt-get clean \
     && apt-get install -y zip
RUN mkdir /opt/oracle
RUN chmod 777 /opt/oracle
USER astro
ADD include/install/instantclient-basic-linux.x64-21.5.0.0.0dbru.zip /opt/oracle
RUN cd /opt/oracle && unzip instantclient-basic-linux.x64-21.5.0.0.0dbru.zip && rm instantclient-basic-linux.x64-21.5.0.0.0dbru.zip
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_5:$LD_LIBRARY_PATH
ENV AIRFLOW_CONN_MY_ORACLE_CONN=oracle://system:oracle@oracle-db:1521
