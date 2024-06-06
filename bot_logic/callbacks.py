from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types.input_media_photo import InputMediaPhoto
from functions.data_logic import get_catalog, get_catalog_info, print_catalog
from functions.templates import CATALOG_REQUEST_URL
from functions.config import HEADER
from .handlers import get_catalog_hand
from .Classes import MyCallbackForInline, MyCallbackForBackAndForward
from .buttons import inline_buttons_change_product


call_back_router = Router()

@call_back_router.callback_query(MyCallbackForInline.filter())
async def product_printer(query: CallbackQuery, callback_data: MyCallbackForInline):
    await query.message.delete()
    data = get_catalog(CATALOG_REQUEST_URL.format(callback_data.catalog_id), header=HEADER)
    info = get_catalog_info(data)
    posts, photos = print_catalog(info)
    product_count = len(posts)
    change_product_buttons = inline_buttons_change_product(product_count, 0, callback_data.catalog_id)
    await query.message.answer_photo(photo=photos[0], caption=posts[0], reply_markup=change_product_buttons)


@call_back_router.callback_query(MyCallbackForBackAndForward.filter())
async def change_product(query: CallbackQuery, callback_data: MyCallbackForBackAndForward):

    if callback_data.action == "Назад":
        await query.answer()
        if callback_data.actual_number > 0:
            callback_data.actual_number -= 1
        else:
            await get_catalog_hand(query.message)
            return
    elif callback_data.action == "Далее":
        await query.answer()
        if callback_data.actual_number < callback_data.total_count - 1:
            callback_data.actual_number += 1
        else:
            await get_catalog_hand(query.message)
            return
    elif callback_data.action == "В меню":
        await get_catalog_hand(query.message)
        return

    data = get_catalog(CATALOG_REQUEST_URL.format(callback_data.catalog_id), header=HEADER)
    info = get_catalog_info(data)
    posts, photos = print_catalog(info)



    change_product_buttons = inline_buttons_change_product(callback_data.total_count, callback_data.actual_number, callback_data.catalog_id)
    media = InputMediaPhoto(type="photo", media=photos[callback_data.actual_number], caption=posts[callback_data.actual_number])
    await query.message.edit_media(media=media)
    await query.message.edit_reply_markup(reply_markup=change_product_buttons)
