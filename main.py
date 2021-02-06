import discord 
import os
import requests
import json
#import pokepy
import random
from keepalive import keep_alive
#from mal import Anime

client = discord.Client()

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
#  anime = Anime(random.randint(1,75))
#  return anime

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

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
    await message.channel.send('Hey Jed')

  if message.content.startswith('!cole'):
    await message.channel.send('Hallo Cole')

  if message.content.startswith('!kreme'):
    await message.channel.send('Whattup Donut Man')
  
  if message.content.startswith('!log'):
    await message.channel.send('https://open.spotify.com/track/7GhIk7Il098yCjg4BQjzvb')

#For in sentence random replies  
  if "not pog" in message.content:
    await message.channel.send('I won\'t pog to that')
  elif "pog" in message.content or "Pog" in message.content:
    await message.channel.send('I\'ll pog to that')

  if "cheese" in message.content or "Cheese" in message.content:
    await message.add_reaction('❣️')
    await message.add_reaction('🧀')


#The actual api using requests
  if message.content.startswith('!pog'):
    quote = get_quote()
    await message.channel.send(quote)

#A chance of Gods
  if message:
    godlike = random.randint(1,10000)
    if godlike == 5000:
      await message.channel.send('Godlike')


#  if message.content.startswith('!anime'):
#    anime = get_anime()
#    await message.channel.send(anime.title)
#    await message.channel.send('Rating: ')
#    await message.channel.send(anime.score)
  
#  if message.content.startswith('!poke'):
#    poke = pokemon()
#    await message.channel.send(poke)

keep_alive()
client.run(os.getenv('KEY'))  
