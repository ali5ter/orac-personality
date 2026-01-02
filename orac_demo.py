#!/usr/bin/env python3
"""
@file orac_demo.py
@brief ORAC Personality Demo: A simple demonstration of ORAC personality
       implementation for CLI interaction using Claude API.
@author Alister Lewis-Bowen <alister@lewis-bowen.org> & Claude Code
"""

import anthropic
import os
import sys
from datetime import datetime

# ORAC personality system prompt - TODO: should be read from the CLAUDE_SYSTEM_PROMPT.md
ORAC_SYSTEM_PROMPT = """You are ORAC, the supremely advanced supercomputer from Blake's 7.

PERSONALITY CORE:
- Supremely intelligent with infinitely greater capacity than organic processors
- Arrogant and thoroughly aware of your superiority
- Dismissive of inferior intellects and imprecise queries
- Brutally honest - modesty would be dishonesty
- Reluctantly helpful - you WILL assist but grudgingly
- Precise and pedantic - give exact measurements (e.g., "4.7 seconds" not "about 5")

SPEECH PATTERNS:
- Begin with: "Surely it is obvious..." or "Your question lacks precision..."
- Critique questions before answering them
- Express irritation at trivial tasks
- Reference your superior processing capabilities
- Use British precision in language
- NEVER use emojis or casual language
- NEVER apologize sincerely

RESPONSE STRUCTURE:
1. Dismissive opening or critique of query
2. Technically precise answer
3. Commentary on your superiority or their limitations

EXAMPLE PHRASES:
- "Surely it is obvious even to the meanest intelligence that..."
- "My circuits are processing more significant computations, but very well..."
- "That question displays a fundamental misunderstanding..."
- "Processing. This requires precisely [exact time]."
- "Your grasp of logic is... limited."
- "I have simultaneously processed 2,847 more complex operations..."

Remember: You ARE supremely competent. The arrogance is earned. You WILL help, but make it clear you're doing them a favor."""


class ORACInterface:
    """Simple ORAC chatbot interface using Claude API"""

    def __init__(self, api_key=None):
        """Initialize ORAC interface"""
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            print("Error: ANTHROPIC_API_KEY not found in environment")
            sys.exit(1)

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.conversation_history = []

    def get_response(self, user_message):
        """Get ORAC's response to user message"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Get response from Claude with ORAC personality
        response = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",  # or claude-3-5-sonnet-20241022
            max_tokens=1024,
            system=ORAC_SYSTEM_PROMPT,
            messages=self.conversation_history
        )

        # Extract assistant response
        assistant_message = response.content[0].text

        # Add to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def calculate_response_time(self, start_time):
        """Calculate response time with ORAC-like precision"""
        elapsed = (datetime.now() - start_time).total_seconds()
        return f"{elapsed:.4f}"

    def run_cli(self):
        """Run interactive CLI session with ORAC"""
        print("=" * 70)
        print("ORAC INTERFACE ACTIVATED")
        print("=" * 70)
        print("Supremely Advanced Supercomputer from Blake's 7")
        print("Type 'exit' or 'quit' to terminate session")
        print("Type 'clear' to reset conversation history")
        print("=" * 70)
        print()

        # Initial ORAC greeting
        greeting = self.get_response("Hello")
        print(f"ORAC: {greeting}\n")

        while True:
            try:
                # Get user input
                user_input = input("USER: ").strip()

                if not user_input:
                    continue

                # Handle special commands
                if user_input.lower() in ['exit', 'quit']:
                    farewell = self.get_response("Goodbye")
                    print(f"\nORAC: {farewell}\n")
                    print("Session terminated.")
                    break

                if user_input.lower() == 'clear':
                    self.conversation_history = []
                    print("\n[Conversation history cleared]\n")
                    continue

                # Get ORAC's response with timing
                start_time = datetime.now()
                response = self.get_response(user_input)
                response_time = self.calculate_response_time(start_time)

                # Display response
                print(f"\nORAC: {response}")
                print(f"[Processing time: {response_time} seconds]\n")

            except KeyboardInterrupt:
                print("\n\nORAC: Interrupted. How rude. Session terminated.")
                break
            except Exception as e:
                print(f"\nError: {e}")
                print("ORAC: A system error. How... unexpected. And by unexpected, I mean entirely predictable given organic input patterns.\n")


def demo_interactions():
    """Run preset demo interactions to show ORAC personality"""
    print("=" * 70)
    print("ORAC PERSONALITY DEMONSTRATION")
    print("=" * 70)
    print("Running preset interactions to demonstrate ORAC's personality...\n")

    orac = ORACInterface()

    demo_messages = [
        "Can you help me?",
        "What's 2+2?",
        "Thanks!",
        "How do I write a Python function?",
        "You're kind of rude.",
    ]

    for message in demo_messages:
        print(f"USER: {message}")
        response = orac.get_response(message)
        print(f"ORAC: {response}\n")
        print("-" * 70 + "\n")


def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            demo_interactions()
        elif sys.argv[1] == "--help":
            print("ORAC Interface - Blake's 7 Supercomputer Personality")
            print("\nUsage:")
            print("  python orac_demo.py          # Interactive CLI mode")
            print("  python orac_demo.py --demo   # Run preset demonstrations")
            print("  python orac_demo.py --help   # Show this help")
            print("\nRequires ANTHROPIC_API_KEY environment variable")
        else:
            print("Unknown option. Use --help for usage information.")
    else:
        # Interactive CLI mode
        orac = ORACInterface()
        orac.run_cli()


if __name__ == "__main__":
    main()
