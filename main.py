import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



            
@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def globalpot(ctx):
    await ctx.send('Глобальное потепле́ние — долгосрочное повышение средней температуры климатической системы Земли, происходящее уже более века, основной причиной чего, по мнению подавляющего большинства учёных, является человеческая деятельность антропогенных факторов')


@bot.command()
async def reason(ctx):
    await ctx.send('Поскольку выбросы парниковых газов окутывают всю Землю, они удерживают солнечное тепло. Это приводит к глобальному потеплению и изменению климата. В настоящее время потепление на Земле происходит быстрее, чем когда-либо за всю историю наблюдений.')


@bot.command()
async def decision(ctx):
    await ctx.send('Экономьте энергию дома, Ходите пешком, ездите на велосипеде или пользуйтесь общественным транспортом, Употребляйте больше овощей, Выбрасывайте меньше продуктов питания, Сокращайте потребление, используйте вещи повторно, ремонтируйте их и отправляйте на вторичную переработку, Поменяйте источник домашнего энергоснабжения, Пересаживайтесь на электромобили')


@bot.command()
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Какой твой выбор?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await bot.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Отлично, у нас ничья!\nТвой выбор: {user_choice}\nМой выбор: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Хорошая попытка, но я выйграл!\nТвой выбор: {user_choice}\nМой выбор: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"О нет, ты победил меня!!\nТвой выбор: {user_choice}\nМой выбор: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'Перо побеждает меч? Больше похоже на то, что бумага бьет камень!!\nТвой выбор: {user_choice}\nМой выбор: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'О нет, у нас ничья. Я требую реванш!\nТвой выбор: {user_choice}\nМой выбор: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"О да, я порезал тебя на кусочки!\nТвой выбор: {user_choice}\nМой выбор: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'ХАХА, я сломал твои ножницы, у меня камень!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Блин, ты порезал меня :< \nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Не так хорошо, но у нас ничья!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

@bot.command()
async def procent(ctx):
    await ctx.send('Шесть миллиардов жителей планеты, треть которых – дети, дышат загрязненным воздухом, что создает угрозу их здоровью и даже жизни. Примерно процент рагрязнения окружающей среды 90% и этим воздухом дышат все живые организмы!')





bot.run("TOKEN")
