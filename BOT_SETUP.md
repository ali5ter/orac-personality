# ORAC Bot Setup Guide

Deployment instructions for Discord and Slack bots.

---

## Discord Bot Setup

### Prerequisites
```bash
pip install discord.py anthropic python-dotenv
```

### 1. Create Discord Bot

1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Name it "ORAC"
4. Go to "Bot" tab → "Add Bot"
5. Under "Privileged Gateway Intents", enable:
   - MESSAGE CONTENT INTENT
6. Copy the bot token

### 2. Configure Environment

Create `.env` file:
```bash
DISCORD_TOKEN=your_discord_bot_token_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### 3. Invite Bot to Server

1. Go to "OAuth2" → "URL Generator"
2. Select scopes:
   - `bot`
3. Select permissions:
   - Send Messages
   - Read Message History
4. Copy generated URL and open in browser
5. Select your server and authorize

### 4. Run Bot

```bash
python discord_orac_bot.py
```

### 5. Usage in Discord

```
!orac ask How do I optimize my code?
!orac clear          # Clear conversation history
!orac status         # Check bot status
!orac help           # Show commands
```

---

## Slack Bot Setup

### Prerequisites
```bash
pip install slack-bolt anthropic python-dotenv
```

### 1. Create Slack App

1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. Name it "ORAC"
4. Select your workspace

### 2. Enable Socket Mode

1. Go to "Socket Mode"
2. Enable Socket Mode
3. Copy the App-Level Token (starts with `xapp-`)

### 3. Configure Bot

1. Go to "OAuth & Permissions"
2. Add Bot Token Scopes:
   - `app_mentions:read`
   - `chat:write`
   - `im:history`
   - `channels:history`
3. Install App to Workspace
4. Copy Bot User OAuth Token (starts with `xoxb-`)

### 4. Enable Events

1. Go to "Event Subscriptions"
2. Enable Events
3. Subscribe to bot events:
   - `app_mention`
   - `message.im`

### 5. Configure Environment

Create `.env` file:
```bash
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
ANTHROPIC_API_KEY=your_anthropic_api_key
```

### 6. Optional: Slash Command

1. Go to "Slash Commands"
2. Create command: `/orac`
3. Request URL: Not needed for Socket Mode (leave blank)
4. Description: "Ask ORAC a question"
5. Usage hint: "How do I implement a hash table?"

### 7. Run Bot

```bash
python slack_orac_bot.py
```

### 8. Usage in Slack

**Mentions:**
```
@ORAC How do I optimize this database query?
```

**Direct Messages:**
```
How do I implement a binary tree?
clear                # Clear history
help                 # Show help
status               # Check status
```

**Slash Command (if configured):**
```
/orac How do I write a Python decorator?
```

---

## Environment Variables

Both bots require:

| Variable | Description | Required For |
|----------|-------------|--------------|
| `ANTHROPIC_API_KEY` | Claude API key | Both |
| `DISCORD_TOKEN` | Discord bot token | Discord |
| `SLACK_BOT_TOKEN` | Slack bot token (xoxb-) | Slack |
| `SLACK_APP_TOKEN` | Slack app token (xapp-) | Slack |

Get Anthropic API key: https://console.anthropic.com/

---

## Deployment Options

### Development (Local)

```bash
# Discord
python discord_orac_bot.py

# Slack
python slack_orac_bot.py
```

### Production (Server)

#### Option 1: systemd (Linux)

Create `/etc/systemd/system/orac-discord.service`:
```ini
[Unit]
Description=ORAC Discord Bot
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/orac-personality
Environment="DISCORD_TOKEN=your_token"
Environment="ANTHROPIC_API_KEY=your_key"
ExecStart=/usr/bin/python3 discord_orac_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable orac-discord
sudo systemctl start orac-discord
sudo systemctl status orac-discord
```

#### Option 2: Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install discord.py anthropic python-dotenv

COPY discord_orac_bot.py .
CMD ["python", "discord_orac_bot.py"]
```

Build and run:
```bash
docker build -t orac-bot .
docker run -d \
  -e DISCORD_TOKEN=your_token \
  -e ANTHROPIC_API_KEY=your_key \
  --name orac \
  orac-bot
```

#### Option 3: Screen/tmux (Quick)

```bash
# Start in screen
screen -S orac
python discord_orac_bot.py

# Detach: Ctrl+A, D
# Reattach: screen -r orac
```

---

## Customization

### Adjust Personality Intensity

Edit the `ORAC_PROMPT` variable in either bot file:

**Mild ORAC:**
```python
ORAC_PROMPT = """You are ORAC from Blake's 7 in mild mode.
Be helpful and technically precise. Occasionally display intellectual
superiority but maintain patience. Use exact measurements. No emojis."""
```

**Maximum ORAC:**
```python
ORAC_PROMPT = """You are ORAC, supremely advanced supercomputer from Blake's 7.

MAXIMUM SUPERIORITY: Mental capacity infinitely greater than organic processors.
Thoroughly arrogant and dismissive. Brutally honest - modesty would be dishonesty...
[Full prompt from CLAUDE_SYSTEM_PROMPT.md]
```

### Change Command Prefix (Discord)

```python
bot = commands.Bot(command_prefix='!', intents=intents)  # Change '!orac ' to '!'
```

Then use:
```
!ask How do I...
!status
```

### Add Custom Commands

```python
@bot.command(name='analyze')
async def analyze_code(ctx, *, code: str):
    """Analyze code with ORAC"""
    # Your implementation
```

---

## Troubleshooting

### Discord: "Privileged intent provided is not enabled"
**Solution:** Enable MESSAGE CONTENT INTENT in Discord Developer Portal → Bot settings

### Slack: "not_authed" error
**Solution:** Check SLACK_BOT_TOKEN starts with `xoxb-` and is correct

### Both: "ANTHROPIC_API_KEY not found"
**Solution:** Ensure `.env` file is in same directory as bot script, or export variable:
```bash
export ANTHROPIC_API_KEY=your_key
```

### Discord: Bot not responding
**Solution:** Check bot has "Send Messages" and "Read Message History" permissions in your server

### Slack: Socket mode not working
**Solution:** Ensure Socket Mode is enabled and SLACK_APP_TOKEN (xapp-) is set

---

## Cost Considerations

Both bots use Claude API:
- Typical message: 200-500 tokens
- Cost: ~$0.003 per message (Sonnet pricing)
- 1000 messages ≈ $3

Consider:
- Setting usage limits
- Monitoring API usage
- Using rate limiting for public servers

---

## Security Best Practices

1. **Never commit `.env` to git**
   - Add to `.gitignore`
   - Use environment variables in production

2. **Rotate tokens regularly**
   - Discord: Regenerate bot token
   - Slack: Rotate OAuth tokens
   - Anthropic: Rotate API keys

3. **Limit bot permissions**
   - Only grant necessary scopes
   - Review permissions quarterly

4. **Monitor usage**
   - Set up logging
   - Track API costs
   - Monitor for abuse

---

## Support

- Discord bot issues: https://discord.py.readthedocs.io/
- Slack bot issues: https://slack.dev/bolt-python/
- ORAC personality issues: https://github.com/ali5ter/orac-personality

**Remember:** Modesty would be dishonesty. Both bots are supremely capable and will make this clear.
