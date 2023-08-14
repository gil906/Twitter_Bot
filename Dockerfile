FROM python:3.8-slim

WORKDIR /app

COPY twitter_bot.py /app

RUN pip install tweepy

CMD ["python", "twitter_bot.py"]
