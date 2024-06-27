import telebot
from telebot import types

# Токен твоего бота, полученный от BotFather
bot_token = '7437632107:AAHJGor9v3SYaK04redoD-RcBVCA0U83PiE'

# Создаем объект бота
bot = telebot.TeleBot(bot_token)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_id(message):
    user_id = message.chat.id

    # Отправляем дополнительное сообщение
    additional_message = (
        "Join the Elite Escort Agency - INTER MAN! 🌟\n\n"
        "Are you looking for a job that brings not only income but also pleasure? "
        "Want to be part of a professional team and offer high-class services? Then you are in the right place! 💼\n\n"
        "Who are we?\n\n"
        "INTER MAN AGENCY is a leading company in the men's escort services industry in the World. "
        "We provide our clients with unique and unforgettable experiences, combining elegance, style, and professionalism. ✨\n\n"
        "Who are we looking for?\n\n"
        "We are looking for confident, charming, and cultured men aged 21 to 35 who:\n\n"
        "- Have an attractive appearance and well-groomed look. 💇‍♂️\n"
        "- Can engage in conversation on various topics. 🗣\n"
        "- Are proficient in English and other languages (a plus). 🌍\n"
        "- Are responsible and punctual. ⏰\n"
        "- Are ready to maintain a high level of confidentiality and professionalism. 🔒\n\n"
        "What do we offer?\n\n"
        "- High income and flexible working hours. 💸\n"
        "- A steady stream of clients and stable earnings. 🔄\n"
        "- Working in a team of professionals and career growth opportunities. 📈\n"
        "- Training and support at all stages of work. 📚\n"
        "- Safety and confidentiality. 🛡"
    )

    bot.send_message(message.chat.id, additional_message)

    # Создаем клавиатуру с кнопкой
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="SEND MESSAGE", url="https://t.me/llllBLACKllll")
    keyboard.add(url_button)

    # Текст перед кнопкой
    message_text = (
        "If you are confident in your abilities and want to try yourself as a professional escort specialist, and to earn from 2000$ to 10000$ "
        "send a message to our manager at @llllBLACKllll or press the button \"SEND MESSAGE\" 💬\n\n"
        "Become a part of INTER MAN AGENCY and start earning today! 💸"
    )

    bot.send_message(message.chat.id, message_text, reply_markup=keyboard)

# Запускаем бота
bot.polling()
