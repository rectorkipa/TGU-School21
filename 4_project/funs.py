import requests
import json
import telebot

# инициализация бота:
token = '5926670172:AAFc7vMZurJiSEuYp_dEK2MMHJgoa6EwSm4'
bot = telebot.TeleBot(token)

# создание класса:
class Funs:
    def __init__(self, url: str):
        self.url = url

    # создание методов класса:
    def get_dog(self):
        response = requests.get(f'{self.url}')
        data = json.loads(response.text)
        return data['url']

    def get_quote(self):
        response = requests.get(f'{self.url}')
        data = json.loads(response.text)
        return f"Рандомная цитата: {data[0]['quote']} \nЕё автор: {data[0]['author']}."

    def get_answer(self):
        response = requests.get(f'{self.url}')
        data = json.loads(response.text)
        return f"Ответ на твой вопрос: {data['answer']} \n {data['image']}."

    def get_no_answer(self):
        return f"Такой команды нет. \nЯ могу показать собачку, цитату или ответ. Для этого используй команды: \n/dog - увидишь милую собачонку \n/quote - прочитаешь умную цитату \n/answer - получишь ответ на самый сокровенный вопрос"


# handler для старта бота:
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Заскучал? Используй команды, чтобы поразвлечься: \n"
                          "/dog - увидишь милую собачонку \n"
                          "/quote - прочитаешь умную цитату \n"
                          "/answer - получишь ответ на самый сокровенный вопрос")

# handler для создания экземпляра класса и вывода собаки:
@bot.message_handler(commands=['dog'])
def send_dog(message):
    if __name__ == '__main__':
        # создание экземпляра класса:
        dog = Funs(url='https://random.dog/woof.json')
        bot.send_message(message.chat.id, dog.get_dog())

# handler для создания экземпляра класса и вывода цитаты:
@bot.message_handler(commands=['quote'])
def send_quote(message):
    if __name__ == '__main__':
        # создание экземпляра класса:
        quote = Funs(url='https://strangerthings-quotes.vercel.app/api/quotes')
        bot.send_message(message.chat.id, quote.get_quote())

# handler для создания экземпляра класса и вывода ответа:
@bot.message_handler(commands=['answer'])
def send_answer(message):
    if __name__ == '__main__':
        # создание экземпляра класса:
        answer = Funs(url='https://yesno.wtf/api')
        bot.send_message(message.chat.id, answer.get_answer())

@bot.message_handler()
def send_no_answer(message):
    if __name__ == '__main__':
        no_answer = Funs(url=None)
        bot.send_message(message.chat.id, no_answer.get_no_answer())


bot.infinity_polling()