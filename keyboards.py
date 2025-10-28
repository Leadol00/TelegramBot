from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import emoji


btn_info = KeyboardButton(f"{emoji.INFORMATION} Инфо")
btn_games = KeyboardButton(f"{emoji.VIDEO_GAME} Игры")
btn_profile = KeyboardButton(f"{emoji.PERSON} Профиль")
btn_time = KeyboardButton("Время")


btn_rps = KeyboardButton(f"{emoji.PLAY_BUTTON} Камень ножницы бумага")
btn_quest = KeyboardButton(f"{emoji.CITYSCAPE_AT_DUSK} Квест")
btn_back =   KeyboardButton(f"{emoji.BACK_ARROW} Назад")

btn_scissors = KeyboardButton(f"{emoji.SCISSORS} Ножницы")
btn_stone = KeyboardButton(f"{emoji.ROCK}Камень")
btn_paper = KeyboardButton(f"{emoji.NOTEBOOK}Бумага")

btn_image = KeyboardButton(f"{emoji.FRAMED_PICTURE} Сгенирировать изображение")

btn_run_away = InlineKeyboardButton("Бегство от дракона", callback_data="run_away")
btn_jump = KeyboardButton("Прыжок")

kb_jump = ReplyKeyboardMarkup(
    keyboard=[[btn_jump]],
    resize_keyboard=True
)


inline_kb_start_quest = InlineKeyboardMarkup([
    [InlineKeyboardButton("Пройти квест",callback_data="start_quest")]])

inline_kb_choice_one = InlineKeyboardMarkup([
    [InlineKeyboardButton("Ввойти в пещеру", callback_data="cave")],
    [InlineKeyboardButton("Уйти домой", callback_data="home")]
])

inline_kb_choice_two = InlineKeyboardMarkup([
    [InlineKeyboardButton("Пройти тихо", callback_data="pass")],
    [InlineKeyboardButton("Напасть", callback_data= "death")],
    [InlineKeyboardButton("Бежать", callback_data= "run")],
    [btn_run_away]
])

inline_kb_choice_four = InlineKeyboardMarkup([
    [InlineKeyboardButton("Кинуть зелье с ядом", callback_data="potion")],
    [InlineKeyboardButton("Стрелять луком", callback_data="bow")],
    [InlineKeyboardButton("Бить мечом", callback_data="sword")],
    [InlineKeyboardButton("Бить магией", callback_data="magic")]
])

inline_kb_choice_five = InlineKeyboardMarkup([
    [InlineKeyboardButton("Забрать чешую", callback_data="scales")],
    [InlineKeyboardButton("Не брать чешую", callback_data="passscales")]
]

)





inline_kb_choice_three = InlineKeyboardMarkup([
    [InlineKeyboardButton("Взять золото", callback_data="gold")],
    [InlineKeyboardButton("Пройти мимо", callback_data="passgold")]
])






kb_gameSSP = ReplyKeyboardMarkup(
    keyboard=[
        [btn_scissors, btn_stone, btn_paper],
        [btn_back]
    ],
    resize_keyboard=True
)


kb_main = ReplyKeyboardMarkup(
    keyboard=[
       [btn_info, btn_games, btn_profile, btn_time, btn_image]
   ],
   resize_keyboard=True)




kb_game = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rps],
        [btn_quest, btn_back]
    ],
    resize_keyboard=True)

