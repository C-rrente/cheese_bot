import discord 
import os
import requests
import json
#import pokepy
#import random
from keepalive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#def pokemon():
#  response = pokepy.V2Client()
#  poke = pokepy.V2Client().get_pokemon(random.randint(1, 151))
#  return(poke)

#def get_anime():

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
    await message.channel.send ('Hello kristina')

  if message.content.startswith('!steb'):
    await message.channel.send('Hello stebab')

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
    await message.channel.send('Hello foo')

#The actual api using requests
  if message.content.startswith('!pog'):
    quote = get_quote()
    await message.channel.send(quote)

#  if message.content.startswith('!anime'):
#    anime = get_anime()
#    await message.channel.send(anime)

# if message.content.startswith('!pokemon'):
#   poke = pokemon()
#  await message.channel.send(poke)

keep_alive()
client.run(os.getenv('KEY'))  