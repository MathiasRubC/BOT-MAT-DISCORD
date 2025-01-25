import discord
from discord.ext import commands
from bot_logic import gen_pass  # Importamos la función para generar contraseñas
import random  # Para generar emojis, lanzar moneda y seleccionar imágenes al azar
import os  # Para verificar la existencia de archivos si es necesario

# Configurar los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot con prefijo "!" y transferirle los privilegios
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

# Manejar comandos desconocidos
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Verificar si el mensaje es un comando válido
    ctx = await client.get_context(message)
    if ctx.valid:
        await client.process_commands(message)  # Procesar comandos válidos
    elif message.content.startswith('!'):
        # Responder para comandos desconocidos
        await message.channel.send("No puedo procesar este comando :(")

# Comando para mostrar ayuda
@client.command(name="ayuda")
async def ayuda(ctx):
    help_message = (
        "**Lista de comandos disponibles:**\n"
        "`!hola` - Saludo del bot.\n"
        "`!bye` - Despedida del bot.\n"
        "`!contraseña [longitud]` - Genera una contraseña de la longitud especificada.\n"
        "`!emoji` - Envía un emoji al azar.\n"
        "`!moneda` - Lanza una moneda al aire (Cara o Cruz).\n"
        "`!meme` - Envía un meme al azar."
    )
    await ctx.send(help_message)

# Comando para saludar
@client.command()
async def hola(ctx):
    await ctx.send("Hola un gusto, soy BOTMAT y te ayudaré en lo que necesites :)")

# Comando para despedirse
@client.command()
async def bye(ctx):
    await ctx.send("Nos vemos pronto :)")

# Comando para generar una contraseña
@client.command()
async def contraseña(ctx, length: int):
    try:
        password = gen_pass(length)
        await ctx.send(f"Tu contraseña generada es: {password}")
    except ValueError:
        await ctx.send("Por favor, especifica una longitud válida. Ejemplo: `!contraseña 10`")

# Comando para enviar un emoji al azar
@client.command()
async def emoji(ctx):
    emojis = ["😀", "😂", "🥳", "😎", "💩", "👻", "🤖", "🐶", "🐱", "🐸"]
    random_emoji = random.choice(emojis)
    await ctx.send(f"Aquí tienes un emoji al azar: {random_emoji}")

# Comando para lanzar una moneda
@client.command()
async def moneda(ctx):
    result = random.choice(["Cara", "Cruz"])
    await ctx.send(f"La moneda cayó en: {result}")

# Comando para enviar un meme al azar
@client.command()
async def meme(ctx):
    # Lista de archivos de imágenes
    meme_files = ["imagenes/1.png", "imagenes/2.png", "imagenes/3.png"]
    
    # Seleccionar un archivo al azar
    selected_meme = random.choice(meme_files)
    
    # Verificar si el archivo existe antes de enviarlo
    if os.path.exists(selected_meme):
        with open(selected_meme, 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send(f"No se encontró el archivo: {selected_meme}")

# Ejecutar el bot con tu token
client.run('TOKEN')
                           











