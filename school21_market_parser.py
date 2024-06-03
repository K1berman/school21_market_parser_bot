from functions.config import TOKEN
from aiogram import Bot, Dispatcher
from bot_logic.handlers import router
import asyncio

async def main():

    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    await bot.send_message(chat_id="693186551", text="Бот запущен!")

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())