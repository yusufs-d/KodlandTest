# discord modülünü içe aktarıyoruz
import discord
from discord.ext import commands

# Botun çalıştığını görebilmek için TOKEN kısmına kendi bot token'ınızı koymalısınız.
TOKEN = ''
intents = discord.Intents.default()
intents.message_content = True
# Botumuzun çalışacağı prefix (ön ek) belirlenir. Bu örnekte, komutlar için ön ek olarak "!" kullanıyoruz.
bot = commands.Bot(command_prefix='!',intents=intents)

# Bot çevrimiçi olduğunda çalışan olay
@bot.event
async def on_ready():
    # Botun başarılı bir şekilde çalıştığını gösteren mesaj
    print(f'{bot.user} çevrimiçi!')

# Basit bir komut ekliyoruz: Merhaba komutu
@bot.command()
async def merhaba(ctx):
    # ctx, komutun çalıştırıldığı bağlamı ifade eder
    await ctx.send(f'Merhaba {ctx.author.mention}!')  # Komutu çalıştıran kişiye "Merhaba" der.

# Toplama işlemi yapan bir komut ekleyelim
@bot.command()
async def topla(ctx, a: int, b: int):
    # Komutu çalıştıran kişiye iki sayıyı toplar ve sonucu döner
    sonuc = a + b
    await ctx.send(f'{a} + {b} = {sonuc}')
    
@bot.command()
async def sıfre(ctx, uzunluk):
    elements = "+-/*!&$#?=@<>"
    password = ""
    pass_length = int(input("Enter pass length: "))

    for i in range(pass_length):
        password += random.choice(elements)
    
    await ctx.send(f'Şifreniz: {password}')
    
# Hata yönetimi: Hataları yakalayarak kullanıcıya daha dostça bir mesaj gösterelim
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        # Eğer eksik bir argüman varsa kullanıcıyı bilgilendirir
        await ctx.send('Bu komut için gerekli argümanları eksiksiz girin!')
    elif isinstance(error, commands.CommandNotFound):
        # Eğer geçersiz bir komut girilirse kullanıcıyı bilgilendirir
        await ctx.send('Bu geçerli bir komut değil!')



# Bot tokeni ile giriş yap
bot.run(TOKEN)


