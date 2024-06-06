from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from functions.data_logic import get_catalog, get_shop_categories
from functions.config import URL, HEADER
from functions.templates import START_HELLO, ACTUAL_COMANDS
from .buttons import make_inline_buttons
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup

router = Router()




@router.message(CommandStart())
async def start(message: Message):
    await message.delete()
    await message.answer(text= START_HELLO)



@router.message(Command(commands="help"))
async def info(message: Message):
    await message.delete()
    await message.answer(text=ACTUAL_COMANDS)


@router.message(Command(commands="get_catalog"))
async def get_catalog_hand(message: Message):
    try:
        await message.delete()
    except TelegramBadRequest:
        pass
    data = ""
    if (catalog_all := get_catalog(url=URL, header=HEADER)) is None: return
    categories_info = get_shop_categories(catalog_all)
    key_board = make_inline_buttons(categories_info)
    for catalog in categories_info:
        data += f"{catalog.get("name")}\n"
    await message.answer(text = "Доступные каталоги",  reply_markup = key_board)

