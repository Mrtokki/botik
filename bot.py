import telebot
from telebot import types

token = "5101703536:AAFLOKNDo3WRKLgh7bWTxS6eurd6SH4u2gM"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    keyboardmain = types.InlineKeyboardMarkup()
    item =  types.InlineKeyboardButton(text="Заказать ПК😌", callback_data="Заказать ПК")
    item2 = types.InlineKeyboardButton(text="Уточнить по заказу😉", callback_data="Уточнить")
    item3 = types.InlineKeyboardButton(text="Спросить🤔", callback_data="Спросить")
    item4 = types.InlineKeyboardButton(text="Контакты😌", callback_data="Контакты")
    keyboardmain.add(item, item3, item4, item2)
    bot.reply_to(message, 'Приветствуем🥰, ' + message.from_user.first_name, reply_markup=keyboardmain)
    
## Контакты
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
   if call.message:
    if call.data in "Контакты":
        keyboardmain = types.InlineKeyboardMarkup()
        second_button12 = types.InlineKeyboardButton(text="VK", url="https://vk.com/write-146666669")
        second_button22 = types.InlineKeyboardButton(text="WhatsApp", url="https://wa.me/79301113355")
        second_button23 = types.InlineKeyboardButton(text="Назад", callback_data="Назад2")
        keyboardmain.add(second_button12, second_button22, second_button23)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Куда удобней написать?",reply_markup=keyboardmain)
                
    elif call.data == "VK":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id)
       
    elif call.data == "Уточнить":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Подготовьте номер заказа, с вами свяжуться")
    elif call.data == "Спросить":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Напишите ваш вопрос")
        
    elif call.data == "Назад2":
       keyboardmain = types.InlineKeyboardMarkup()
       item24 = types.InlineKeyboardButton(text="Заказать ПК😌", callback_data="Заказать ПК")
       item25 = types.InlineKeyboardButton(text="Уточнить по заказу😉", callback_data="Уточнить")
       item26 = types.InlineKeyboardButton(text="Спросить🤔", callback_data="Спросить")
       item27 = types.InlineKeyboardButton(text="Контакты😌", callback_data="Контакты")
       keyboardmain.add(item24, item25, item26, item27)
       bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Приветствуем🥰)",reply_markup=keyboardmain)     
            
    elif call.data == "Заказать ПК":    
        keyboardmain = types.InlineKeyboardMarkup()
        first_button = types.InlineKeyboardButton(text="PLUTO X", callback_data="pluto")
        second_button = types.InlineKeyboardButton(text="MERCURY", callback_data="mercury")
        second_button2 = types.InlineKeyboardButton(text="MARS", callback_data="Марс")
        second_button3 = types.InlineKeyboardButton(text="EARTH", callback_data="earth")
        second_button4 = types.InlineKeyboardButton(text="CALLISTO", callback_data="callisto")
        second_button5 = types.InlineKeyboardButton(text="BELKA 1960", callback_data="belka")
        Далее = types.InlineKeyboardButton(text="Далее", callback_data="Далее")
        second_button7 = types.InlineKeyboardButton(text="STRELKA 1960", callback_data="strelka")
        second_button8 = types.InlineKeyboardButton(text="ANDROMEDA", callback_data="andromeda")
        second_button9 = types.InlineKeyboardButton(text="SIMULATION", callback_data="simulation")
        second_button10 = types.InlineKeyboardButton(text="FERMI PARADOX", callback_data="fermi")
        second_button11 = types.InlineKeyboardButton(text="HALLEY'S COMET", callback_data="comet")
        keyboardmain.add(first_button, second_button, second_button2, second_button3, second_button4, second_button5, second_button7, second_button8, second_button9, second_button10, second_button11, Далее)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выбирай",reply_markup=keyboardmain)
        
    elif call.data == "Далее":
        keyboardmain = types.InlineKeyboardMarkup()
        first_button13 = types.InlineKeyboardButton(text="THOMAS YOUNG 1801", callback_data="thomas")
        second_button13 = types.InlineKeyboardButton(text="Индивидуальный", callback_data="Индивид")
        Назад = types.InlineKeyboardButton(text="Назад", callback_data="Назад")
        keyboardmain.add(first_button13, second_button13, Назад)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выбирай",reply_markup=keyboardmain) 
                   

    elif call.data == "pluto":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер")
        
    elif call.data == "mercury":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер")
        
    elif call.data == "earth":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)      
    
    elif call.data == "Марс":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)
        
    elif call.data == "callisto":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)   
        
    elif call.data == "belka":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)
        
    elif call.data == "strelka":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)       
        
    elif call.data == "andromeda":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)   
        
    elif call.data == "simulation":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)
        
    elif call.data == "fermi":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)   
     
    elif call.data == "comet":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)
        
    elif call.data == "thomas":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)
        
    elif call.data == "Индивид":
        keyboard = types.InlineKeyboardMarkup()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Ваш заказ принят, с вами свяжеться менеджер",reply_markup=keyboard)
        
    elif call.data == "Назад":    
        keyboardmain = types.InlineKeyboardMarkup()
        first_button = types.InlineKeyboardButton(text="PLUTO X", callback_data="pluto")
        second_button = types.InlineKeyboardButton(text="MERCURY", callback_data="mercury")
        second_button2 = types.InlineKeyboardButton(text="MARS", callback_data="Марс")
        second_button3 = types.InlineKeyboardButton(text="EARTH", callback_data="earth")
        second_button4 = types.InlineKeyboardButton(text="CALLISTO", callback_data="callisto")
        second_button5 = types.InlineKeyboardButton(text="BELKA 1960", callback_data="belka")
        Далее = types.InlineKeyboardButton(text="Далее", callback_data="Далее")
        second_button7 = types.InlineKeyboardButton(text="STRELKA 1960", callback_data="strelka")
        second_button8 = types.InlineKeyboardButton(text="ANDROMEDA", callback_data="andromeda")
        second_button9 = types.InlineKeyboardButton(text="SIMULATION", callback_data="simulation")
        second_button10 = types.InlineKeyboardButton(text="FERMI PARADOX", callback_data="fermi")
        second_button11 = types.InlineKeyboardButton(text="HALLEY'S COMET", callback_data="comet")
        keyboardmain.add(first_button, second_button, second_button2, second_button3, second_button4, second_button5, second_button7, second_button8, second_button9, second_button10, second_button11, Далее)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выбирай",reply_markup=keyboardmain)        
           
     #elif call.data   
        


if __name__ == "__main__":
        bot.remove_webhook()
        bot.polling(none_stop=True)
        bot.delete_webhook()
