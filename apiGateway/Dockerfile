FROM    ubuntu
RUN     apt -y -q update && apt -y -q install python3 python3-pip
COPY    . /api-gateway
WORKDIR /api-gateway
RUN     pip3 install -r requirements.txt
EXPOSE  8000/tcp
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]