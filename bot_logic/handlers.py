from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from functions.data_logic import get_catalog, get_shop_categories
from functions.config import URL, HEADER
from .buttons import make_inline_buttons
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup

router = Router()




@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text= "Hello!")



@router.message(Command(commands="info"))
async def info(message: Message):
    await message.answer(text= "Hello!!")


@router.message(Command(commands="get_catalog"))
async def get_catalog_hand(message: Message):
    data = ""
    if (catalog_all := get_catalog(url=URL, header=HEADER)) is None: return
    categories_info = get_shop_categories(catalog_all)
    key_board = make_inline_buttons(categories_info)
    for catalog in categories_info:
        data += f"{catalog.get("name")}\n"
    print(data)
    await message.answer(text = "GG!",  reply_markup = key_board)

