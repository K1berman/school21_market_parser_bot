from aiogram.utils.keyboard import InlineKeyboardBuilder

def make_buttons(buttons_test:list):

    builder = InlineKeyboardBuilder()
    for button in buttons_test:
        builder.button(text=f"{button.get("name")}", callback_data=f"{button.get("name")}")
    builder.adjust(2)

    return builder
