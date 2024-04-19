import telebot

bot = telebot.TeleBot("6931674584:AAHgkAMQX-gjlu3li41zSTJE_1yXWIR4CwA")

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Hello!")
    
bot.polling(non_stop = True)