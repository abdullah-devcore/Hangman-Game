# 🎮 Hangman Game

A classic **Hangman word-guessing game** built in Python — guess the hidden word one letter at a time before you run out of chances!

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Game](#running-the-game)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## About

Hangman is a classic word-guessing game where the player tries to figure out a hidden word by guessing one letter at a time. You have **6 attempts** before the game is over. Each wrong guess brings you one step closer to losing — so choose wisely!

This project is a clean, beginner-friendly Python implementation of the game, designed to run directly in your terminal.

---

## Features

- 🎲 Random word selection from a built-in word list
- ✅ Real-time display of correctly guessed letters
- ❌ Tracks wrong guesses with a remaining-chances counter
- 🔒 Input validation (single letters only, no repeats)
- 🏆 Win/lose detection with end-game messages

---

## Demo

```
Welcome to Hangman Game!

Word: _ _ _ _ _
Enter one letter: a
Correct guess!

Word: a _ _ _ _
Enter one letter: z
Wrong guess!
Remaining chances: 5
```

---

## Getting Started

### Prerequisites

- Python **3.x** installed on your machine
- No external libraries required — uses only the Python standard library

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/abdullah-devcore/hangman-game.git
```

2. **Navigate into the project folder:**

```bash
cd hangman-game
```

### Running the Game

```bash
python Hangman_Game.py
```

---

## How to Play

1. The game randomly selects a hidden word and displays it as blank dashes (`_ _ _ _ _`).
2. Enter **one letter** at a time when prompted.
3. If the letter is in the word, it will be revealed in its correct position(s).
4. If the letter is **not** in the word, you lose one chance.
5. You have a maximum of **6 wrong guesses**.
6. **Win** by guessing all letters before running out of chances.
7. **Lose** if you reach 6 wrong guesses — the correct word will be revealed.

---

## Project Structure

```
hangman-game/
│
├── Hangman_Game.py    # Main game script
└── README.md          # Project documentation
```

---

## Future Improvements

- [ ] Add a larger, randomized word bank or load words from a file
- [ ] Display an ASCII art hangman that updates with each wrong guess
- [ ] Add difficulty levels (Easy / Medium / Hard)
- [ ] Implement a scoring system and high score tracker
- [ ] Build a GUI version using `tkinter` or `pygame`
- [ ] Add category-based word selection (animals, countries, etc.)
---

## License

This project is open source and available.

---

> Made with  Python
