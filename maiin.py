import logging
from aiogram import Bot, Dispatcher, executor, types
from buttoonse import menyu, menyu_next, menyu_set,menyu_trendvich,menyu_burger,menyu_hotdog

API_TOKEN = '7398915271:AAFTn9lTbLG1fWZFmX-GGcMujREiQs8xDfs'
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(f'Assalomu alekum {msg.from_user.full_name}', reply_markup=menyu)



@dp.message_handler(text='Bosh menyuga qaytish')
async def b_m(msg: types.Message):
    await msg.answer("Setlar bo'limiga kirdingz!", reply_markup=menyu)


@dp.message_handler(text='Qaytish')
async def i_m(msg: types.Message):
    await msg.answer("Setlar bo'limiga kirdingz!", reply_markup=menyu_next)


@dp.message_handler(text='Menyu')
async def menyu_n(msg: types.Message):
    await msg.answer("Quyidagilardan birini tanlang!", reply_markup=menyu_next)


@dp.message_handler(text='Setlar(8)')
async def menyu_s(msg: types.Message):
    await msg.answer("Setlar bo'limiga kirdingz!", reply_markup=menyu_set)



@dp.message_handler(text='Trendvich')
async def menyu_s(msg: types.Message):
    await msg.answer("trendvich bo'limiga kirdingz!", reply_markup=menyu_trendvich)


@dp.message_handler(text='Burgerlar')
async def menyu_s(msg: types.Message):
    await msg.answer("Burger bo'limiga kirdingz!", reply_markup=menyu_burger)

@dp.message_handler(text='Hotdog')
async def menyu_s(msg: types.Message):
    await msg.answer("Hotdog bo'limiga kirdingz!", reply_markup=menyu_hotdog)


@dp.message_handler(text='standart hotdog')
async def hotdog(msg: types.Message):
    url = 'https://media.express24.uz/r/600/600/uutvd1Znw7xPURMIA4ebu.jpg'
    text = """
Narxi: 12 000
Dastavka: Bor (30 000)
"""
@dp.message_handler(text='mini hotdog')
async def hotdog(msg: types.Message):
    url = 'https://media.express24.uz/r/600/600/uutvd1Znw7xPURMIA4ebu.jpg'
    text = """
Narxi: 12 000
Dastavka: Bor (30 000)
"""
@dp.message_handler(text='standart hotdog')
async def hotdog(msg: types.Message):
    url = 'https://media.express24.uz/r/600/600/uutvd1Znw7xPURMIA4ebu.jpg'
    text = """
Narxi: 12 000
Dastavka: Bor (30 000)
"""
@dp.message_handler(text='standart hotdog')
async def hotdog(msg: types.Message):
    url = 'https://media.express24.uz/r/600/600/uutvd1Znw7xPURMIA4ebu.jpg'
    text = """
Narxi: 12 000
Dastavka: Bor (30 000)
"""
    await bot.send_photo(msg.chat.id, photo=url, caption=text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)