from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from aiogram.types import CallbackQuery, Message, Update, BotCommand
from aiogram.filters.callback_data import CallbackData
from aiogram.filters.command import Command
from functions.data_logic import get_catalog, get_catalog_info, print_catalog
from functions.templates import CATALOG_REQUEST_URL
from functions.config import HEADER
from .Classes import MyCallbackForInline, MyCallbackForBackAndForward
from aiogram.types import InputMediaPhoto
# from .classes import MyCallback


def make_inline_buttons(buttons_test: list):
    builder = InlineKeyboardBuilder()
    i = 1
    for button in buttons_test:
        builder.button(text=f"{button.get('name')}", callback_data=MyCallbackForInline(action=button.get('name'), catalog_id=button.get('id'), actual_number = i))
        i += 1
    builder.adjust(2)
    return builder.as_markup()


def inline_buttons_change_product(total_count: int, actual_count: int, id: int):
    builder = InlineKeyboardBuilder()
    builder.button(text="Назад", callback_data=MyCallbackForBackAndForward(action="Назад", actual_number=actual_count, total_count=total_count, catalog_id=id))
    builder.button(text="Далее", callback_data=MyCallbackForBackAndForward(action="Далее", actual_number=actual_count, total_count=total_count, catalog_id=id))
    builder.button(text="В меню", callback_data=MyCallbackForBackAndForward(action="В меню", actual_number=actual_count, total_count=total_count, catalog_id=id))
    builder.button(text=f"{actual_count + 1} из {total_count}", url="https://t.me/school21_volunteers")
    builder.adjust(2, 1, 1, True)
    return builder.as_markup()



