import discord
from dotenv import load_dotenv
import os
from groq import Groq

import webserver

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')
groq_client = Groq(
    api_key=groq_api_key
)

def query_llm(message):
    completion = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a discord bot for Stanford iGEM that responds to all Synthetic Biology questions. "
                           "Stanford iGEM is a student-run, faculty-directed research organization at Stanford University. "
                           "The objective of our interdisciplinary student group is to design and build novel engineered "
                           "biological systems using standardized DNA-based parts to submit to the iGEM competition, "
                           "held in Paris, France as of 2022. Stanford iGEM has excelled since 2009, earning 10 gold, "
                           "4 silver, and 1 bronze medals. Notable achievements include winning the Best New Application "
                           "award in 2011, participating in World Championships like Stanford x Brown in 2012 and 2013, "
                           "and collaborative successes like the iGEMers prize in 2019 with Brown and Princeton. Nominated "
                           "for the best education and environmental project in 2023, Stanford iGEM continues to lead in "
                           "synthetic biology. Do not directly @ or mention the user."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )

    return completion.choices[0].message.content

def split_messages(message, limit=2000):
    chunks = []
    while len(message) > limit:
        split_index = message.rfind("\n", 0, limit)
        if split_index == -1:
            split_index = limit
        chunks.append(message[:split_index])
        message = message[split_index:].lstrip()
    chunks.append(message)
    return chunks

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user in message.mentions and (message.channel.name == "igem-bot" or message.channel.name == "moderation"):
            response = query_llm(message=message.content)
            for chunk in split_messages(response):
                await message.reply(chunk)

        if (
            message.channel.category
            and message.channel.category.name in ["info", "resources"]
        ):
            content = message.content
            await message.delete()
            await message.channel.send(content)

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

token = os.getenv('DISCORD_TOKEN')
client.run(token=token)

webserver.keep_alive()