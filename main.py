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
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

@bot.command()
async def procent(ctx):
    await ctx.send('Примерно процент рагрязнения окружающей среды 90%')


@bot.command()
async def procentair(ctx):
    await ctx.send('На сегодняшний день более 90 процентов людей во всем мире дышат воздухом, уровень загрязнения которого превышает допустимые нормы.')


@bot.command()
async def amountpeople(ctx):
    await ctx.send('Шесть миллиардов жителей планеты, треть которых – дети, дышат загрязненным воздухом, что создает угрозу их здоровью и даже жизни.') 




bot.run("MTE2NTI1MTQ2OTg4OTUyMzc1Mg.GjGsCs.zXk5SqWy2fSb70R1DSf2f3womQlb5ABT-7dXaw")