FROM python:3.13
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src /app/src
COPY tests /app/tests
ENV PYTHONPATH=/app/src
CMD ["bash", "-i"]