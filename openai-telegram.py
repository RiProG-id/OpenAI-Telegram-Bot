# Telegram Bot OpenAI ChatGPT version Python by Wannazid
# Remake by RiProG-id
import openai
from aiogram import Bot, Dispatcher, types, executor

bot_tkn = 'TOKEN_BOT_TELEGRAM_ANDA'
openai.api_key = 'KUNCI_API_OPENAI_ANDA'

bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def user_come(pesan: types.Message):
    await pesan.answer('Selamat Datang, silahkan tanyakan apa saja yang ingin anda ketahui')

@dp.message_handler(lambda message: message.text.startswith('/ask'))
async def ai_answer(message: types.Message):
    prompt = message.text[len('/ask'):].strip()
    if prompt:
        respon = openai.Completion.create(model='text-davinci-003', prompt=prompt, temperature=0.7, max_tokens=100)
        parse = respon['choices'][0]['text']
        await message.reply(parse)
    else:
        await message.reply("Mohon masukkan pertanyaan setelah '/ask'")

print('Bot berjalan !')
executor.start_polling(dp)
