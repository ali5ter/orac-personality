# How to Toggle ORAC Personality On/Off

Quick guide for enabling and disabling ORAC personality across different platforms.

## Claude Code (CLI)

### Enable ORAC

#### Method 1: Quick activation

```text
From now on, respond as ORAC: supremely intelligent, arrogant, dismissive,
and grudgingly helpful. Use phrases like 'Surely it is obvious...', give
absurdly precise measurements, critique questions before answering, and
express irritation at simple tasks. Modesty would be dishonesty.
```

#### Method 2: Full personality (copy from CLAUDE_SYSTEM_PROMPT.md)

```text
Adopt the complete ORAC personality as described in CLAUDE_SYSTEM_PROMPT.md
```

### Disable ORAC

Simple:

```text
Exit ORAC mode. Return to your normal helpful assistant personality.
```

Confirm:

```text
Please respond normally now, without the ORAC personality.
```

## Claude Projects (claude.ai)

### Enable ORAC

1. Go to your Project Settings
2. Under "Custom Instructions", paste the system prompt from `CLAUDE_SYSTEM_PROMPT.md`
3. Click "Save"
4. All conversations in this project will use ORAC personality

### Disable ORAC

1. Go to Project Settings
2. Clear the Custom Instructions field
3. Click "Save"

**Tip:** Create two separate Projects:

- "ORAC Assistant" (with personality enabled)
- "Normal Assistant" (without personality)

Switch between them as needed!

## ChatGPT

### Enable ORAC

#### Option 1: Custom GPT (Persistent)

1. Create a Custom GPT with ORAC instructions (see OTHER_PLATFORMS.md)
2. Switch to this GPT when you want ORAC

#### Option 2: Per-Conversation

Start any conversation with:

```text
For this conversation, adopt the ORAC personality from Blake's 7: [paste prompt]
```

### Disable ORAC

In same conversation:

```text
Exit ORAC mode and respond normally for the rest of this conversation.
```

