FROM python:3.5

RUN pip install wheel
WORKDIR /usr/src/app

ADD python-lib /usr/src/app
ADD quotes /usr/src/app/pyquotes/assets
