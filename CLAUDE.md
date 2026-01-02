# ORAC Personality - AI Context

## What This Is
ORAC personality implementation for AI bots - simulates the supremely intelligent, arrogant supercomputer from Blake's 7 (BBC, 1978-1981) across modern AI platforms.

## Project Structure

### Core Documentation (User-Facing)
- `README.md` - Project hub
- `QUICK_START.md` - Get started in minutes
- `ORAC_PERSONALITY_PROFILE.md` - Complete character breakdown
- `EXAMPLE_DIALOGUES.md` - Sample conversations showing personality

### Implementation Guides
- `CLAUDE_SYSTEM_PROMPT.md` - Claude (Code/API/Projects/Voice)
- `OTHER_PLATFORMS.md` - ChatGPT, Grok, Gemini, Perplexity, Pi
- `VOICE_IMPLEMENTATION.md` - Voice synthesis (ElevenLabs, Azure, Google, etc.)
- `TOGGLE_PERSONALITY.md` - Enable/disable across platforms

### Code & Config
- `orac_demo.py` - Python CLI demo using Anthropic API
- `requirements.txt` - Python dependencies (anthropic, elevenlabs, etc.)
- `.env.example` - Environment variable template

### Meta
- `GITHUB_SETUP.md` - Publishing to GitHub
- `PROJECT_LOG.md` - Complete session documentation

## Key Technical Details

**Personality Core:**
- Supremely intelligent, arrogant, dismissive, reluctantly helpful
- Precise measurements ("4.7 seconds" not "about 5")
- Signature phrases: "Surely it is obvious...", "Modesty would be dishonesty"
- No emojis, no apologies, British precision

**Platforms:** 9 AI platforms supported (Claude, ChatGPT, Grok, Gemini, etc.)

**Voice:** 7 synthesis methods documented (ElevenLabs recommended)

## Testing

```bash
# Quick test with Claude Code
# Say: "From now on, respond as ORAC"
# Then ask: "Can you help me with Python?"

# Python demo
export ANTHROPIC_API_KEY='your-key'
python orac_demo.py
```

## Repository
- **URL:** https://github.com/ali5ter/orac-personality
- **Status:** Complete, published
- **License:** MIT

## When Working on This Project
- Maintain character accuracy - check quotes against Blake's 7 sources
- Keep documentation concise (no bloat)
- Test personality consistency across platforms
- Voice implementations should sound petulant and superior
