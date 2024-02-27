FROM python:3.10-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN echo "Cython<3" > cython_constraint.txt
RUN PIP_CONSTRAINT=cython_constraint.txt pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
