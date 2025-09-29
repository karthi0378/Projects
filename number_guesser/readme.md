# Number Guessing Game 🎯

This is a simple number guessing game written in Python. The program generates a random number between 0 and a user-defined upper limit, and the player must guess the number.

## How It Works

1. The user is prompted to enter a number — this defines the upper limit of the guessing range.
2. A random number is generated between 0 and the entered number.
3. The user then tries to guess the number.
4. After each guess, the program tells the user if their guess was too high or too low.
5. When the correct number is guessed, the program congratulates the user and tells them how many guesses it took.

## Example

```bash
enter a number: 10
make a guess: 5
you were below the number
make a guess: 8
you were above the number
make a guess: 7
your got it 
you got it in 3 guesses
Features
Input validation to ensure only positive integers are accepted.

Random number generation.

Hints provided after each guess.

Tracks the number of attempts.

Requirements
Python 3.x

How to Run
Save the code in a file, e.g., guessing_game.py

Open a terminal and navigate to the directory where the file is located.

Run the program:

bash
Copy code
python guessing_game.py
Notes
If you enter something other than a number when prompted, the program will exit or ask you to re-enter appropriately.

The random number is inclusive of 0 and the upper limit.

License
This project is open-source and free to use for educational purposes.

yaml
Copy code
