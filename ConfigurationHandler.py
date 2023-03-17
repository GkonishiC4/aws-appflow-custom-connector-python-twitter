import tweepy
import pandas as pd

API_Key = 'xxxx'
API_Key_Secret = 'xxxxx'
Bearer_Token = 'xxxxxx'
Access_Token = 'xxxx-xxxxx'
Access_Token_Secret = 'xxxxxx'

auth = tweepy.OAuthHandler(API_Key, API_Key_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)

api = tweepy.API(auth)

# Verificando se a autenticação foi bem sucedida
try:
    api.verify_credentials()
    print("Autenticação com a API do Twitter realizada com sucesso!")
except Exception as e:
    print("Erro ao autenticar com a API do Twitter:", e)

termo = "Lula"

tweets = tweepy.Cursor(api.search_tweets, q=termo).items(1000)

lista_tweets = []

for tweet in tweets:
    lista_tweets.append(
        [tweet.id_str, tweet.created_at, tweet.text, tweet.lang])

df_tweets = pd.DataFrame(lista_tweets, columns=[
                         "id", "data_criacao", "texto", "Linguagem"])

df_tweets.to_json('test43.json', orient='records')
