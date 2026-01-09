FROM python:3.9
RUN addgroup --system appgroup && adduser --system --group appuser
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chown -R appuser:appgroup /server
USER appuser
EXPOSE 8000