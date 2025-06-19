# Nextgen Encryption: Secret Code Language in Python

This project is a simple Python script that lets you **encode** or **decode** messages using a custom set of rules. It’s perfect for beginners who want to practice Python string manipulation and basic user input.

## Features

- **Encode**: Hide your message by rearranging letters and adding fixed patterns.
- **Decode**: Reveal the original message from the encoded text.
- No external libraries or imports needed—just pure Python!

## How It Works

### Encoding Rules

- If a word has **3 or more characters**:
  - Remove the first letter, add it to the end.
  - Add `"huk"` at the start and `"kkt"` at the end.
- If a word has **less than 3 characters**:
  - Reverse the word.

### Decoding Rules

- If a word has **3 or more characters**:
  - Remove the first 3 and last 3 characters.
  - Move the last letter to the front.
- If a word has **less than 3 characters**:
  - Reverse the word.
