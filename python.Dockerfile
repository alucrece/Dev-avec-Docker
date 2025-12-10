FROM python:3.9
WORKDIR /server
COPY requirements.txt .
RUN pip install mysql-connector-python fastapi uvicorn
EXPOSE 8000