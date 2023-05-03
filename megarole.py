import random
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hide_link
from aiogram.types import ChatMemberAdministrator
from aiogram.dispatcher.filters import Command
import time
from aiogram.utils.markdown import link
OSKORBLYA = ['всеволод лох','всеволод чмо','всеволод даун','компьютер']






API_TOKEN = '6123767585:AAFct5eGVw2vZC_iJ_FhoQ17yObdw-nJbTI'
bot = Bot(token=API_TOKEN,parse_mode="html")
dp = Dispatcher(bot)
@dp.message_handler(regexp='рофл')
async def joke(message: types.Message):
    await message.answer('что такое рофл??? я знаю только шутки из смешной группы вконтакте')
    time.sleep(3)
    await bot.send_message(message.chat.id, text=(link('ПРИКОЛЫБЕСПЛАНТОРЖАКАХАХАХХА','https://vk.com/channehumor')), parse_mode='Markdown',disable_web_page_preview=True)




@dp.message_handler(text=OSKORBLYA)
async def rude(message: types.Message):
    await message.answer('сам такой(( хнык...')
    time.sleep(1)
    await message.answer('ОТСТАНЬ ОТ МЕНЯ((')
    await message.bot.kick_chat_member(message.from_user.id,30,False)








@dp.message_handler(commands=['btn'])
async def send_welcome(message: types.Message):
    btn = types.KeyboardButton(text="a")
    markup = types.ReplyKeyboardMarkup(row_width=0.5)
    markup.add(btn)
    text = f'я му, {message.from_user.first_name}'
    await message.answer(text, reply_markup=markup)

@dp.message_handler(text='всеволод, расскажи анекдот')
async def cats(message: types.Message):
    kb = ['Что надо сказать негру в униформе?\nМне, пожалуйста, бигмак и колу.',
          'Как напугать негра?\nВзять его с собой на аукцион.']
    rand = random.randint(0,1)
    photo = ['negros.jpg', 'raby.jpg']
    with open(photo[rand], 'rb') as photo:

        await message.reply_photo(photo, caption=kb[rand])


@dp.message_handler(commands=['name'])
async def name(message: types.Message,command):
    if command.args:
        await bot.promote_chat_member(message.chat.id,message.from_user.id,can_pin_messages = True)
        await bot.set_chat_administrator_custom_title(message.chat.id, message.from_user.id, command.args)
        await message.answer(f"Привет  <b>{command.args}</b>, я всеволод бо)))\n "
                             f"чтобы увидеть список команд напиши /commandlist")

@dp.message_handler(commands=['commands'])
async def coommands(message: types.Message, command):
    if command.args == 'kek':
        kb = ['Что надо сказать негру в униформе?\nМне, пожалуйста, бигмак и колу.',
              'Как напугать негра?\nВзять его с собой на аукцион.']
        rand = random.randint(0, 1)
        photo = ['negros.jpg', 'raby.jpg']
        with open(photo[rand], 'rb') as photo:
            await message.reply_photo(photo, caption=kb[rand])
    elif command.args == 'tooth':
        with open('tooth.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption='смотри.....')



@dp.message_handler(commands=['commandlist'])
async def comm(message: types.Message,command):
    await message.reply('ПЕРВАЯ команда: расскажи анекдот, чтобы всеволод рассказал анекдот напиши команду "/commands kek" \n '
                        'ВТОРАЯ команда: всеволод покажи зуб, чтобы всеволод показал зуб введи команду "/commands tooth"\n')



@dp.message_handler(regexp='(^почему в фильме про пикачу нет команды р, они что расстрелялись?)')
async def cats(message: types.Message):
    with open('gun.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='да.')

@dp.message_handler(regexp=('ты знаешь формулу атмосферного давления?'))
async def formula(message: types.Message):
    await message.reply("мой айкью выше твоего")

@dp.message_handler(regexp=('покемон'))
async def poke(message: types.Message):
    with open('1place.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='это самый сильный покемон аркеус')
    await asyncio.sleep(2)

    await types.ChatActions.upload_photo()

    media = types.MediaGroup()

    media.attach_photo(types.InputFile('2place.jpg'), 'а это второй по силе meowto^_^')


    await message.reply_media_group(media=media)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)