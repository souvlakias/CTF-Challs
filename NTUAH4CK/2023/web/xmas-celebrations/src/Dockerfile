FROM python:3.11
RUN pip install flask requests

COPY . /app/
WORKDIR /app
EXPOSE 1337

CMD ["python","app.py"]