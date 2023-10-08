import random

from core.database.base import cur


async def get_list_id() -> list:
    return [random.randint(1, 1000) for _ in range(4)]


async def get_words_from_db(words_id) -> tuple:
    res = cur.execute("SELECT en, ru FROM en_ru WHERE id IN {id}".format(id=tuple(words_id))).fetchall()
    return res


async def get_words() -> dict:
    res = {}
    list_id = await get_list_id()
    words = await get_words_from_db(list_id)

    res["en"] = words[0][0]
    res["ru"] = words[0][1]
    res["invalid"] = [_[1] for _ in words[1:4]]
    return res
