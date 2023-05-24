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
OSKOR = ['всеволод лох','всеволод дубина','всеволод дурак','компьютер','клоун','дебил']







API_TOKEN = '6123767585:AAFct5eGVw2vZC_iJ_FhoQ17yObdw-nJbTI'
bot = Bot(token=API_TOKEN,parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message, command):
    await message.reply('Vsevolod - это телеграмм бот, который знает многое о физике и покемонах. Он может решать простые физические задачи и поделиться интересными фактами о покемонах. Кроме того, он может развлечь людей в чате с помощью игр и шуток, а также узнать, какой покемон подходит тебе по знаку зодиака. Общайтесь с Vsevolodом, чтобы разнообразить свои чаты в Телеграмме!\n'
                        'чтобы узнать что я умею введи команду "/commandlist"')
    time.sleep(1)
    with open('6X8TAhIZy6c.jpg', 'rb') as photo:
        await message.reply_photo(photo)



#ВСЕ КОМАНДЫ
@dp.message_handler(commands=['commands'])
async def coommands(message: types.Message, command):
    if command.args == 'kek': #АНЕКДОТ
        kb = ['Что надо сказать темнокожему в униформе?\nМне, пожалуйста, бигмак и колу.',
              'Как напугать темнокожего?\nВзять его с собой на аукцион.']
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
    await message.reply('ПЕРВАЯ главная команда покемонолога: чтобы всеволод узнал вашего покемона по знаку зодиака введите команду "/pokemon"\n'
                        'ВТОРАЯ команда: всеволод покажи зуб, чтобы всеволод показал зуб введите команду "/commands <b>tooth"</b>\n'
                        'ТРЕТЬЯ команда: всеволод скажи что нибудь умное... чтобы всеволод сказал что-то умное введите команду "/commands <b>smort</b>"\n'
                        'ЧЕТВЕРТАЯ команда: всеволод матемацируй, чтобы всеволод показал свой уровень математики введите команду "/commands <b>math</b>"\n'
                        'ПЯТАЯ ЮБИЛЕЙНАЯ!!! команда: всеволод узнай силу тяжести, чтобы всеволод узнал силу твоей тяжести введите команду "/grav" ваша масса \n'
                        'ШЕСТАЯ ваз 2106 команда: чтобы всеволод бросил игральные кости введите команду "/commands <b>/bones</b>"\n'
                        'СЕДЬМАЯ команда: чтобы всеволод подбросил монетку введите команду"/commands <b>/coin</b>"\n'
                        'ВОСЬМАЯ команда: всеволод расскажи анекдот, чтобы всеволод рассказал анекдот введите команду "/commands <b>kek</b>" \n '
                        'ДЕВЯТАЯ вишневая команда: чтобы всеволод узнал скорость машины(меня) в час введите команду "/speed" и путь в метрах который вы преодолели за 5 минут\n'
                        )

'ВОСЬМАЯ главная команда покемонолога: чтобы всеволод узнал вашего покемона по знаку зодиака введите команду "/pokemon"\n'
'ПЕРВАЯ команда: всеволод расскажи анекдот, чтобы всеволод рассказал анекдот введите команду "/commands <b>kek</b>" \n '
#РОФЛАНПОМИНКИ
@dp.message_handler(regexp='рофл')
async def joke(message: types.Message):
    await message.answer('что такое рофл??? я знаю только шутки из смешной группы вконтакте')
    time.sleep(2)
    await bot.send_message(message.chat.id, text=(link('ПРИКОЛЫБЕСПЛАНТОРЖАКАХАХАХХА','https://vk.com/channehumor')), parse_mode='Markdown',disable_web_page_preview=True)

#vfnbtkamfgm Я


@dp.message_handler(commands=['math'])
async def mathe(message: types.Message, command):
    if command.args:
        await message.reply(int(command.args) * int(command.args))
        return
    else:
        await message.answer('sleg')

@dp.message_handler(commands=['speed'])
async def sp(msg: types.Message, command):
        if command.args:
            await msg.reply((float(command.args)*12)/(1000))


@dp.message_handler(commands=['grav'])
async def phys(msg: types.Message, command):
        if command.args:
            await msg.reply(float(command.args)*9.8)

@dp.message_handler(commands=['pokemon'])
async def poke(msg: types.Message, command):
        if command.args == 'овен' and 'Овен':
            with open('char.jpg','rb') as photo:
                await msg.reply_photo(photo, caption='ты чармандер!!!Покемон огненного типа')

        elif command.args == 'близнецы'and 'Близнецы':
            with open('but.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты Баттерфи!!!Покемон насекомого типа')

        elif command.args == 'телец' and 'Телец':
            with open('sudo.jfif','rb') as photo:
                await msg.reply_photo(photo, caption='ты СУДОВУДО!!!Покемон каменного типа')




        elif command.args == 'рак' and 'Рак':
            with open('mis.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты Мисдривус!!!Покемон призрачного типа')



        elif command.args == 'лев' and 'Лев':
            with open('pika.jpg','rb') as photo:
                await msg.reply_photo(photo, caption='ты ПИКАчу!!!Покемон грузинского типа')



        elif command.args == 'дева' and 'Дева':
            with open('klink.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты КЛИНК(клинкз)!!!Покемон стального типа')



        elif command.args == 'весы' and 'Весы':
            with open('spag.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты ТАНГЕЛА ЧтОО ТАНГО??Покемон травяного типа')



        elif command.args == 'скорпион' and 'Скорпион':
            with open('squ.jpg','rb') as photo:
                await msg.reply_photo(photo, caption='ты сквиртл...Покемон водного типа')



        elif command.args == 'стрелец' and 'Стрелец':
            with open('kor','rb') as photo:
                await msg.reply_photo(photo, caption='ты Корвиксар!!Покемон летающего типа')



        elif command.args == 'козерог' and 'Козерог':
            with open('manki.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты Манки(фанкиманкиколахд)Покемон боевого типа')



        elif command.args == 'водолей' and 'Водолей':
            with open('ivi.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты ИВИ(кинотеатр?хд)Покемон нормального типа')



        elif command.args == 'рыбы' and 'Рыбы':
            with open('slow.png','rb') as photo:
                await msg.reply_photo(photo, caption='ты слоупок(хахахачзх?!)Покемон психического типа')






#BAN
@dp.message_handler(text=OSKOR)
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