import random
import string
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# import requests as rq
# import datetime as dt
from conf import bot_token


b = Bot(token=bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет. Давай сгенерируем тебе новый надёжный пароль. \n введи цыфрой длину пароля  ")



@dp.message_handler()
async def pas(message: types.Message, password=None):
    try:
        async def gen_pass(length):
                alphabet = "abcdefghijklmnopqrstuxyzABCDEFGHIJKLMNOPQRSTUXYZ"
                choise = await message.reply('Хотите чтобы в пароле были цыфры, введите y/n ')
                if choise == 'y' or choise == 'Y' or choise == 'yes':
                    alphabet += "013456789"
                choise = await message.reply('Хотите чтобы в пароле были символы !@#$%^&, введите y/n ')
                if choise == 'y' or choise == 'Y' or choise == 'yes':
                    alphabet += "!@#$%^&"
                password = ''
                for i in range(length):
                    passwordLetter = random.choice(alphabet)
                    lenPassword = len(password)
                    if lenPassword > 2:
                        lastLetter = password[-1]
                        if passwordLetter != lastLetter:
                            password += passwordLetter
                        else:
                            passwordLetter = random.choice(alphabet)
                            password += passwordLetter
                    else:
                        password += passwordLetter
                return password

        length = int(message.text)
        result = gen_pass(length)
        await message.reply(f'Ваш пароль {result}')

    except:
        await message.reply('ERRORE')


if __name__ == '__main__':
    executor.start_polling(dp)

