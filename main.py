import discord 
import os
import requests
import json
import random
from keepalive import keep_alive

client = discord.Client()
atw = 'AROUND THE WORLD'

#async def time_check():

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#def pokemon():
#  client = pokepy.V2Client()
#  poke = client.get_pokemon(random.randint(1,151))
#  return(poke.name)
        
#def get_anime():
  #anime = Anime(random.randint(1,75))
  #return anime

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name='Parmesan'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

# For all the people in the server, they have their own request
  if message.content.startswith('!Hello'):
    await message.channel.send ('Hello!')

  if message.content.startswith('!krist'):
    await message.channel.send ('Hello kristina\n https://open.spotify.com/track/0yK8sWD6cfrc7pGfaPIcZH')

  if message.content.startswith('!steb'):
    await message.channel.send('Hello stebab\n https://open.spotify.com/track/1Pt7RPrjEQfzpPA9PS5aZj')

  if message.content.startswith('!bail'):
    await message.channel.send('Hello bailey')

  if message.content.startswith('!este'):
    await message.channel.send('Hola este')

  if message.content.startswith('!connor'):
    await message.channel.send('Hello coner')

  if message.content.startswith('!trent'):
    await message.channel.send('Whattup trent')

  if message.content.startswith('!mads'):
    await message.channel.send('Hello madis2nn')
  
  if message.content.startswith('!phu'):
    await message.channel.send('Hello foo https://open.spotify.com/track/2XpV9sHBexcNrz0Gyf3l18')

  if message.content.startswith('!jay'):
    await message.channel.send('Sup Jay')

  if message.content.startswith('!jed'):
    await message.channel.send('Hey Jed https://open.spotify.com/track/6JnufVNLIO5F5Lk4sEVLeI?si=6de203e6f78947f4')

  if message.content.startswith('!cole'):
    await message.channel.send('Hallo Cole')

  if message.content.startswith('!kreme'):
    await message.channel.send('Whattup Donut Man')
  
  if message.content.startswith('!log'):
    await message.channel.send('https://open.spotify.com/track/7GhIk7Il098yCjg4BQjzvb')

  if message.content.startswith('!devin'):
    await message.channel.send('CRANIUM https://open.spotify.com/track/2y8PnhXwnyHTxe72TtY58e?si=a08f815b12e74ce0')
    
  if message.content.startswith('!gg'):
    await message.channel.send('Nice one dumbass', tts=True)

  if message.content.startswith('--version'):
    await message.channel.send('Current Version: 1.0')
    await message.channel.send('Updates are just organized for my OCD now')



#For in sentence random replies
  if "NOT POG" in message.content.upper():
    await message.channel.send('I won\'t pog to that')
    await message.add_reaction(":not_pog:811762371579740171")
  elif "POG" in message.content.upper():
    await message.channel.send('I\'ll pog to that')
    await message.add_reaction(":pog:811762317314359346")
  
  if "CHEESE" in message.content.upper():
    await message.add_reaction('❣️')
    await message.add_reaction('🧀')
  
  if "AROUND THE WORLD" in message.content.upper():
    await message.channel.send('plɹoʍ ǝɥʇ punoɹɐ')
  
  if "HAPPY BIRTHDAY" in message.content.upper():
    await message.channel.send('Happy birthday! 🎊')
  
  if "HELP" in message.content.upper():
    await message.channel.send('I\'m here to help!')
  
  if "ROLL" in message.content.upper():
    if "D100" in message.content.upper():
      dice = random.randint(1,100)
      await message.channel.send(dice)
    elif "D6" in message.content.upper():
      dice = random.randint(1,6)
      await message.channel.send(dice)
    elif "D10" in message.content.upper():
      dice = random.randint(1,10)
      await message.channel.send(dice)
    elif "D20" in message.content.upper():
      dice = random.randint(1,20)
      await message.channel.send(dice)
    elif "D4" in message.content.upper():
      dice = random.randint(1,4)
      await message.channel.send(dice)



#The actual api using requests
  if message.content.startswith('!pog'):
    quote = get_quote()
    await message.channel.send(quote)

#A chance of Gods
  if message:
    godlike = random.randint(1,10000)
    print(godlike)
    if godlike == 5000:
      await message.channel.send('Godlike')
  
#Hopefully a game
  if message.content.startswith('!game'):
    await message.channel.send('Let\'s go! Choose your weapon')

keep_alive()
client.run(os.getenv('KEY'))  
