FROM python:3.11
RUN pip install flask pycryptodome gunicorn

WORKDIR /app
COPY . .  
EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]