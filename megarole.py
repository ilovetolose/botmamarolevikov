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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
OSKORBLYA = ['всеволод лох','всеволод чмо','всеволод даун','компьютер',]
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='Перейти в блог Skillbox', url='https://skillbox.ru/media/code/')
urlButton2 = InlineKeyboardButton(text='Перейти к курсам Skillbox', url='https://skillbox.ru/code/')
urlkb.add(urlButton, urlButton2)







API_TOKEN = '6123767585:AAFct5eGVw2vZC_iJ_FhoQ17yObdw-nJbTI'
bot = Bot(token=API_TOKEN,parse_mode="html")
dp = Dispatcher(bot)







#ВСЕ КОМАНДЫ
@dp.message_handler(commands=['commands'])
async def coommands(message: types.Message, command):
    if command.args == 'kek': #АНЕКДОТ
        kb = ['Что надо сказать негру в униформе?\nМне, пожалуйста, бигмак и колу.',
              'Как напугать негра?\nВзять его с собой на аукцион.']
        rand = random.randint(0, 1)
        photo = ['negros.jpg', 'raby.jpg']
        with open(photo[rand], 'rb') as photo:
            await message.reply_photo(photo, caption=kb[rand])
    elif command.args == 'tooth': #зуб
        with open('tooth.jpg', 'rb') as photo:
            await message.reply_photo(photo, caption='смотри.....')
    elif command.args == 'smort': #УМНЫЙ
        smorting = ['Формула скорости равномерного прямолинейного движения: V = S / t, где S — путь тела, t — время, за которое этот путь пройден',
                    'Площадь треугольника равна половине произведения двух сторон на синус угла между ними.',
                    'Закон Архимеда - на тело, погружённое в жидкость или газ, действует выталкивающая сила, численно равная весу объема жидкости или газа, вытесненного телом.',
                    'Плотность = масса объём ρ = m V , где (m) — масса, (V) — объём']
        await message.reply(smorting[random.randint(0,3)])
    elif command.args == 'bones': #КОСТИ
        await message.answer('всеволод кинул '+ str(random.randint(1,6)))
    elif command.args == 'coin': #МОНЕТА
        a = ['орел','решка']
        await message.answer(a[random.randint(0,1)])

#СПИСОК
@dp.message_handler(commands=['commandlist'])
async def comm(message: types.Message):
    await message.reply('ПЕРВАЯ команда: всеволод расскажи анекдот, чтобы всеволод рассказал анекдот напиши команду "/commands <b>kek</b>" \n '
                        'ВТОРАЯ команда: всеволод покажи зуб, чтобы всеволод показал зуб введи команду "/commands <b>tooth"</b>\n'
                        'ТРЕТЬЯ команда: всеволод скажи че нибудь умное... чтобы всеволод сказал что-то умное введи команду "/commands <b>smort</b>"\n'
                        'ЧЕТВЕРТАЯ команда: всеволод матемацируй, чтобы всеволод показал свой уровень математики введи команду "/commands <b>math</b>"\n'
                        'ПЯТАЯ ЮБИЛЕЙНАЯ!!! команда: всеволод узнай силу тяжести, чтобы всеволод узнал силу твоей тяжести введи команду "/grav" тута число \n'
                        'ШЕСТАЯ ваз 2106 команда: чтобы всеволод бросил игральные кости введи команду "/commands <b>/bones</b>"'
                        )


#РОФЛАНПОМИНКИ
@dp.message_handler(regexp='рофл')
async def joke(message: types.Message):
    await message.answer('что такое рофл??? я знаю только шутки из смешной группы вконтакте')
    time.sleep(2)
    await bot.send_message(message.chat.id, text=(link('ПРИКОЛЫБЕСПЛАНТОРЖАКАХАХАХХА','https://vk.com/channehumor')), parse_mode='Markdown',disable_web_page_preview=True)

#vfnbtkamfgm Я ЧМОЛ


@dp.message_handler(commands=['math'])
async def mathe(message: types.Message, command):
    if command.args:
        await message.reply(int(command.args) * int(command.args))
    else:
        await message.answer('sosi leg')


@dp.message_handler(commands=['grav'])
async def phys(msg: types.Message, command):
        if command.args:
            await msg.reply(float(command.args)*9.8)

@dp.message_handler(commands=['pokemon'])
async def poke(msg: types.Message, command):
        if command.args == 'овен' and 'Овен':
            await msg.reply('ты чармандер!!!Покемон огненного типа')
        elif command.args == 'близнецы'and 'Близнецы':
            await msg.reply('ты Баттерфи!!!Покемон насекомого типа')
        elif command.args == 'телец' and 'Телец':
            await msg.reply('ты СУДОВУДО!!!Покемон каменного типа')
        elif command.args == 'рак' and 'Рак':
            await msg.reply('ты Мисдривус!!!Покемон призрачного типа')
        elif command.args == 'лев' and 'Лев':
            await msg.reply('ты ПИКАчу!!!Покемон грузинского типа')
        elif command.args == '' and '':
            await msg.reply('')









#BAN
@dp.message_handler(text=OSKORBLYA)
async def rude(message: types.Message):
    await message.answer('сам такой((...')
    time.sleep(1)
    await message.answer('ОТСТАНЬ ОТ МЕНЯ!!!')
    await bot.kick_chat_member(message.chat.id, message.from_user.id)
    await message.delete()

#КНОПКА
@dp.message_handler(commands=['btn'])
async def send_welcome(message: types.Message):
    btn = types.KeyboardButton(text="a")
    markup = types.ReplyKeyboardMarkup(row_width=0.5)
    text = f'я му, {message.from_user.first_name}'
    await message.answer(text, reply_markup=markup)
    markup = types.ReplyKeyboardRemove()
    return await bot.send_message(message.from_user.id, 'text', markup=markup)





#АНЕКДОТ(ОЛД)
@dp.message_handler(text='всеволод, расскажи анекдот')
async def cats(message: types.Message):
    kb = ['Что надо сказать негру в униформе?\nМне, пожалуйста, бигмак и колу.',
          'Как напугать негра?\nВзять его с собой на аукцион.']
    rand = random.randint(0,1)
    photo = ['negros.jpg', 'raby.jpg']
    with open(photo[rand], 'rb') as photo:

        await message.reply_photo(photo, caption=kb[rand])


#КОМАНДА РРРР
@dp.message_handler(regexp='(^почему в фильме про пикачу нет команды р, они что расстрелялись?)')
async def cats(message: types.Message):
    with open('gun.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='да.')


#ФОРМУЛА АТМОСФЕРЫ
@dp.message_handler(regexp=('ты знаешь формулу атмосферного давления?'))
async def formula(message: types.Message):
    await message.reply("мой айкью выше твоего")


#ПОКЕМОН
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