import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, ReplyKeyboardRemove
from buttons import manzil
from api import prayerTime
import datetime
from database import usersInsert,usersRead,usersUpdate

bugun =f'{datetime.datetime.today().date().day}-{datetime.datetime.today().date().month}-{datetime.datetime.today().date().year}'


#this is bot token
BOT_TOKEN = ""
TOKEN = BOT_TOKEN

dp = Dispatcher()

#this is start command
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f" Assalomu alaykum, {html.bold(message.from_user.full_name)}\nManzilingizni tanlang.",reply_markup=manzil)

    


#this is privacy command
@dp.message(Command(commands=["privacy"]))
async def privacy(message: Message):
    await message.answer(f"Quyidagi link ustiga bosing: [privacy link](https://docs.google.com/document/d/1KI_BSOVnu7YMB_sWzFDXq4rPM8syp3s3-B4joOazVmo/edit?usp=sharing)",parse_mode="Markdown")


#this is addres finds
@dp.message()
async def manzilbot(message: Message) -> None:
    manzil = message.text
    user_id=message.from_user.id
    
    for user in usersRead():
        if user_id == user[0]:
            usersUpdate(manzil =manzil, user_id=user_id)        
            print("bu foydalanuvchi mavjud ekan")
    else:
        usersInsert(manzil=manzil,user_id=message.from_user.id)
        

    try:
        prayer_times = prayerTime(manzil)
        await message.answer(f"bugun: ---{bugun}--- \n"
                            f"bomdod    🏙 {prayer_times['fajr']}\nquyosh chiqishi    🌄 {prayer_times['sun_rise']} \npeshin    🔆 {prayer_times['dhuhr']}\n"
                            f"asr    🔅 {prayer_times['asr']} \nshom    🌆 {prayer_times['maghrib']} \nhufton   🌃 {prayer_times['isha']}",reply_markup=ReplyKeyboardRemove())
    except Exception as error:
        print("error",error)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())    
    except:
        print('tugadi')
