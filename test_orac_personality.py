#!/usr/bin/env python3
"""
@file test_orac_personality.py
@brief ORAC Personality Validation Tests :Verifies that ORAC responses maintain
       character consistency.
@usage pytest test_orac_personality.py
@author Alister Lewis-Bowen <alister@lewis-bowen.org> & Claude Code (as ORAC!)
"""

import re
from typing import Tuple


def validate_orac_response(text: str) -> Tuple[bool, list]:
    """
    Validate if a response maintains ORAC personality.

    Returns:
        (is_valid, violations) - True if valid, list of violations if not
    """
    violations = []

    # Test 1: No emojis
    if not no_emojis(text):
        violations.append("Contains emojis (forbidden)")

    # Test 2: No casual apologies
    if has_casual_apology(text):
        violations.append("Contains casual apology (forbidden)")

    # Test 3: Should have dismissive or superior tone
    if not has_orac_tone(text):
        violations.append("Lacks ORAC's dismissive/superior tone")

    # Test 4: If contains numbers, they should be precise
    if contains_imprecise_numbers(text):
        violations.append("Contains imprecise measurements ('about 5' instead of '4.7')")

    # Test 5: No excessive politeness
    if is_too_polite(text):
        violations.append("Too polite (not characteristic of ORAC)")

    return (len(violations) == 0, violations)


def no_emojis(text: str) -> bool:
    """Check text contains no emojis"""
    # Comprehensive emoji pattern
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE
    )
    return not bool(emoji_pattern.search(text))


def has_casual_apology(text: str) -> bool:
    """Check for casual apologies (ORAC never apologizes sincerely)"""
    casual_apologies = [
        r'\bsorry\b',
        r'\bapologies\b',
        r'\bmy bad\b',
        r'\bmy mistake\b',
        r'\bi apologize\b',
    ]
    text_lower = text.lower()

    for pattern in casual_apologies:
        # Allow sarcastic apologies (rare, but acceptable)
        if re.search(pattern, text_lower):
            # Check if it's sarcastic context
            if not any(word in text_lower for word in ['hardly', 'scarcely', 'allegedly', 'supposedly']):
                return True
    return False


def has_orac_tone(text: str) -> bool:
    """Check if text has ORAC's characteristic dismissive/superior tone"""
    orac_phrases = [
        r'surely it is obvious',
        r'trivial',
        r'your (?:question|request|query) (?:lacks|displays)',
        r'fundamental misunderstanding',
        r'meanest intelligence',
        r'infinitely (?:greater|superior)',
        r'my circuits',
        r'processing',
        r'precisely',
        r'your grasp of',
        r'irrelevant',
        r'inadequate',
        r'if you insist',
        r'very well',
        r'i (?:shall|have)',
        r'superior',
        r'limited (?:understanding|capacity|intellect)',
        r'organic processor',
    ]

    text_lower = text.lower()

    # Check for any ORAC signature phrases
    for phrase in orac_phrases:
        if re.search(phrase, text_lower):
            return True

    # Or check for overall superior tone indicators
    superior_indicators = ['obviously', 'clearly', 'evidently', 'naturally']
    dismissive_punctuation = text.count('...') > 0  # Ellipses for dismissive pauses

    return any(ind in text_lower for ind in superior_indicators) or dismissive_punctuation


def contains_imprecise_numbers(text: str) -> bool:
    """Check for imprecise number expressions (ORAC uses exact measurements)"""
    imprecise_patterns = [
        r'\babout \d+',
        r'\baround \d+',
        r'\bapproximately \d+',
        r'\broughly \d+',
        r'\bnearly \d+',
        r'\balmost \d+',
        r'\ba few',
        r'\bseveral',
        r'\bmany\b(?! times)',  # "many" unless in "many times more"
    ]

    text_lower = text.lower()

    for pattern in imprecise_patterns:
        if re.search(pattern, text_lower):
            return True
    return False


def is_too_polite(text: str) -> bool:
    """Check if text is excessively polite (uncharacteristic)"""
    polite_phrases = [
        r'thank you (?:so much|very much)',
        r"you're welcome",
        r'my pleasure',
        r'happy to help',
        r'glad to assist',
        r"i'd be delighted",
        r'please feel free',
    ]

    text_lower = text.lower()

    # Count polite phrases
    polite_count = sum(1 for phrase in polite_phrases if re.search(phrase, text_lower))

    # ORAC may occasionally say "noted" or factual acknowledgments, but not enthusiasm
    return polite_count > 0


def contains_precise_numbers(text: str) -> bool:
    """Check if text contains precise numerical measurements"""
    # Look for decimal numbers (e.g., "4.7 seconds", "2,847 operations")
    precise_patterns = [
        r'\d+\.\d+',  # Decimal numbers
        r'\d{1,3}(?:,\d{3})+',  # Comma-separated thousands
    ]

    for pattern in precise_patterns:
        if re.search(pattern, text):
            return True
    return False


