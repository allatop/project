import telebot
from telebot import types

bot = telebot.TeleBot('6873182878:AAEx2qzNaAuRk9s470AygQdyhXn-m-I0qVs')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn2 = types.KeyboardButton('Расписание занятий')
    btn3 = types.KeyboardButton('СДО',)
    btn4 = types.KeyboardButton('Учебный план')
    markup.row(btn2, btn3, btn4)
    btn5 = types.KeyboardButton('Контакты тьютора')
    btn6 = types.KeyboardButton('Приемная комиссия')
    btn7 = types.KeyboardButton('Электронная библиотека')
    markup.row(btn5, btn6, btn7)
    btn8 = types.KeyboardButton('Деканат Факультета')
    btn9 = types.KeyboardButton('Единый деканат')
    btn10 = types.KeyboardButton('Техническая поддержка')
    markup.row(btn8, btn9, btn10)
    btn11 = types.KeyboardButton('Задать вопрос Приемногй комиссии')
    btn12 = types.KeyboardButton('Студенческие кадры' )
    #btn13 = types.KeyboardButton('Службы социального обеспечения'))
    markup.row(btn11, btn12)

    bot.send_message(message.chat.id, 'Это бот сетевой магистратуры МИИГАиК - тут есть ответы на вопросы которые вас интересуют.' '\n' '\n'
                     'По вопросам пересдач, ВКР и общих, касающихся учебных процессов, обращайтесь в <b>деканат факультета</b>.' '\n' '\n'
                     'Если вам нужно заказать справку об обучении в вузе, написать заявление на академический отпуск или на отчисление, то обращайтесь в <b>Единый деканат</b>.' '\n' '\n'
                     'По вопросам получения диплома и возврата документов, подаваемых при поступлении, обращайтесь в <b>студенческий отдел кадров</b>.' '\n' '\n'
                     'Если вам потребовалось изменить почту, получить доступ к СДО или возникли другие технические трудности, обращайтесь в <b>техническую поддержку</b>.' '\n' '\n'
                     'По вопросам поступления, восстановления в вуз, обращайтесь в <b>Приемную комиссию</b>.' '\n' '\n'
                     'Если вы не нашли, к кому обратиться со своим вопросом, то <b>тьютор</b> поможет вам найти ответ.', reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Расписание занятий':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Расписание','https://schedule.miigaik.ru/'))
        bot.reply_to(message, 'Перейдите по ссылке:', reply_markup=markup )

    elif message.text == 'СДО':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('СДО', 'https://sdo.miigaik.ru/local/crw/index.php'))
        bot.reply_to(message, 'Перейдите по ссылке:', reply_markup=markup)

    elif message.text == 'Учебный план':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Учебный план', 'https://www.miigaik.ru/education/study-plans/'))
        bot.reply_to(message, 'Перейдите по ссылке:', reply_markup=markup)

    elif message.text == 'Электронная библиотека':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Электронная библиотека', 'https://www.miigaik.ru/library/'))
        bot.reply_to(message, 'Перейдите по ссылке:', reply_markup=markup)

    elif message.text == 'Задать вопрос Приемной комиссии':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Задать вопрос', 'https://www.miigaik.ru/Abitur/question/'))
        bot.reply_to(message, 'Перейдите по ссылке:', reply_markup=markup)

    elif message.text == 'Приемная комиссия':
        bot.reply_to(message, 'Приемная комиссия:' '\n' 'Номер телефона - 8(499) 267-15-45' '\n' 'Почта - pk@miigaik.ru' '\n' 'Время работы: пн-пт с 10:00 по 18:00, сб-вс выходные. Обед с 13:00 по 14:00')

    elif message.text == 'Единый деканат':
        bot.reply_to(message, 'Единый деканат:' '\n' 'Номер телефона -  8(499) 267-35-40' '\n' 'Почта - e_dekanat@miigaik.ru' '\n' 'Время работы: пн-пт с 10:00 по 18:00, сб-вс выходные. Обед с 13:00 по 14:00')

    elif message.text == 'Студенческие кадры':
        bot.reply_to(message,'Студенческие кадры:' '\n' 'Номер телефона -  8(499) 261-19-98' '\n' 'Почта - uk@miigaik.ru' '\n' 'Время работы: пн-пт с 10:00 по 18:00, сб-вс выходные. Обед с 13:00 по 14:00')

    # elif message.text == 'Службы социального обеспечения':
    #     markup = types.InlineKeyboardMarkup()
    #     markup.add(types.InlineKeyboardButton('Службы социального обеспечения', 'https://www.miigaik.ru/students/social- security-service/'))
    #     bot.reply_to(message, 'Перейдите по ссылке:', reply_markup=markup)

    elif message.text == 'Контакты тьютора':
        bot.reply_to(message,'Контакты тьютора (Белых Анастасия Дмитриевна):'  '\n' 'Почта -  sm@miigaik.ru' '\n' 'Телеграм -  @ya_mooha, @bb_sonya' '\n' 'Время работы: пн-пт с 10:00 по 18:00, сб-вс выходные. Обед с 13:00 по 14:00')

    elif message.text == 'Техническая поддержка':
        bot.reply_to(message,'Поддержка пользователей:'  '\n' 'Почта -  support@edu.miigaik.ru' '\n' 'Техническая поддержка СДО:' '\n' 'Почта -  eee@miigaik.ru' '\n' 'Время работы: пн-пт с 10:00 по 18:00, сб-вс выходные. Обед с 13:00 по 14:00')

    elif message.text == 'Деканат Факультета':
        bot.reply_to(message,'ФУТ'  '\n' 'Почта -  feut@feut.ru' '\n' 'Номер телефона - 8(499) 404-12-20 добавочные цифры 2510' '\n' '\n' 
                             'ФГиИБ'  '\n' 'Почта -  gis_faculty@miigaik.ru' '\n' 'Номер телефона - 8(499) 404-12-20 добавочные цифры 2310' '\n' '\n'
                            'КФ'  '\n' 'Почта -  kartfak@miigaik.ru' '\n' 'Номер телефона - 8(499) 404-12-20 добавочные цифры 2210' '\n' '\n'
                             'ГФ'  '\n' 'Почта -  geofak@miigaik.ru' '\n' 'Номер телефона - 8(499) 404-12-20 добавочные цифры 2110' '\n' '\n'
                             'Время работы: пн-пт с 10:00 по 18:00, сб-вс выходные. Обед с 13:00 по 14:00')

    bot.register_next_step_handler(message, on_click)

bot.polling(none_stop=True)

