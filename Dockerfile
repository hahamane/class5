FROM ubuntu:16.04
MAINTAINER Dae Hun Park
RUN mkdir -p /home/work/
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install numpy pandas
RUN pip3 install sklearn
RUN pip3 install plotly
RUN pip3 install statsmodels
RUN pip3 install matplotlib

