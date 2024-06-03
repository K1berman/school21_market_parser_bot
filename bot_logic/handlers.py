from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from functions.data_logic import get_catalog, get_shop_categories
from functions.config import COOKIES, URL
from .buttons import make_buttons
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup

router = Router()




@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text= "Hello!")



@router.message(Command(commands="info"))
async def info(message: Message):
    await message.answer(text= "Hello!!")


@router.message(Command(commands="get_catalog"))
async def get_catalog_(message: Message):
    data = ""
    catalog_all = get_catalog(url = URL, cookies=COOKIES)
    categories_info = get_shop_categories(catalog_all)
    key_board = make_buttons(categories_info)
    for catalog in categories_info:
        data += f"{catalog.get("name")}\n"
    await message.answer(text = "GG!",  reply_markup = key_board.as_markup())