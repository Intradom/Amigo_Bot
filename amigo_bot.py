# Work with Python 3.6
import re
import random
from discord.ext.commands import Bot

amigos = ['tostador',
        'esposa',
        'cocina',
        'grandes almacenes',
        'frijoles',
        'policía',
        'azul',
        'papá',
        'mantis',
        'temperatura',
        'novio',
        'pimentero',
        'bisonte',
        'basurero',
        'toalla',
        'desayuno',
        'alce',
        'amarillo',
        'cabra',
        'saltamontes',
        'ardillita',
        'abrelatas',
        'medias',
        'petirrojo',
        'edificio',
        'ping pong',
        'fútbol',
        'bolsa',
        'nuera',
        'sillón',
        'calzoncillo',
        'nube',
        'pavo',
        'hija',
        'hermana',
        'vaporera',
        'termómetro',
        'hermano',
        'caja de herramientas',
        'pantaleta',
        'colgador',
        'guantes',
        'horno microondas',
        'rábano',
        'pasa',
        'camarera',
        'mermelada',
        'gato',
        'champú',
        'gaviota',
        'trompa',
        'orquídea',
        'familia',
        'guitarra',
        'latería',
        'lagartija',
        'tenedor',
        'espejo',
        'claxon',
        'árbol',
        'escurridor',
        'licuadora',
        'cierre',
        'jugo',
        'destapador',
        'aperitivo',
        'salmón',
        'papas',
        'sombrero',
        'gafas del sol',
        'baño',
        'primos',
        'mesita de noche',
        'mayonesa',
        'agua',
        'biblioteca',
        'corazón',
        'habilidades',
        'queso',
        'nada']

BOT_PREFIX = ("?", "!")
TOKEN = 'NDc4MjY0MzkzMTIyMTg1MjE4.DlIKtQ.qCSBZklam-5chY2HMwhzq48FnxI' # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='amigo',
                    brief="Amigofication",
                    pass_context=True)
async def amigo(context, user_id):
    user = context.message.server.get_member(re.sub('[^0-9]','', user_id)) # Strips extras
    if user != None:
        await client.change_nickname(user, 'Amigo con ' + random.choice(amigos))
        await client.say(str(user) + ' has been Amigofied!')
    else:
        print("Username not found")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)