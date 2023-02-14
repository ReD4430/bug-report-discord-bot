```

import discord

import random

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

#import discord

#client = discord.Client()

import string

@client.event

async def on_message(message):

    if message.content.startswith("!reportbug"):

        if len(message.content) > 10:

            bug_report = message.content[10:]

            bug_channel = discord.utils.get(message.guild.channels, name="afk")

            color = random.randint(0, 0xffffff)

            identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

            embed = discord.Embed(title=f"Bug Reported By {message.author.name}#{message.author.discriminator}", description=bug_report, color=color)

            embed.set_footer(text=f"SkyVillage Network | ID: {identifier}")

            msg = await bug_channel.send(embed=embed)

            color = random.randint(0, 0xffffff)

            embed = discord.Embed(title="Bug Report Received", description="Thank you for reporting the bug.", color=color)

            await message.channel.send(embed=embed)

        else:

            color = random.randint(0, 0xffffff)

            embed = discord.Embed(title="Error", description="Please mention the bug you would like to report.", color=color)

            await message.channel.send(embed=embed)

    if message.content.startswith("!replybug"):

        await message.channel.send(embed=discord.Embed(title="Bug Report Successfully Responded", color=0x00ff00))

        reply = message.content[10:].split(" ", 1)

        if len(reply) == 2:

            bug_channel = discord.utils.get(message.guild.channels, name="afk")

            id = reply[0]

            response = reply[1]

            async for message in bug_channel.history(limit=100):

                if id in message.embeds[0].footer.text:

                    color = message.embeds[0].color

                    embed = discord.Embed(title=message.embeds[0].title, description=message.embeds[0].description, color=color)

                    embed.add_field(name="\u200b", value="", inline=False)

                    embed.add_field(name="Response From Staff:", value=response, inline=False)

                    await message.edit(embed=embed)

                    

                    break

              

            else:

                color = random.randint(0, 0xffffff)

                embed = discord.Embed(title="Error", description="No bug found with the provided ID.", color=color)

                await message.channel.send(embed=embed)

        else:

            color = random.randint(0, 0xffffff)

            embed = discord.Embed(title="Error", description="Please use the command format !replybug ID response.", color=color)

            await message.channel.send(embed=embed)

      

client.run("OTExNjc5ODEwMTc3MjI4ODYx.Gy_SdH.7015MpzzAunhtb9RearTeJm7lfO5P1NDOWzHgY")

```

fi