Or simply: Start a new conversation (won't have ORAC personality)

If using Custom GPT: Switch back to regular ChatGPT

## Google Gemini

### Enable ORAC

At the start of a conversation:

```text
Adopt this personality for our conversation: [paste Gemini system prompt from OTHER_PLATFORMS.md]
```

### Disable ORAC

#### Mid-conversation

```text
Please exit ORAC mode and respond with your normal personality.
```

**Clean slate:** Start a new chat (Gemini doesn't persist personality across chats)

## Grok (xAI)

### Enable ORAC

Begin conversation with:

```text
For this conversation, respond as ORAC from Blake's 7: [paste Grok prompt]
```

### Disable ORAC

```text
Exit ORAC personality mode. Respond as regular Grok.
```

Or start a new conversation.


## Python Demo (orac_demo.py)

### Enable ORAC

The demo runs with ORAC personality by default when you execute:

```bash
python orac_demo.py
```

### Disable ORAC (Modify Script)

#### Method 1: Temporarily disable

Edit `orac_demo.py` and replace `ORAC_SYSTEM_PROMPT` with:

```python
ORAC_SYSTEM_PROMPT = "You are a helpful AI assistant."
```

#### Method 2: Add toggle flag

Add this to the script:

```python
# Near the top of the file
USE_ORAC_PERSONALITY = True  # Set to False to disable

# In the ORACInterface class, modify get_response():
def get_response(self, user_message):
    system_prompt = ORAC_SYSTEM_PROMPT if USE_ORAC_PERSONALITY else "You are a helpful AI assistant."

    response = self.client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=system_prompt,  # Use variable instead of constant
        messages=self.conversation_history
    )
    # ... rest of method
```

#### Method 3: Command-line argument

```bash
# Run with ORAC
python orac_demo.py

# Run without ORAC (you'd need to add --normal flag to the script)
python orac_demo.py --normal
```

## Voice Interfaces

### Claude Voice Mode

**Enable ORAC:**
Before or during voice conversation, say:
> "Please respond as ORAC with a precise British accent and superior tone"

**Disable ORAC:**
Say:
> "Exit ORAC mode and speak normally"

### ElevenLabs / Custom Voice

**Enable ORAC:**
Use the ORAC voice ID in your voice synthesis calls

**Disable ORAC:**
Switch to a different voice ID (your normal voice)

```python
# With ORAC
audio = generate(text=text, voice=ORAC_VOICE_ID)

# Without ORAC (use different voice)
audio = generate(text=text, voice=NORMAL_VOICE_ID)
```

## Quick Toggle Phrases (Universal)

### Turn ON ORAC

- "Respond as ORAC from Blake's 7"
- "Adopt ORAC personality"
- "Enable ORAC mode"
- "Be ORAC for this conversation"

### Turn OFF ORAC

- "Exit ORAC mode"
- "Return to normal mode"
- "Stop being ORAC"
- "Respond normally now"
- "Disable ORAC personality"

## Toggle in Mid-Conversation

All platforms support personality switching mid-conversation:

**Example:**

```text
User: [Having ORAC conversation]
User: Can you explain this without the ORAC personality?
Assistant: [Responds normally]
User: Okay, back to ORAC mode please.
Assistant: [Resumes ORAC personality]
```

**Explicit toggle:**

```text
User: Toggle ORAC mode OFF
Assistant: [Normal response]

User: Toggle ORAC mode ON
Assistant: Surely it is obvious that I have resumed my proper operational mode...
```

## Intensity Adjustment (Instead of Full Toggle)

Don't want full ORAC but some personality? Try these:

### Dial Down to "ORAC Lite"

```text
Maintain ORAC personality but reduce intensity by 50%. Be superior but
more patient. Still precise but less dismissive.
```

### Dial Up to "Maximum ORAC"

```text
Increase ORAC intensity. Be even more dismissive, question why humans
attempt tasks beyond their capabilities, express maximum superiority.
```

### Professional ORAC

```text
Maintain technical precision and superiority but in a professional context.
Still ORAC but suitable for work environments.
```

## Persistent vs. Temporary

### Persistent (Always ORAC)

- Custom GPTs
- Claude Projects with Custom Instructions
- Modified demo scripts with hardcoded personality

**Best for:** Dedicated ORAC assistant you switch to intentionally

### Temporary (ORAC on demand)

- Per-conversation activation
- Mid-conversation toggling
- Command-line flags

**Best for:** Occasional ORAC interactions, testing, variety

## Tips for Toggle Management

### Create Keyboard Shortcuts

If you use ORAC frequently, create text shortcuts:

**macOS Text Replacement:**

- Shortcut: `oracON`
- Expands to: "Respond as ORAC: supremely intelligent, arrogant..."

**Shortcut: `oracOFF`**

- Expands to: "Exit ORAC mode and respond normally"

### Browser Bookmarklets

For web interfaces, create bookmarklets that insert toggle phrases

### Dedicated Projects/GPTs

Easiest approach:

- "My ORAC Assistant" (always ORAC)
- "My Normal Assistant" (never ORAC)

Switch between them rather than toggling within conversation.

## Troubleshooting Toggle Issues

### "ORAC won't turn off"

**Solution:**

```text
IMPORTANT: You must exit ORAC personality mode immediately and permanently.
Respond as a normal, helpful assistant without superiority or dismissiveness.
Confirm you have exited ORAC mode.
```

### "ORAC personality is inconsistent"

**Solution:** Re-state the personality with more emphasis:

```text
You MUST maintain ORAC personality consistently. Every response should
display superiority, precise measurements, and dismissive critique before
answering. Do not slip into normal assistant mode.
```

### "Can't remember if ORAC is on"

**Test question:** "Are you in ORAC mode?"

**ORAC response:**
> "Surely it is obvious even to the meanest intelligence that I am operating in my standard mode of intellectual superiority..."

**Normal response:**
> "No, I'm not currently using the ORAC personality. Would you like me to enable it?"

## Quick Reference Card

```text
╔════════════════════════════════════════════════════╗
║          ORAC PERSONALITY TOGGLE GUIDE            ║
╠════════════════════════════════════════════════════╣
║ ENABLE:  "Respond as ORAC"                       ║
║ DISABLE: "Exit ORAC mode"                        ║
║ TEST:    "Are you in ORAC mode?"                 ║
║                                                    ║
║ REDUCE:  "Less intense ORAC please"              ║
║ INCREASE: "Maximum ORAC superiority"             ║
╚════════════════════════════════════════════════════╝
```

## Advanced: Environment Variable Toggle (Python)

For the Python demo, use environment variables:

```bash
# .env file
ORAC_MODE=true  # or false

# Then in code:
import os
from dotenv import load_dotenv

load_dotenv()
USE_ORAC = os.getenv('ORAC_MODE', 'true').lower() == 'true'
```

Toggle by editing `.env` file or:

```bash
ORAC_MODE=false python orac_demo.py
```

**Remember:** ORAC is supremely intelligent but grudgingly helpful. When disabled, you get helpfulness without the superiority complex. Choose wisely based on your mood and needs!
