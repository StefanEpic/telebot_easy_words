import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from core.commands.base import start_bot
from core.commands.commands import start
from core.forms.base import play, get_answer, AnswerForm


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.startup.register(start_bot)
    dp.message.register(start, Command(commands="start"))
    dp.message.register(play, Command(commands="play"))

    dp.message.register(get_answer, AnswerForm.GET_ANSWER)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
