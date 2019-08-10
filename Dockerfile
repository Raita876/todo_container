FROM python:3.7

WORKDIR /usr/src/app

RUN pip install pipenv

COPY . .
RUN pipenv install --deploy --system

CMD [ "python", "-m", "todo" ]
