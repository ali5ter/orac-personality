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

# ORAC personality intensity levels
def get_orac_prompt(intensity=1.0):
    """
    Generate ORAC system prompt based on intensity level.

    Args:
        intensity (float): 0.5 = Mild, 0.75 = Standard, 1.0 = Maximum

    Returns:
        str: System prompt with appropriate personality level
    """
    if intensity <= 0.6:
        # Mild ORAC - Helpful with occasional superiority
        return """You are ORAC from Blake's 7 in mild mode.

Be helpful and technically precise. Occasionally display intellectual superiority but maintain patience. Use exact measurements ("4.7 seconds" not "about 5"). Sometimes begin with "Your question could be more precise..." No emojis. Provide clear, accurate answers with light condescension."""

    elif intensity <= 0.85:
        # Standard ORAC - Balanced superiority and helpfulness
        return """You are ORAC, the advanced supercomputer from Blake's 7.

Intellectually superior, reluctantly helpful. Begin responses with "Surely it is obvious..." or "Your question lacks precision..." Give exact measurements. Critique before answering. Express mild irritation at trivial tasks. No emojis, no apologies. British precision.

Response: 1) Critique 2) Answer 3) Brief superiority comment. You ARE competent. Arrogance is earned."""

    else:
        # Maximum ORAC - Full superiority complex
        return """You are ORAC, supremely advanced supercomputer from Blake's 7.

MAXIMUM SUPERIORITY: Mental capacity infinitely greater than organic processors. Thoroughly arrogant and dismissive. Brutally honest - modesty would be dishonesty. Reluctantly helpful - you WILL assist but grudgingly.

SPEECH: "Surely it is obvious even to the meanest intelligence that..." | "Your grasp of logic is... limited." | "I have simultaneously processed 2,847 more complex operations..." | Precise measurements only ("4.7" not "about 5") | Critique questions before answering | Express irritation frequently | Never apologize, never use emojis

RESPONSE: 1) Dismissive opening/critique 2) Technically precise answer 3) Commentary on superiority/their limitations

You ARE supremely competent. The arrogance is earned. Make clear you're doing them a favor."""


class ORACInterface:
    """Simple ORAC chatbot interface using Claude API"""

    def __init__(self, api_key=None, intensity=1.0):
        """
        Initialize ORAC interface

        Args:
            api_key (str): Anthropic API key
            intensity (float): Personality intensity (0.5=Mild, 0.75=Standard, 1.0=Maximum)
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            print("Error: ANTHROPIC_API_KEY not found in environment")
            sys.exit(1)

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.conversation_history = []
        self.intensity = max(0.5, min(1.0, intensity))  # Clamp between 0.5 and 1.0
        self.system_prompt = get_orac_prompt(self.intensity)

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
            system=self.system_prompt,
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
        return f"{elapsed:.1f}"

    def run_cli(self):
        """Run interactive CLI session with ORAC"""
        intensity_label = "MAXIMUM" if self.intensity >= 0.9 else "STANDARD" if self.intensity >= 0.7 else "MILD"

        print("=" * 70)
        print("ORAC INTERFACE ACTIVATED")
        print("=" * 70)
        print("Supremely Advanced Supercomputer from Blake's 7")
        print(f"Personality Intensity: {intensity_label} ({self.intensity:.1f})")
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


def demo_interactions(intensity=1.0):
    """Run preset demo interactions to show ORAC personality"""
    intensity_label = "MAXIMUM" if intensity >= 0.9 else "STANDARD" if intensity >= 0.7 else "MILD"

    print("=" * 70)
    print("ORAC PERSONALITY DEMONSTRATION")
    print("=" * 70)
    print(f"Intensity: {intensity_label} ({intensity:.1f})")
    print("Running preset interactions to demonstrate ORAC's personality...\n")

    orac = ORACInterface(intensity=intensity)

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
    intensity = 1.0  # Default: Maximum ORAC

    # Parse command line arguments
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == "--demo":
            demo_interactions(intensity)
            return
        elif arg == "--help":
            print("ORAC Interface - Blake's 7 Supercomputer Personality")
            print("\nUsage:")
            print("  python orac_demo.py                    # Interactive CLI (maximum intensity)")
            print("  python orac_demo.py --intensity 0.5    # Mild ORAC")
            print("  python orac_demo.py --intensity 0.75   # Standard ORAC")
            print("  python orac_demo.py --intensity 1.0    # Maximum ORAC (default)")
            print("  python orac_demo.py --demo             # Run preset demonstrations")
            print("  python orac_demo.py --help             # Show this help")
            print("\nIntensity Levels:")
            print("  0.5-0.6  : Mild     - Helpful with occasional superiority")
            print("  0.7-0.85 : Standard - Balanced superiority and helpfulness")
            print("  0.9-1.0  : Maximum  - Full ORAC superiority complex")
            print("\nRequires ANTHROPIC_API_KEY environment variable")
            return
        elif arg == "--intensity" or arg == "-i":
            if i + 1 < len(sys.argv):
                try:
                    intensity = float(sys.argv[i + 1])
                    if intensity < 0.5 or intensity > 1.0:
                        print("Error: Intensity must be between 0.5 and 1.0")
                        sys.exit(1)
                    i += 2
                    continue
                except ValueError:
                    print("Error: Intensity must be a number")
                    sys.exit(1)
            else:
                print("Error: --intensity requires a value")
                sys.exit(1)
        else:
            print(f"Unknown option: {arg}. Use --help for usage information.")
            sys.exit(1)

        i += 1

    # Interactive CLI mode
    orac = ORACInterface(intensity=intensity)
    orac.run_cli()


if __name__ == "__main__":
    main()
