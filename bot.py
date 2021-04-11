from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    await message.reply("Здравствуйте. Выберите язык.\nAsslomu alaykum. Tilni tanlang.",
                        reply_markup=kb.language_button)


'''Russian'''

@dp.message_handler()
async def process(message: types.Message):
    if message.text == 'Русский язык':
        await bot.send_message(message.chat.id, 'Выберите пункт ↩️.', reply_markup=kb.other_button)

    elif message.text == 'Подключение':
        await bot.send_message(message.chat.id,
                               "Запрашиваем Контакт и Геолокацию, для уточнение есть ли возможность подключения по "
                               "вашему адресу. В скором времени вам ответят либо свяжутся!",
                               reply_markup=kb.connection_button)

    elif message.text == 'Тарифы':
        await bot.send_message(message.chat.id, "С тарифным планом вы можете ознакомиться тут ↩️.",
                               reply_markup=kb.rate_url_keyboard)

    elif message.text == 'Связь':
        await bot.send_message(message.chat.id, "Номер тех. поддержки:\n+998 78 113 60 01\nНомер бухгалтерии:\n"
                                                "+998 78 113 63 13\nНаш Telegram: @skyline_support")

    elif message.text == 'О нас':
        await bot.send_message(message.chat.id, "Подробная информация в разделе ниже ↩️.",
                               reply_markup=kb.about_us_keyboard)

    elif message.text == "Выбрать язык.":
        await bot.send_message(message.chat.id, 'Выберите язык.\nTilni tanlang.',
                               reply_markup=kb.language_button)

    elif message.text == 'Назад 🔙':
        await bot.send_message(message.chat.id, 'Главное меню.', reply_markup=kb.other_button)

    elif message.text == text():
        await bot.send_message(message.chat.id, 'Выберите один пункт', reply_markup=kb.other_button)







    '''Uzbek'''

    if message.text == "O'zbek tili":
        await bot.send_message(message.chat.id, "Ob'ektni tanlang ↩️.", reply_markup=kb.uz_button_other)

    elif message.text == 'Ulanish':
        await bot.send_message(message.chat.id,
                               "Telefon raqam va geolokatsiyani so'rayabmiz, manzilingizda ulanish imkoniyati "
                               "mavjudligini aniqlashimiz uchun. Tez orada javob beramiz yoki bog'lanamiz!",
                               reply_markup=kb.uz_button_connection)

    elif message.text == 'Tariflar':
        await bot.send_message(message.chat.id, "Tarif rejasi bilan bu yerda tanishishingiz mumkin ↩️.",
                               reply_markup=kb.uz_rate_url)

    elif message.text == 'Aloqa':
        await bot.send_message(message.chat.id, "Texnik yordam raqami:\n+998 78 113 60 01\nBuxgalteriya raqami:\n+998 "
                                                "78 "
                                                "113 63 13\nBizning Telegram: @skyline_support")

    elif message.text == 'Biz haqimizda':
        await bot.send_message(message.chat.id, "Quyidagi bo'limda batafsil ma'lumot ↩️.",
                               reply_markup=kb.uz_about_us)

    elif message.text == "Tilni tanlash.":
        await bot.send_message(message.chat.id, 'Выберите язык.\nTilni tanlang.',
                               reply_markup=kb.language_button)

    elif message.text == 'Orqaga 🔙':
        await bot.send_message(message.chat.id, 'Asosiy menyu.', reply_markup=kb.uz_button_other)















if __name__ == '__main__':
    executor.start_polling(dp)
