FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./bin/entrypoint.sh

ENTRYPOINT [ "./bin/entrypoint.sh" ]