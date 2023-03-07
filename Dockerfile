FROM python:3.10-slim

COPY . .

RUN pip3 install -r requirements.txt
CMD ["sh", "/game/make.sh"]

CMD [ "python3.10", "/console.py" ]