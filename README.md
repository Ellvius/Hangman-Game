# Hangman Game

Welcome to the Hangman Game! This is a fun command-line game where you try to guess a hidden word by suggesting letters or the entire word within a limited number of tries.

## Features

- **Random Word Selection**: The game randomly selects a word from a predefined list.
- **User Input**: Players can guess letters or the entire word.
- **Hangman Graphics**: Visual representation of the hangman is shown based on the number of incorrect guesses.
- **Tracking Guesses**: The game keeps track of guessed letters and words, providing feedback on previous guesses.
- **Replay Option**: Players can choose to play again after finishing a game.

## Getting Started

### Prerequisites

- Python 3.x
- Required modules (random)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   ```

2. Navigate to the project directory:
    ```bash
    cd hangman-game
    ```

### Running the Game

To run the game, simply execute the `hangman.py` file:

```bash
python hangman.py
```

### How to Play

- The game will display a series of underscores representing the letters in the word.
- You can guess either a single letter or the entire word.
- For each correct letter guessed, the letter will be revealed in the correct position(s).
- If you guess incorrectly, you will lose a try. You have a total of 6 tries before the game ends.
- The game continues until you either guess the word correctly or run out of tries.
- After finishing, you can choose to play again.

### Acknowledgements

- Inspired by the classic Hangman game.
- Hangman graphics and word list are sourced from `hangman_art.py` and `words.py`, respectively.
