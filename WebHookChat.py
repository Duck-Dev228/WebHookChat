import os
try:
    from discord import Webhook,RequestsWebhookAdapter
except:
    os.system('pip install discord.py')
from json import load 
from time import sleep
def ReadConfig():
    try:
        with open('Config.json',encoding = 'UTF-8') as config:
            parsedconfig = load(config)
            config.close()
        return parsedconfig
    except:
        exit(-1)

def Main():
    cls = lambda:os.system('cls' if os.name=='nt' else 'clear')
    config = ReadConfig()
    while True:
      name = config['name']
      avatar = config['avatar_url']
      hok = Webhook.from_url(config['webhook_url'],adapter=RequestsWebhookAdapter())
      message = input(f'"{name}" Message : ')
      if len(message) > 1999:
          print("The number of characters in the message should not exceed 2000")
          sleep(500)
      if len(message) < 2000:
          hok.send(message,username=name,avatar_url=avatar)
          cls()
      
if __name__ == "__main__":
    if not os.path.exists('Config.json'):
        o = open('Config.json','w')
        o.write('{\n    "webhook_url":"url",\n    "avatar_url":"https://avatars.mds.yandex.net/get-zen_doc/1906877/pub_5e54e08fe977e25b8eec7a32_5e54e1a4b7ff5817661e7c22/scale_1200",\n    "name":"John"\n}')
        o.close()
        print('Первый запуск произошел успешно\nфайл "Config.json" Создан Пожалуйста внестие в него ваши данные для вебхука')
        sleep(1500)
        exit(1)
    Main()