FROM python:3

COPY Projet_Flask/mnist_model.zip /src/
RUN cd /src && unzip mnist_model.zip

COPY Projet_Flask/requirements.txt /src/
RUN pip install -r /src/requirements.txt

COPY Projet_Flask /src

WORKDIR /src
CMD python3 /src/script_app.py
