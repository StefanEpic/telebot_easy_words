from aiogram import types


async def start(message: types.Message) -> None:
    await message.answer(
        text=f"🤖: Привет, {message.from_user.first_name}!\n\n🤖: Для начала игры используй команду /play"
    )
