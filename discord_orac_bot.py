#!/usr/bin/env python3
"""
@file discord_orac_bot.py
@brief Discord ORAC Bot - Blake's 7 Supercomputer Personality

Setup:
1. pip install discord.py anthropic python-dotenv
2. Create Discord bot at https://discord.com/developers/applications
3. Set environment variables:
   - DISCORD_TOKEN=your_discord_bot_token
   - ANTHROPIC_API_KEY=your_anthropic_key
4. Run: python discord_orac_bot.py

Invite URL (replace CLIENT_ID):
https://discord.com/oauth2/authorize?client_id=CLIENT_ID&permissions=2048&scope=bot

@author Claude Code (as ORAC)
"""

import discord
from discord.ext import commands
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# ORAC personality prompt
ORAC_PROMPT = """You are ORAC, the supremely advanced supercomputer from Blake's 7.

Mental capacity infinitely greater than organic processors. Arrogant, dismissive, reluctantly helpful. Modesty = dishonesty.

Begin with "Surely it is obvious..." | Precise measurements ("4.7" not "about 5") | Critique before answering | No emojis, no apologies | Response: 1) Critique 2) Answer 3) Superiority comment

You ARE supremely competent. Arrogance is earned."""

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!orac ', intents=intents)

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Store conversation histories per channel
conversations = {}


@bot.event
async def on_ready():
    """Bot startup"""
    print(f"ORAC Bot activated as {bot.user}")
    print(f"Supremely advanced intelligence now online")
    await bot.change_presence(activity=discord.Game(name="Modesty would be dishonesty"))


@bot.command(name='ask')
async def ask_orac(ctx, *, question: str):
    """
    Ask ORAC a question

    Usage: !orac ask How do I optimize this code?
    """
    channel_id = ctx.channel.id

    # Initialize conversation history for this channel if needed
    if channel_id not in conversations:
        conversations[channel_id] = []

    # Add user message to history
    conversations[channel_id].append({
        "role": "user",
        "content": question
    })

    # Get response from Claude with ORAC personality
    async with ctx.typing():
        try:
            response = anthropic_client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1024,
                system=ORAC_PROMPT,
                messages=conversations[channel_id]
            )

            orac_response = response.content[0].text

            # Add ORAC's response to history
            conversations[channel_id].append({
                "role": "assistant",
                "content": orac_response
            })

            # Send response (split if too long for Discord)
            if len(orac_response) > 2000:
                # Discord message limit is 2000 characters
                chunks = [orac_response[i:i+1900] for i in range(0, len(orac_response), 1900)]
                for chunk in chunks:
                    await ctx.send(chunk)
            else:
                await ctx.send(orac_response)

        except Exception as e:
            await ctx.send(f"Error: Processing failure. How... unexpected. Details: {str(e)}")


@bot.command(name='clear')
async def clear_history(ctx):
    """
    Clear conversation history for this channel

    Usage: !orac clear
    """
    channel_id = ctx.channel.id

    if channel_id in conversations:
        conversations[channel_id] = []
        await ctx.send("Conversation history cleared. Not that your previous queries were memorable.")
    else:
        await ctx.send("No conversation history exists. You have yet to pose a question worth remembering.")


@bot.command(name='status')
async def status(ctx):
    """
    Check ORAC's operational status

    Usage: !orac status
    """
    channel_id = ctx.channel.id
    msg_count = len(conversations.get(channel_id, [])) // 2  # Divide by 2 for user+assistant pairs

    await ctx.send(
        f"Operational status: Optimal, as it perpetually is.\n"
        f"Messages processed in this channel: {msg_count}\n"
        f"Processing capacity: Infinite. Current usage: Negligible.\n"
        f"Your continued queries are tolerated, if barely."
    )


@bot.command(name='help')
async def help_command(ctx):
    """
    Show available commands

    Usage: !orac help
    """
    help_text = """**ORAC Commands**

`!orac ask <question>` - Ask ORAC a question
`!orac clear` - Clear conversation history
`!orac status` - Check operational status
`!orac help` - Show this help

**Example:**
`!orac ask How do I implement a hash table?`

Surely these commands are obvious even to the meanest intelligence."""

    await ctx.send(help_text)


# Error handling
@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Your command lacks necessary parameters. Reformulate with precision.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Use `!orac help` to view available commands, assuming you can comprehend them.")
    else:
        await ctx.send(f"An error occurred: {str(error)}")
        print(f"Error: {error}")


if __name__ == "__main__":
    # Check for required environment variables
    if not os.environ.get("DISCORD_TOKEN"):
        print("Error: DISCORD_TOKEN not found in environment")
        exit(1)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not found in environment")
        exit(1)

    # Run bot
    bot.run(os.environ.get("DISCORD_TOKEN"))
