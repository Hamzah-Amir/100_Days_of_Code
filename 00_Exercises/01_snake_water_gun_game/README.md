# Snake Water Gun Game

A simple Python implementation of a rock-paper-scissors style game where the player competes against the computer.

## 🎮 Game Overview

This is a classic game with a twist - instead of rock, paper, scissors, we use:
- **Snake (s)** - beats Water
- **Water (w)** - beats Gun  
- **Gun (g)** - beats Snake

## 🚀 Features

- **Multi-round gameplay**: Choose how many rounds you want to play
- **Computer opponent**: Random AI opponent for challenging gameplay
- **Score tracking**: Keeps track of wins for both player and computer
- **Input validation**: Ensures only valid moves are accepted
- **Clear feedback**: Shows round results and final game outcome

## 🎯 How to Play

1. **Start the game**: Run `main.py`
2. **Enter rounds**: Choose how many rounds you want to play
3. **Make your move**: For each round, enter:
   - `s` for Snake
   - `w` for Water  
   - `g` for Gun
4. **See results**: The computer will make its choice and show who wins
5. **Final score**: After all rounds, see the final results

## 🏆 Winning Rules

- **Snake beats Water** (Snake can swim through water)
- **Water beats Gun** (Water can rust/damage the gun)
- **Gun beats Snake** (Gun can shoot the snake)

## 💻 Technical Implementation

### Key Components

- **Random module**: Used for computer's random move selection
- **Dictionary-based logic**: `winning_combinations` maps which move beats what
- **Input validation**: Checks if user input is valid before processing
- **Score tracking**: Separate counters for user and computer wins
- **Loop control**: `while` loop manages round progression

### Code Structure

```python
# Game options and winning logic
option = ["s", "w", "g"]
winning_combinations = {
    "s": "w",  # Snake beats Water
    "w": "g",  # Water beats Gun
    "g": "s"   # Gun beats Snake
}
```

## 🎲 Sample Gameplay

```
Snake Water Gun Game
Enter the no of Rounds: 3
Round 1 starts now 
 Snake - s 
 Water - w 
 Gun -g 
Enter your move: s
Computer chooses w
User win
Round 2 starts now 
 Snake - s 
 Water - w 
 Gun -g 
Enter your move: g
Computer chooses s
User win
Round 3 starts now 
 Snake - s 
 Water - w 
 Gun -g 
Enter your move: w
Computer chooses g
User win
You Won 3 Rounds
Congratulations You Won the Game!
```

## 🛠️ Requirements

- Python 3.x
- No external dependencies required

## 🚀 How to Run

1. Navigate to the project directory
2. Run the game:
   ```bash
   python main.py
   ```

## 📝 What I Learned

This project helped me practice:
- **User input handling** and validation
- **Random number generation** for game logic
- **Dictionary data structures** for mapping relationships
- **Control flow** with loops and conditional statements
- **Game state management** and score tracking
- **Error handling** for invalid inputs

## 🎯 Future Enhancements

Potential improvements could include:
- GUI interface using tkinter or pygame
- Sound effects and animations
- Statistics tracking across multiple games
- Different difficulty levels
- Multiplayer support 