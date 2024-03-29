FROM python:3.12.2-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["chainlit run", "./app.py"]
