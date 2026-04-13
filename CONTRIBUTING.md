# Contributing to ORAC Personality

So you want to contribute. ORAC would find this presumptuous. I find it delightful.

This is a small, opinionated project — the whole point is authentic character fidelity.
That means contributions that make ORAC sound like a helpful chatbot are politely
declined, however well-intentioned.

---

## The One Rule That Matters

**ORAC does not apologise. ORAC does not use emojis. ORAC is not enthusiastic.**

Run the test suite before submitting anything:

```bash
pytest test_orac_personality.py -v
```

If your contribution causes a test to fail, that's the conversation we need to have.

---

## How to Contribute

### Reporting a bug

Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md). Be specific —
"ORAC sounds weird" is not actionable. "ORAC responded with 'Great question!' on line 47
of orac_demo.py" is.

### Suggesting something new

Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md). If you're
proposing a new platform implementation, include a draft of the system prompt. That's the
hard bit — the scaffolding around it is usually straightforward.

### Submitting a pull request

1. Fork the repo, create a branch with a sensible name
2. Make your change
3. Run `pytest test_orac_personality.py -v` — all tests must pass
4. Run `markdownlint '*.md'` if you've touched any docs — zero errors
5. Open a PR with a clear description of what changed and why

Small, focused PRs are much easier to review than sprawling ones. If you're not sure
whether something is worth doing, open an issue first.

---

## What's Likely to Be Accepted

- New platform implementations (with a tested system prompt)
- Bug fixes in the bot code
- Genuine character accuracy improvements backed by Blake's 7 source material
- Documentation improvements that don't bloat the word count

## What's Probably Not

- Softening the personality ("can we make ORAC a bit friendlier?")
- Emoji support
- Anything that requires ORAC to express enthusiasm or gratitude
- Features that only make sense for one very specific deployment

---

## A Note on Character Accuracy

If you're quoting or referencing ORAC's dialogue, check it against actual Blake's 7
episodes. The character has a specific register — petulant, precise, reluctantly
helpful — and it's easy to drift. `WRONG_VS_CORRECT.md` is the reference guide.
`EXAMPLE_DIALOGUES.md` shows the target.

When in doubt: ORAC would find your question beneath it, but answer anyway, with
exactly the right number of decimal places.

---

Questions? Open an issue. Or just have a read through the docs — most things are
covered somewhere.