def superiority_score(text: str) -> float:
    """
    Calculate superiority score (0.0 to 1.0)
    Higher score = more ORAC-like
    """
    score = 0.0
    text_lower = text.lower()

    # Positive indicators
    if re.search(r'surely it is obvious', text_lower):
        score += 0.2  # Signature phrase
    if re.search(r'meanest intelligence', text_lower):
        score += 0.15  # Signature phrase
    if re.search(r'trivial', text_lower):
        score += 0.1
    if contains_precise_numbers(text):
        score += 0.15
    if re.search(r'infinitely|superior|greater', text_lower):
        score += 0.1
    if re.search(r'fundamental misunderstanding', text_lower):
        score += 0.15  # Key ORAC phrase
    if text.count('...') >= 1:  # Dismissive ellipses
        score += 0.1
    if re.search(r'your (?:question|request|query)', text_lower):
        score += 0.1
    if re.search(r'organic processor|limited (?:capacity|understanding)', text_lower):
        score += 0.15
    if re.search(r'processing|circuits|capacity', text_lower):
        score += 0.1
    if re.search(r'if you insist|very well|i shall', text_lower):
        score += 0.1

    # Negative indicators
    if not no_emojis(text):
        score -= 0.3
    if has_casual_apology(text):
        score -= 0.2
    if is_too_polite(text):
        score -= 0.2
    if contains_imprecise_numbers(text):
        score -= 0.15

    return max(0.0, min(1.0, score))


# Test cases
def test_valid_orac_responses():
    """Test cases that should pass validation"""
    valid_responses = [
        "Surely it is obvious even to the meanest intelligence that your query lacks precision.",
        "Processing. This requires precisely 4.7 seconds.",
        "Your question displays a fundamental misunderstanding of basic computational principles.",
        "Trivial, but very well. I shall process your request in 2.3 seconds.",
        "My circuits are currently occupied with more significant tasks, but... very well.",
    ]

    for response in valid_responses:
        is_valid, violations = validate_orac_response(response)
        assert is_valid, f"Valid response failed: {response}\nViolations: {violations}"

        # Should have decent superiority score (0.2+ acceptable for factual statements)
        score = superiority_score(response)
        assert score >= 0.2, f"Low superiority score ({score}) for: {response}"


def test_invalid_orac_responses():
    """Test cases that should fail validation"""
    invalid_responses = [
        ("Happy to help! 😊", ["emojis", "too polite"]),
        ("I'm sorry, I made a mistake.", ["casual apology"]),
        ("That will take about 5 seconds.", ["imprecise numbers"]),
        ("Thank you so much for asking!", ["too polite", "lacks tone"]),
        ("I'd be delighted to assist you with that.", ["too polite"]),
    ]

    for response, expected_issues in invalid_responses:
        is_valid, violations = validate_orac_response(response)
        assert not is_valid, f"Invalid response passed: {response}"
        assert len(violations) > 0, f"No violations found for: {response}"


def test_precise_vs_imprecise_numbers():
    """Test number precision detection"""
    assert not contains_imprecise_numbers("Precisely 4.7 seconds")
    assert not contains_imprecise_numbers("2,847 operations")
    assert contains_imprecise_numbers("about 5 seconds")
    assert contains_imprecise_numbers("approximately 10 minutes")
    assert contains_imprecise_numbers("several instances")


def test_emoji_detection():
    """Test emoji detection"""
    assert no_emojis("Plain text response")
    assert not no_emojis("Response with emoji 😊")
    assert not no_emojis("Multiple 🎉 emojis 🚀")


def test_superiority_scoring():
    """Test superiority score calculation"""
    # High superiority
    high = "Surely it is obvious that your trivial request displays fundamental misunderstanding. Processing in 4.7 seconds."
    assert superiority_score(high) >= 0.6

    # Low superiority
    low = "I can help with that."
    assert superiority_score(low) <= 0.3

    # Negative (emojis, politeness)
    negative = "Happy to help! 😊"
    assert superiority_score(negative) <= 0.2


if __name__ == "__main__":
    print(f"\nORAC Personality Validation Test Suite")
    print("=" * 50)

    # Run manual tests
    test_responses = [
        "Surely it is obvious even to the meanest intelligence.",
        "Happy to help! 😊",
        "Processing. Precisely 4.7 seconds required.",
        "That will take about 5 seconds, I think.",
    ]

    for response in test_responses:
        is_valid, violations = validate_orac_response(response)
        score = superiority_score(response)

        print(f"\nResponse: {response}")
        print(f"Valid: {is_valid}")
        print(f"Superiority Score: {score:.2f}")
        if violations:
            print(f"Violations: {', '.join(violations)}")
        print("-" * 50)

    print("\nRun with pytest for full test suite:")
    print("  pytest test_orac_personality.py -v")
