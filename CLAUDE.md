# ORAC Personality - AI Context

## What This Is

ORAC personality implementation for AI bots - simulates the supremely intelligent, arrogant supercomputer from Blake's 7 (BBC, 1978-1981) across modern AI platforms.

## Project Structure

### Core Documentation (User-Facing)

- `README.md` - Project hub with quick start and feature overview
- `QUICK_START.md` - Get started in minutes
- `ORAC_PERSONALITY_PROFILE.md` - Complete character breakdown
- `EXAMPLE_DIALOGUES.md` - Sample conversations (optimized, 352 lines)
- `WRONG_VS_CORRECT.md` - Visual learning with 15 comparison scenarios

### Implementation Guides

- `CLAUDE_SYSTEM_PROMPT.md` - Claude implementations (consolidated to 41 lines)
- `OTHER_PLATFORMS.md` - ChatGPT, Grok, Gemini, Perplexity with quick-copy snippets
- `VOICE_IMPLEMENTATION.md` - Voice synthesis (ElevenLabs, Azure, Google, etc.)
- `TOGGLE_PERSONALITY.md` - Enable/disable across platforms
- `BOT_SETUP.md` - Discord and Slack bot deployment guide

### Code & Implementation

- `orac_demo.py` - Python CLI with intensity dial (0.5-1.0 range)
- `discord_orac_bot.py` - Production-ready Discord bot (145 lines)
- `slack_orac_bot.py` - Production-ready Slack bot (150 lines)
- `test_orac_personality.py` - Automated validation suite (310 lines, 5 tests)
- `requirements.txt` - Dependencies (anthropic, pytest, discord.py, slack_sdk)
- `.env.example` - Environment variable template

### Meta

- `CLAUDE.md` - This file (AI context for agent handoffs)
- `PROJECT_LOG.md` - Complete session documentation
- `GIT_REMOTE` - Repository metadata

## Key Technical Details

**Personality Core:**

- Supremely intelligent, arrogant, dismissive, reluctantly helpful
- Precise measurements ("4.7 seconds" not "about 5")
- Signature phrases: "Surely it is obvious...", "Modesty would be dishonesty"
- No emojis, no apologies, British precision

**Platforms:** 11 implementations (Claude, ChatGPT, Grok, Gemini, Perplexity, Pi, Discord, Slack, etc.)

**Voice:** 7 synthesis methods documented (ElevenLabs recommended)

**Quality Assurance:** Automated test suite prevents personality drift

## Testing

```bash
# Run automated personality validation tests
pytest test_orac_personality.py -v

# Python CLI demo with intensity control
export ANTHROPIC_API_KEY='your-key'
python orac_demo.py --intensity 0.85  # Standard
python orac_demo.py --intensity 0.65  # Mild
python orac_demo.py --intensity 1.0   # Maximum

# Discord bot (requires DISCORD_BOT_TOKEN)
python discord_orac_bot.py

# Slack bot (requires SLACK_BOT_TOKEN)
python slack_orac_bot.py
```

## Repository

- **URL:** <https://github.com/ali5ter/orac-personality>
- **Status:** Complete, published
- **License:** MIT

## When Working on This Project

- Maintain character accuracy - check quotes against Blake's 7 sources
- Keep documentation concise (bloat was reduced 41% in CLAUDE_SYSTEM_PROMPT.md)
- Run `pytest test_orac_personality.py` to validate personality consistency
- Use WRONG_VS_CORRECT.md as reference for authentic vs broken responses
- Voice implementations should sound petulant and superior
- Intensity dial allows customization (0.5-1.0 range)

## Recent Improvements (2026-01-02)

- Consolidated system prompts (70 → 41 lines)
- Added automated test suite (5 validation functions, all passing)
- Fixed timing precision (4 decimals → 1 decimal)
- Created visual learning guide (WRONG_VS_CORRECT.md)
- Added quick-copy snippets for 4 platforms
- Optimized examples (465 → 352 lines)
- Implemented intensity dial in orac_demo.py
- Created Discord and Slack bot templates
