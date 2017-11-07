FROM python:2
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "main.py"]
