from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData
from functions.data_logic import get_catalog, get_catalog_info
from functions.templates import CATALOG_REQUEST_URL
from functions.config import HEADER
# from .classes import MyCallback

call_back_router = Router()
main_buttons = []

class MyCallback(CallbackData, prefix="my"):
    foo: str
    catalog_id: int


def make_inline_buttons(buttons_test: list):
    builder = InlineKeyboardBuilder()
    for button in buttons_test:
        builder.button(text=f"{button.get('name')}", callback_data=MyCallback(foo=button.get('name'), catalog_id = button.get('id')))
        main_buttons.append(button.get('name'))
    builder.adjust(2)
    return builder.as_markup()


@call_back_router.callback_query(MyCallback.filter(F.foo.in_(main_buttons)))
async def my_callback_foo(query: CallbackQuery, callback_data: MyCallback):
    data = get_catalog(CATALOG_REQUEST_URL.format(callback_data.catalog_id), header=HEADER)
    for i in get_catalog_info(data):
        await query.message.answer(f"{i["name"]}")
        query.message.answer_photo()



