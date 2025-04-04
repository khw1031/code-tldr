ARG BUILD_URL
FROM ${BUILD_URL}:python3.11

WORKDIR /devops-api-code-review
COPY . .
RUN pip install -r requirements.txt

EXPOSE 15000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=15000"]