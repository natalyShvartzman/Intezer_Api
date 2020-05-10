FROM python:3.6.10
WORKDIR index_words

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY intezer_api .

CMD [ "python", "api_main.py" ]

