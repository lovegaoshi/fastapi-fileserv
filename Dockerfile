FROM python:3.10.9
RUN pip install "fastapi[all]"
WORKDIR /fastapi