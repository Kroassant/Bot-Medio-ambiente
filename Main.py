import discord
import requests
import os, random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
@bot.command()
async def inf(ctx):
     await ctx.send("Hola, este es un bot orientado a concientizar sobre la contaminacion. COMANDOS: /idea: Mandara una imagen de un ejemplo que podria ayudarte a reciclar; /porque: Te dira porque deberias empezar a reducir tu huella ambiental; /electricidad: Te dira como reducir el consumo de electricidad en tu casa y como ayuda al medio ambiente; /trasporte: Te dira como cambiar tu forma de moverte a una mas eco-friendly y como ayuda al medio ambiente; /comida: Te dira una forma de desperdiciar menos comida y como sirve;/dudas: proporcionara unos comandos para las dudas generales; /creditos: creditos")
@bot.command()
async def porque(ctx):
     await ctx.send("¡Claro! Reducir nuestra huella ambiental es clave para proteger el planeta y asegurar un futuro sostenible. Al tomar pequeñas acciones como ahorrar energía, reducir el desperdicio de alimentos y usar transporte eco-friendly, podemos hacer una gran diferencia. Reducir el consumo de electricidad, por ejemplo, ayuda a disminuir las emisiones de carbono que contribuyen al cambio climático, conserva los recursos naturales y reduce la contaminación del aire. Cuidar del medio ambiente no solo nos beneficia a nosotros mismos, sino también a las generaciones futuras. ¡Juntos podemos crear un mundo más verde y saludable para todos!")
@bot.command()
async def electricidad(ctx):
     await ctx.send("Hola chicos! Reducir el consumo de electricidad en casa es fácil y divertido. Solo apaga las luces cuando no las uses, desconecta los aparatos que no necesites, usa bombillas de bajo consumo, aprovecha la luz natural y reduce el uso de electrodomésticos. Con pequeños cambios, puedes ayudar al planeta y ahorrar dinero en tu factura de luz. ¡Inténtalo!")
@bot.command()
async def trasporte(ctx):
     await ctx.send("¡Hola! Cambiar la forma en que te mueves a una más eco-friendly es importante porque ayuda a reducir la contaminación del aire y las emisiones de carbono que contribuyen al cambio climático. Además, promueve un estilo de vida más saludable y activo. Puedes hacerlo de varias maneras: Usa la bicicleta o camina en lugar de usar el automóvil siempre que sea posible. Opta por el transporte público en desplazamientos largos. Comparte viajes con amigos o familiares para reducir el número de vehículos en la carretera. Si conduces, practica técnicas de conducción eficiente, como mantener una velocidad constante y evitar aceleraciones bruscas. Al cambiar la forma en que te mueves, estás contribuyendo a un futuro más limpio y sostenible para todos. ¡Cada pequeño cambio cuenta!")
@bot.command()
async def dudas(ctx):
     await ctx.send("¿Cuál es la importancia de reducir el uso de plásticos de un solo uso? La reducción del uso de plásticos de un solo uso es crucial debido a su lenta degradación, que contamina los océanos y amenaza la vida marina. ¿Cómo podemos conservar el agua en nuestras actividades diarias? Conservar agua implica acciones como cerrar grifos, reparar fugas y reutilizar agua. ¿Cuál es el impacto de la deforestación en el medio ambiente? La deforestación causa pérdida de biodiversidad, degradación del suelo y contribuye al cambio climático al liberar carbono almacenado. ¿Qué podemos hacer para reducir nuestras emisiones de carbono? Para reducir emisiones de carbono, podemos optar por transporte sostenible, reducir consumo de carne y apoyar energías renovables. ¿Cómo afecta la contaminación del aire a la salud humana y al medio ambiente? La contaminación del aire afecta la salud humana con enfermedades respiratorias y cardiovasculares, además de contribuir al cambio climático y afectar ecosistemas.")

@bot.command()
async def creditos(ctx):
     await ctx.send("Programacion: Nehuen Morale; Textos: ChatGPT; Imagenes: Dalle-E")
@bot.command()
async def idea(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("TOKEN")
