import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, ChatMemberAdministrator
from pyrogram.types import ChatMember
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6152705166:AAHxW-N8PyDC50D1PDeGJ006UsHSp0E2TtI'
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
     await message.reply("Привет!\nЯ существую для того, чтобы ты изучал Python!\nТеперь ты админ чата!")
     await bot.promote_chat_member(-1001888602510, f'{message.from_user.id}', can_pin_messages=True)

@dp.message_handler(commands=["name"])
async def name(message: types.Message, command):
    if command.args:
        await bot.promote_chat_member(-1001872014144, message.from_user.id, can_pin_messages=True)
        await bot.set_chat_administrator_custom_title(-1001872014144, message.from_user.id, command.args)
        await message.answer(f"Привет, <b>{command.args}</b>")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
