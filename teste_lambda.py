# importar as bibliotecas
import os
import tweepy
from io import BytesIO
import boto3
import pandas as pd

# Setar as sua credenciasis
api_key = os.environ['API_Key']
API_Key_Secret = os.environ['API_Key_Secret']
Bearer_Token = os.environ['Bearer_Token']
Access_Token = os.environ['Access_Token']
Access_Token_Secret = os.environ['Access_Token_Secret']
aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']


# Autenticar suas credenciais
auth = tweepy.OAuthHandler(api_key, API_Key_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)


# create API object
api = tweepy.API(auth)

termo = "Python"

bucket_name = ''
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)


tweets = tweepy.Cursor(api.search_tweets, q=termo).items(1000)

lista_tweets = []

for tweet in tweets:
    lista_tweets.append(
        [tweet.id_str, tweet.created_at, tweet.text, tweet.lang])

df_tweets = pd.DataFrame(lista_tweets, columns=[
                         "id", "data_criacao", "texto", "Linguagem"])

s3.upload_fileobj(df_tweets.to_json(
    'test43.json', orient='records'), bucket_name)
