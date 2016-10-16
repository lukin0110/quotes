FROM python:3.5

RUN pip install wheel==0.30.0a0 scrapy==1.2.0
WORKDIR /usr/src/app

ADD python-lib /usr/src/app
ADD python-lib /root/
ADD quotes /usr/src/app/quotes/assets

CMD ["bash"]
