# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# install
RUN pip install pipenv
ADD Pipfile Pipfile.lock /
RUN pipenv install --system
RUN pipenv install sqlalchemy pymysql fastapi[all] aiomysql

ADD db.py /
ADD app.py /
ADD routers /routers
ADD models /models
ADD schemas /schemas
ADD CRUDs /CRUDs
ADD session /session

EXPOSE 8000
CMD python /app.py