import telebot
import markups as mk
token = "5579518194:AAFa6MtvYwul7g-cTlsMbJKhFmnDvSPeza0"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def first_message(message):
    bot.send_message(message.chat.id, "*Привет, воллейболист, в данном боте ты получишь море полезной информации про воллейбол!*", parse_mode="Markdown", reply_markup=mk.Main_Reply)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == "АМПЛУА В ВОЛЛЕЙБОЛЕ":
        bot.send_message(message.chat.id, "*ВОТ ПОДБОРКА ВИДЕО ПРО РОЛИ В ВОЛЛЕЙБОЛЕ*", parse_mode="Markdown", reply_markup=mk.Amplua_inline)

    elif message.text == "СХЕМЫ ИГРЫ В ВОЛЛЕЙБОЛ":
        bot.send_message(message.chat.id, "*ВОТ ПОДБОРКА ВИДЕО ПРО СХЕМЫ ИГРЫ В ВОЛЛЕЙБОЛЕ*", parse_mode="Markdown", reply_markup=mk.Scheme_Inline)

    elif message.text == "ПОЛЕЗНАЯ ИНФОРМАЦИЯ":
        bot.send_message(message.chat.id, "*ВОТ ПОЛЕЗНАЯ ИНФОРМАЦИЯ ДЛЯ ВАС*", parse_mode="Markdown", reply_markup=mk.Information_Inline)

    elif message.text == "ВИДЕО - ИГРА В ВОЛЛЕЙБОЛ":
        bot.send_message(message.chat.id, "*ВОТ ВИДЕО С ИГРОЙ В ВОЛЛЕЙБОЛ*", parse_mode="Markdown", reply_markup=mk.Video_Inline)


bot.polling(none_stop=True)