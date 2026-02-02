FROM python:3.9
RUN addgroup --system appgroup && adduser --system --group appuser
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chown -R appuser:appgroup /server
USER appuser
CMD ["uvicorn", "postgres-test:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000