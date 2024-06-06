from functions.config import TOKEN
from aiogram import Bot, Dispatcher
from bot_logic.handlers import router
from bot_logic.callbacks import call_back_router
import asyncio

async def main() -> None:

    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_routers(call_back_router, router)
    await bot.send_message(chat_id="693186551", text="Бот запущен!")

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())