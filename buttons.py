from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,WebAppInfo

manzil = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'Andijon'), KeyboardButton(text = 'Buxoro'),KeyboardButton(text = "Farg'ona")],
        [KeyboardButton(text = 'Jizzax'), KeyboardButton(text = 'Qashqadaryo'),KeyboardButton(text = "Nukus")],
        [KeyboardButton(text = 'Namangan'), KeyboardButton(text = 'Navoiy'),KeyboardButton(text = "Samarkand")],
        [KeyboardButton(text = 'Sirdaryo'), KeyboardButton(text = 'Surxondaryo'),KeyboardButton(text = "Toshkent")],
        [KeyboardButton(text= "Xorazm")]
    ],
    resize_keyboard=True
)
