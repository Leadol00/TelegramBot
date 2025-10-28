from pyrogram import Client, filters
import config
from datetime import datetime
import keyboards
import random
import time
import json
from FusionBrain_AI import generate
import base64
from pyrogram.types import ForceReply
import asyncio




user = {

}




def commands_game():
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")



bot = Client (
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="hitokioko"
)



def button_filter(button):
    async def func(_, __, msg):
        return msg.text == button.text
    return filters.create(func, "ButtonFilter", button=button)




query_text = "Введите запрос для генерации изображения"
@bot.on_message(button_filter(keyboards.btn_image))
async def image_command(bot, message):
    await message.reply(query_text, reply_markup=ForceReply(True))

@bot.on_message(filters.reply)
async def reply(bot, message):
    if message.reply_to_message.text == query_text:
        query = message.text
        await message.reply_text(f"Генерирую изображение по запросу '{query}', подождите немного")
    image = await generate(query)
    if image:
        image_data = base64.b64decode(image[0])
        with open(f"images/image.jpg", "wb") as file:
            file.write(image_data)
        await bot.send_photo(message.chat.id, f"images/image.jpg", reply_to_message_id=message.id)
    else:
        await message.reply_text("Возникла ошибка, попробуйте еще раз", reply_to_message_id=message.id)




@bot.on_message(filters.command("image"))
async def image(bot, message):
    if len(message.text.split()) > 1:
        query = message.text.replace("/image", "")
        await message.reply_text(f"Генерирую изображение по запросу '{query}', подождите немного")
        image = await generate(query)
        if image:
            image_data = base64.b64decode(image[0])
            with open(f"images/image.jpg", "wb") as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id, f"images/image.jpg", reply_to_message_id=message.id)
        else:
            await message.reply_text("Возникла ошибка, попробуйте еще раз", reply_to_message_id=message.id)
    else:
        await message.reply_text("Введите запрос")



@bot.on_callback_query()
async def handle_query(bot, query):
    await query.message.delete()
    if query.data == "start_quest":
        await bot.answer_callback_query(query.id, text="Добро пожаловать в квест",show_alert=True)
        await query.message.reply_text("Ты пошел в лес и увидел там пещеру что будешь делать?" ,reply_markup=keyboards.inline_kb_choice_one)
    elif query.data == "cave":
        await query.message.reply_text("Ты входишь в пещеру и увидел там спящего дракона", reply_markup=keyboards.inline_kb_choice_two)
    elif query.data == "home":
        await query.message.reply_text("Вы уходите домой")
    elif query.data == "pass":
        await query.message.reply_text("Вы проходите не замеченным и входите в комнату с золотом", reply_markup=keyboards.inline_kb_choice_three)
    elif query.data == "death":
        await query.message.reply_text("Чем будете бить?", reply_markup=keyboards.inline_kb_choice_four)
    elif query.data == "gold":
        await query.message.reply_text("Взять золото")
    elif query.data == "passgold":
        await query.message.reply_text("Пройти мимо")
    elif query.data == "potion":
        await query.message.reply_text("Вы задыхнулись ядом")
    elif query.data == "bow":
        await query.message.reply_text("Вы убили дракона хотите забрать чешую?", reply_markup=keyboards.inline_kb_choice_five)
    elif query.data == "sword":
        await query.message.reply_text("Дракон убил вас")
    elif query.data == "scales":
        await query.message.reply_text("Вы забрали чешую и сделали из нее броню")
    elif query.data == "passscales":
        await query.message.reply_text("Вы вышли с пещеры не с чем")







@bot.on_message(filters.command("quest") | button_filter(keyboards.btn_quest))
async def quest(bot, message):
    await message.reply_text("Хотите ли вы пройти увекательный квест?", reply_markup=keyboards.inline_kb_start_quest)




@bot.on_message(button_filter(keyboards.btn_scissors) |
                button_filter(keyboards.btn_stone) |
                button_filter(keyboards.btn_paper))
async def choice_rps(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    stone = keyboards.btn_stone.text
    scissors = keyboards.btn_scissors.text
    paper = keyboards.btn_paper.text
    user_choice = message.text
    pc_choice = random.choice([stone, scissors, paper])
    user_id = message.from_user.id


    print(user_choice)
    print(pc_choice)

    if user_choice == pc_choice:
        result = "Ничья"
    elif (user_choice == stone and pc_choice == scissors) or \
         (user_choice == scissors and pc_choice == paper) or \
         (user_choice == paper and pc_choice == stone):
        result = "Вы выиграли"
        users[str(message.from_user.id)] += 10
    else:
        result = "Вы проиграли"
        users[str(message.from_user.id)] -= 10



    await message.reply(
        f"Бот выбрал:    {pc_choice}\n"
        f"Ваш выбор:    {user_choice}\n"
        f"{result}\n"
        f"Ваш баланс: {users[str(message.from_user.id)]} монет"
    )
    with open("users.json", "w") as file:
        json.dump(users, file)


@bot.on_message(filters.command("gameSSP") | button_filter(keyboards.btn_rps))
async def game(bot, message):
    with open("users.json", "r") as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 10:
        await message.reply("Твой ход", reply_markup=keyboards.kb_gameSSP)
    else:
        await message.reply(f"Не хватает средств"
                            f"На твоем счету {users[str(message.from_user.id)]}"
                            f"Минимальная сумма для игры - 10")
    with open("users.json", "w") as file:
        json.dump(users, file)





@bot.on_message(filters.command("back") | button_filter(keyboards.btn_back))
async def back(bot, message):
    await message.reply("Назад", reply_markup=keyboards.kb_main)



@bot.on_message(filters.command("game") | button_filter(keyboards.btn_games))
async def game(bot, message):
    await message.reply(f"Список игр", reply_markup=keyboards.kb_game)



@bot.on_message(filters.command("time") | button_filter(keyboards.btn_time))
async def time(bot, message):
    await message.reply(f"Сейчас {datetime.now().hour} часов {datetime.now().minute} минут", reply_markup=keyboards.kb_main)




@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply("Добро пожаловать",reply_markup=keyboards.kb_main)
    with open("users.json", "r") as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
        with open("users.json", "w") as file:
            json.dump(users, file)

    #await bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEObt5oHLM6QOdhaDwqlF6padd-ht9HGwACty0AArEJ0Unl6u8SkemJGDYE")





@bot.on_message(filters.command("info") | button_filter(keyboards.btn_info))
async def info(bot, message):
    await message.reply("Я умею команды /start, /info")


@bot.on_message()
async def echo(bot, message):
    if "привет" in message.text.lower():
        await message.reply("Привет")
    elif "пока" in message.text.lower():
        await message.reply("Пока")
    elif "как дела" in message.text.lower():
        await message.reply("Всё хорошо")
    elif "спасибо" in message.text.lower():
        await message.reply("Пожалуйста")
    else:
        await message.reply(f"Ты написал: {message.text}")

bot.run()
