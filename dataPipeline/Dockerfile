FROM    ubuntu
RUN     apt -y -q update && apt -y -q install python3 python3-pip
COPY    . /alpha-vantage
WORKDIR /alpha-vantage
RUN     mkdir logs
RUN     pip3 install -r requirements.txt
EXPOSE  15032/tcp
ENTRYPOINT ["python3", "main.py"]