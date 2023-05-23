from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN_API = "Your token"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/sticker')
b3 = KeyboardButton('/photo')
kb.add(b1).insert(b2).add(b3)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton('Button 1',
                           url='Your url')

ib2 = InlineKeyboardButton('Button 2',
                           url='Your url')

ikb.add(ib1, ib2)

HELP_COMMAND = """
/help - list of commands
/start - start 
/sticker - get sticker
/photo
/sticker_id
"""


async def on_startup(_):
    print('Successful')


@dp.message_handler(commands=['start'])
async def sent_ikb(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Hi',
                           reply_markup=ikb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           HELP_COMMAND)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>Your</em> <b>text</b >',
                         "HTML",
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['sticker'])
async def sticker_command(message: types.Message):
    await message.answer('funny kitty')
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEJETNkbGveJ8nLOgMrCyZEBPkoGvJ0ZgACYBEAAjyzxQdl_6z44-FZCi8E")


@dp.message_handler()
async def count(message: types.Message):
    if 'Я'.lower() in message.text:
        await message.reply(message.text + '🫵')
        await message.answer(text=str(message.text.count('Я'.lower())))


@dp.message_handler(content_types=['sticker_id'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHfQfXQD-FhEfRlBCrWZiLi5PMIYWLRr2d6A&usqp=CAU')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
