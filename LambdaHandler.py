# import tweepy

# consumer_key = 'sua_consumer_key'
# consumer_secret = 'seu_consumer_secret'
# access_token = 'seu_access_token'
# access_token_secret = 'seu_access_token_secret'

# # Autenticando com o Tweepy
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# # Conectando com a API do Twitter
# api = tweepy.API(auth)

# # Exemplo de uso da API
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


# import tweepy

# consumer_key = 'xxxx'
# consumer_secret = 'xxxxxx'
# access_token = 'xxxx'
# access_token_secret = 'xxxxx'

# # Autenticando com o Tweepy
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# # Conectando com a API do Twitter
# api = tweepy.API(auth)

# # Verificando se a autenticação foi bem sucedida
# try:
#     api.verify_credentials()
#     print("Autenticação com a API do Twitter realizada com sucesso!")
# except Exception as e:
#     print("Erro ao autenticar com a API do Twitter:", e)
