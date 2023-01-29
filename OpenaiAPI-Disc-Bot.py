from codeop import CommandCompiler
import discord
import os
import openai
import asyncio

intents = discord.Intents().all()
client = discord.Client(intents=intents)


openai.api_key = os.getenv("key")

openai.api_key = "key"

intents.members = True
client = discord.Client(intents=intents)


prompt_count = {}

@client.event
async def on_message(message):
    if message.content.lower().startswith("i "):
        if message.author.id not in prompt_count:
            prompt_count[message.author.id] = 0
        if prompt_count[message.author.id] >= 10:
            await message.channel.send("Sorry, you have reached the daily limit of 10 'really' prompts.")
            return

    print("received message: ", message.content)

    if message.content.lower() == "ping":
        await message.channel.send("pong!")
    if message.content.lower() == "I would like: help":
        await message.channel.send("pong!")
        
    elif message.content.lower().startswith("i want:"):
        prompt = message.content[7:].strip() # Extract the prompt and remove whitespaces
        if prompt: # check if prompt is not empty
            response = openai.Completion.create(
                model="text-ada-001",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            story = response["choices"][0]["text"]
            await message.channel.send(story)

    elif message.content.lower().startswith("i really want:"):
        prompt = message.content[13:].strip() # Extract the prompt and remove whitespaces
        if prompt: # check if prompt is not empty
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            story = response["choices"][0]["text"]
            await message.channel.send(story)
            prompt_count[message.author.id] += 1

async def reset_prompt_counts():
    await asyncio.sleep(86400) # Sleep for one day
    prompt_count.clear()

@client.event
async def on_ready():
    client.loop.create_task(reset_prompt_counts())



client.run("key")

