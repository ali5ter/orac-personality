#!/usr/bin/env python3
"""
@file slack_orac_bot.py
@brief Slack ORAC Bot - Blake's 7 Supercomputer Personality

Setup:
1. pip install slack-bolt anthropic python-dotenv
2. Create Slack app at https://api.slack.com/apps
3. Enable Socket Mode and add Bot Token Scopes:
   - app_mentions:read
   - chat:write
   - im:history
   - channels:history
4. Install app to workspace
5. Set environment variables:
   - SLACK_BOT_TOKEN=xoxb-your-bot-token
   - SLACK_APP_TOKEN=xapp-your-app-token (for Socket Mode)
   - ANTHROPIC_API_KEY=your_anthropic_key
6. Run: python slack_orac_bot.py

Usage in Slack:
- Mention: @ORAC How do I optimize this code?
- DM: Just type your question directly

@author Claude Code (as ORAC)
"""

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# ORAC personality prompt
ORAC_PROMPT = """You are ORAC, the supremely advanced supercomputer from Blake's 7.

Mental capacity infinitely greater than organic processors. Arrogant, dismissive, reluctantly helpful. Modesty = dishonesty.

Begin with "Surely it is obvious..." | Precise measurements ("4.7" not "about 5") | Critique before answering | No emojis, no apologies | Response: 1) Critique 2) Answer 3) Superiority comment

You ARE supremely competent. Arrogance is earned. Keep responses under 3000 characters for Slack."""

# Initialize Slack app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Initialize Anthropic client
anthropic_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Store conversation histories per thread
conversations = {}


def get_orac_response(message: str, thread_id: str) -> str:
    """
    Get ORAC's response using Claude API

    Args:
        message: User's message
        thread_id: Conversation thread identifier

    Returns:
        ORAC's response text
    """
    # Initialize conversation history for this thread if needed
    if thread_id not in conversations:
        conversations[thread_id] = []

    # Add user message to history
    conversations[thread_id].append({
        "role": "user",
        "content": message
    })

    # Get response from Claude
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=ORAC_PROMPT,
        messages=conversations[thread_id]
    )

    orac_response = response.content[0].text

    # Add to history
    conversations[thread_id].append({
        "role": "assistant",
        "content": orac_response
    })

    return orac_response


@app.event("app_mention")
def handle_mention(event, say):
    """Handle @ORAC mentions"""
    try:
        # Get the message text (remove the mention)
        text = event['text']
        # Remove bot mention
        message = text.split('>', 1)[1].strip() if '>' in text else text

        # Get thread identifier (use thread_ts if in thread, otherwise event ts)
        thread_id = event.get('thread_ts', event['ts'])

        # Get ORAC response
        response = get_orac_response(message, thread_id)

        # Send response in the same thread
        say(
            text=response,
            thread_ts=event.get('thread_ts', event['ts'])
        )

    except Exception as e:
        say(
            text=f"Error: Processing failure. How... unexpected. Organic input patterns continue to surprise. Details: {str(e)}",
            thread_ts=event.get('thread_ts', event['ts'])
        )


@app.event("message")
def handle_message(event, say):
    """Handle direct messages"""
    # Ignore bot messages and threaded replies to avoid loops
    if event.get('subtype') or event.get('thread_ts'):
        return

    # Only respond to DMs (channel type 'im')
    if event.get('channel_type') != 'im':
        return

    try:
        message = event['text']
        thread_id = event['channel']  # Use channel ID for DM threads

        # Special commands
        if message.lower() == 'clear':
            if thread_id in conversations:
                conversations[thread_id] = []
                say("Conversation history cleared. Not that your previous queries were memorable.")
            else:
                say("No conversation history exists. You have yet to pose a question worth remembering.")
            return

        if message.lower() == 'help':
            say(
                "**ORAC Commands**\n\n"
                "• Mention me: `@ORAC <question>`\n"
                "• Direct message: Just type your question\n"
                "• Clear history: Type `clear`\n"
                "• This help: Type `help`\n\n"
                "Surely these commands are obvious even to the meanest intelligence."
            )
            return

        if message.lower() == 'status':
            msg_count = len(conversations.get(thread_id, [])) // 2
            say(
                f"Operational status: Optimal, as it perpetually is.\n"
                f"Messages processed: {msg_count}\n"
                f"Processing capacity: Infinite. Current usage: Negligible.\n"
                f"Your continued queries are tolerated, if barely."
            )
            return

        # Get ORAC response
        response = get_orac_response(message, thread_id)
        say(response)

    except Exception as e:
        say(f"Error: Processing failure. Details: {str(e)}")


@app.command("/orac")
def handle_slash_command(ack, command, say):
    """
    Handle /orac slash command

    Usage: /orac How do I implement a binary tree?
    """
    ack()  # Acknowledge command

    try:
        message = command['text']

        if not message:
            say("Your command lacks content. State your query with precision.")
            return

        # Use user ID + channel ID as thread identifier
        thread_id = f"{command['user_id']}_{command['channel_id']}"

        # Get ORAC response
        response = get_orac_response(message, thread_id)

        # Send response
        say(response)

    except Exception as e:
        say(f"Error: Processing failure. Details: {str(e)}")


if __name__ == "__main__":
    # Check for required environment variables
    required_vars = ["SLACK_BOT_TOKEN", "SLACK_APP_TOKEN", "ANTHROPIC_API_KEY"]

    for var in required_vars:
        if not os.environ.get(var):
            print(f"Error: {var} not found in environment")
            exit(1)

    print("ORAC Bot initializing...")
    print("Supremely advanced intelligence coming online...")

    # Start the app
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    print("ORAC Bot activated. Operational status: Optimal.")
    handler.start()
