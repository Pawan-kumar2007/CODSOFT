# CODESOFT 
# Module Documentation

## 1. chatbot.py

### Description
A **simple rule-based chatbot** that demonstrates basic natural language processing capabilities. This chatbot uses pattern matching with regular expressions to identify user intents and provide contextually appropriate responses.

### Key Features
- **Pattern Matching**: Uses regex patterns to recognize user queries like greetings, goodbyes, name inquiries, and questions about feelings
- **Predefined Responses**: Maintains a set of possible responses for each recognized pattern
- **Conversation History**: Tracks conversation history for context and analysis
- **Multiple Intents**: Handles various conversation categories including:
  - Greetings (hello, hi, hey)
  - Farewells (bye, goodbye, exit)
  - Identity questions (who are you, what's your name)
  - Emotional inquiries (how are you, how do you feel)

### Technology
- Python with standard libraries
- Regular expressions for pattern recognition
- Object-oriented design with the `SimpleChatbot` class

### Use Cases
- Learning basic NLP concepts
- Interactive user conversations
- Quick Q&A interactions
- Foundation for building more advanced chatbots

---

## 2. tictactoe_ai.py

### Description
A classic **Tic-Tac-Toe game** with an unbeatable AI opponent powered by the **Minimax algorithm**. The game features witty AI commentary and personality, making it entertaining while demonstrating advanced game theory concepts.

### Key Features
- **Unbeatable AI**: Uses the Minimax algorithm to calculate optimal moves
- **Adjustable Difficulty**: Three difficulty levels:
  - Easy: AI plays randomly
  - Medium: AI uses simplified strategies
  - Impossible: AI plays perfectly with Minimax
- **AI Personality**: The AI provides witty commentary during:
  - Thinking phase (taunt quotes)
  - Victory (win quotes)
  - Defeat (lose quotes)
  - Draws (draw quotes)
  - Move execution (move quotes)
- **Game History**: Maintains history of moves and game states
- **Board Management**: 3x3 board represented as a flat array (0-8 indices)
- **Player Symbols**: Human plays as 'X', AI plays as 'O'

### Technology
- Python with object-oriented design
- Minimax algorithm for perfect AI gameplay
- Enum for player types and states
- Deep copy for game state management

### Use Cases
- Understanding game theory and Minimax algorithm
- Building unbeatable game AI
- Learning recursive algorithms
- Interactive entertainment with personality-driven gameplay

---

## How to Use

### Chatbot
```python
from chatbot import SimpleChatbot

bot = SimpleChatbot()
# Feed user input and get responses based on patterns
```

### Tic-Tac-Toe AI
```python
from tictactoe_ai import TicTacToeGame

game = TicTacToeGame(difficulty="impossible")
game.print_board()
# Play against the unbeatable AI
```
