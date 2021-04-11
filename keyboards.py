from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

'''LANGUAGE'''
language_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    'Русский язык', "O'zbek tili")

'''Russian'''

"""URL"""
rate_url_keyboard = InlineKeyboardMarkup()
rate_url_keyboard.add(InlineKeyboardButton("Тарифные планы.", url='http://skyline.uz/internet'))

about_us_keyboard = InlineKeyboardMarkup()
about_us_keyboard.add(InlineKeyboardButton("Наш сайт", url='http://skyline.uz/'))
about_us_keyboard.add(InlineKeyboardButton("Вотпросы и ответы.", url='http://skyline.uz/faq'))
about_us_keyboard.add(InlineKeyboardButton('Оплата', url='http://skyline.uz/payment'))
about_us_keyboard.add(InlineKeyboardButton("Хотите пообщаться с нами?\nПриезжайте к нам в офис:",
                                           url='http://skyline.uz/contact'))
about_us_keyboard.add(InlineKeyboardButton('Новости компании', url='http://skyline.uz/category/news'))

"""BUTTONS"""
other_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    'Подключение', 'Тарифы'
).add(
    'Связь', 'О нас'
).add(
    'Выбрать язык.'
)

connection_button = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
).add(
    KeyboardButton('Назад 🔙')
)



'''Uzbek'''

"""URL"""
uz_rate_url = InlineKeyboardMarkup()
uz_rate_url.add(InlineKeyboardButton("Tarif rejalari.", url='http://skyline.uz/internet'))

uz_about_us = InlineKeyboardMarkup()
uz_about_us.add(InlineKeyboardButton("Bizning sayt.", url='http://skyline.uz/'))
uz_about_us.add(InlineKeyboardButton("Savol va javoblar.", url='http://skyline.uz/faq'))
uz_about_us.add(InlineKeyboardButton("To'lov", url='http://skyline.uz/payment'))
uz_about_us.add(InlineKeyboardButton("Biz bilan muloqot qilishni xohlaysizmi?\nOfisimizga keling:",
                                     url='http://skyline.uz/contact'))
uz_about_us.add(InlineKeyboardButton('Kompaniya yangiliklari', url='http://skyline.uz/category/news'))

"""BUTTONS"""
uz_button_other = ReplyKeyboardMarkup(resize_keyboard=True).add(
    'Ulanish', 'Tariflar'
).add(
    'Aloqa', 'Biz haqimizda'
).add(
    'Tilni tanlash.'
)

uz_button_connection = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Kontaktingizni yuboring ☎️', request_contact=True)
).add(
    KeyboardButton('Joyingizni yuborish 🗺️', request_location=True)
).add(
    KeyboardButton('Orqaga 🔙')
)
