"""
TIC-TAC-TOE AI - Minimax Implementation
A clever AI opponent that plays perfectly using the Minimax algorithm.
With witty commentary and personality! 😏
"""

import random
from typing import List, Tuple, Optional
from enum import Enum
from copy import deepcopy


class Player(Enum):
    """Game players."""
    HUMAN = 1      # You (X)
    AI = -1        # Computer (O)
    EMPTY = 0


class TicTacToeGame:
    """Classic Tic-Tac-Toe with an unbeatable AI opponent."""
    
    def __init__(self, difficulty: str = "impossible"):
        """
        Initialize the game.
        
        Args:
            difficulty: 'easy', 'medium', or 'impossible'
        """
        self.board = [Player.EMPTY] * 9  # 3x3 board as flat array (0-8)
        self.human_symbol = 'X'
        self.ai_symbol = 'O'
        self.difficulty = difficulty
        self.game_history = []
        
        # AI personality quotes
        self.ai_quotes = {
            'taunt': [
                "I'm thinking... (you should be nervous)",
                "Hmm, tough choice... NOT! 🤖",
                "Let me consult my crystal ball...",
                "Your move was... interesting.",
                "Did you really think that would work?",
            ],
            'win': [
                "GG EZ! Better luck next time, human! 🎉",
                "I win! Beep boop, baby! 🤖",
                "Was that your best? I barely broke a sweat (if I had one).",
                "You played... well... you tried! 😅",
                "AI 1, Humans 0. As it should be.",
                "I'm not programmed to lose, just saying.",
            ],
            'draw': [
                "A draw? How... civilized of you.",
                "We both played perfectly. Now we're enemies forever.",
                "Respect. You almost had me there. ALMOST.",
                "This is like a cold war... a draw war.",
            ],
            'lose': [
                "WHAT?! That's impossible! I demand a recount!",
                "You got lucky. Very lucky. Luckier than humanly possible.",
                "Calculating... calculating... I'M BROKEN!",
                "Did you cheat? You must have cheated.",
            ],
            'move': [
                "Watch this move... *chef's kiss* 👌",
                "Just as I calculated...",
                "Boom! In your face!",
                "This is big brain time 🧠",
                "I choose... SCIENCE! 🔬",
            ]
        }
    
    def print_board(self) -> None:
        """Display the current board state."""
        print("\n")
        for i in range(3):
            row = []
            for j in range(3):
                idx = i * 3 + j
                cell = self.board[idx]
                if cell == Player.HUMAN:
                    row.append(f" {self.human_symbol} ")
                elif cell == Player.AI:
                    row.append(f" {self.ai_symbol} ")
                else:
                    row.append(f" {idx+1} ")
            print(" | ".join(row))
            if i < 2:
                print("-----------")
        print("\n")
    
    def get_open_positions(self) -> List[int]:
        """Return list of available move positions."""
        return [i for i in range(9) if self.board[i] == Player.EMPTY]
    
    def is_terminal(self) -> bool:
        """Check if game is over (win or draw)."""
        return self.check_winner() is not None or len(self.get_open_positions()) == 0
    
    def check_winner(self) -> Optional[Player]:
        """
        Check for a winner.
        
        Returns:
            Player.HUMAN if human wins
            Player.AI if AI wins
            None if no winner yet
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                    and self.board[combo[0]] != Player.EMPTY):
                return self.board[combo[0]]
        
        return None
    
    def count_winning_opportunities(self, player: Player) -> int:
        """Count potential winning moves for a player (strategic evaluation)."""
        count = 0
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            player_count = sum(1 for idx in combo if self.board[idx] == player)
            empty_count = sum(1 for idx in combo if self.board[idx] == Player.EMPTY)
            
            if player_count == 2 and empty_count == 1:
                count += 1
        
        return count
    
    def evaluate_position(self, player: Player) -> int:
        """
        Evaluate position for heuristic purposes.
        Used for 'medium' difficulty AI.
        """
        winner = self.check_winner()
        
        if winner == Player.AI:
            return 10
        elif winner == Player.HUMAN:
            return -10
        else:
            # No winner yet - evaluate based on positioning
            ai_opportunities = self.count_winning_opportunities(Player.AI)
            human_opportunities = self.count_winning_opportunities(Player.HUMAN)
            return ai_opportunities - human_opportunities
    
    def minimax(self, board: List, depth: int, is_maximizing: bool, 
                alpha: int = float('-inf'), beta: int = float('inf')) -> int:
        """
        Minimax algorithm with Alpha-Beta Pruning.
        
        Args:
            board: Current board state
            depth: Current search depth
            is_maximizing: True if maximizing (AI), False if minimizing (Human)
            alpha: Best value found so far for maximizer
            beta: Best value found so far for minimizer
            
        Returns:
            Score of the position
        """
        # Check terminal states
        winner = self.check_winner_for_board(board)
        
        if winner == Player.AI:
            return 10 - depth  # Prefer faster wins
        elif winner == Player.HUMAN:
            return depth - 10  # Prefer slower losses
        elif len([i for i in range(9) if board[i] == Player.EMPTY]) == 0:
            return 0  # Draw
        
        if is_maximizing:  # AI's turn (maximizing)
            max_eval = float('-inf')
            for i in range(9):
                if board[i] == Player.EMPTY:
                    board[i] = Player.AI
                    eval_score = self.minimax(board, depth + 1, False, alpha, beta)
                    board[i] = Player.EMPTY
                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    
                    # Beta cutoff
                    if beta <= alpha:
                        break
            return max_eval
        else:  # Human's turn (minimizing)
            min_eval = float('inf')
            for i in range(9):
                if board[i] == Player.EMPTY:
                    board[i] = Player.HUMAN
                    eval_score = self.minimax(board, depth + 1, True, alpha, beta)
                    board[i] = Player.EMPTY
                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    
                    # Alpha cutoff
                    if beta <= alpha:
                        break
            return min_eval
    
    def check_winner_for_board(self, board: List) -> Optional[Player]:
        """Check winner for a given board state."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] 
                    and board[combo[0]] != Player.EMPTY):
                return board[combo[0]]
        
        return None
    
    def get_best_move(self) -> int:
        """
        Get the best move for AI using Minimax.
        Difficulty level changes search depth and strategy.
        """
        if self.difficulty == "easy":
            # Random move for easy mode
            open_positions = self.get_open_positions()
            return random.choice(open_positions)
        
        elif self.difficulty == "medium":
            # Look 1-2 moves ahead
            best_score = float('-inf')
            best_move = None
            
            for i in self.get_open_positions():
                self.board[i] = Player.AI
                
                # Check for immediate win
                if self.check_winner() == Player.AI:
                    self.board[i] = Player.EMPTY
                    return i
                
                # Check for blocking opponent's win
                self.board[i] = Player.EMPTY
                self.board[i] = Player.HUMAN
                if self.check_winner() == Player.HUMAN:
                    self.board[i] = Player.EMPTY
                    return i
                
                self.board[i] = Player.EMPTY
                score = self.evaluate_position(Player.HUMAN)
                
                if score > best_score:
                    best_score = score
                    best_move = i
            
            return best_move if best_move is not None else random.choice(self.get_open_positions())
        
        else:  # "impossible" - full minimax
            best_score = float('-inf')
            best_move = None
            
            for i in self.get_open_positions():
                self.board[i] = Player.AI
                score = self.minimax(self.board, 0, False)
                self.board[i] = Player.EMPTY
                
                if score > best_score:
                    best_score = score
                    best_move = i
            
            return best_move if best_move is not None else random.choice(self.get_open_positions())
    
    def make_human_move(self, position: int) -> bool:
        """
        Make a move for the human player.
        
        Args:
            position: Board position (1-9)
            
        Returns:
            True if valid move, False otherwise
        """
        if position < 1 or position > 9:
            print("❌ Invalid position! Use 1-9.")
            return False
        
        idx = position - 1
        if self.board[idx] != Player.EMPTY:
            print("❌ That spot is taken! Choose another.")
            return False
        
        self.board[idx] = Player.HUMAN
        self.game_history.append(('human', position))
        return True
    
    def make_ai_move(self) -> int:
        """
        Make a move for the AI player.
        
        Returns:
            Position of the move (1-9)
        """
        move = self.get_best_move()
        self.board[move] = Player.AI
        self.game_history.append(('ai', move + 1))
        
        # Witty commentary
        quote = random.choice(self.ai_quotes['move'])
        print(f"🤖 AI: {quote}")
        
        return move + 1
    
    def reset(self) -> None:
        """Reset the game."""
        self.board = [Player.EMPTY] * 9
        self.game_history = []
    
    def play(self) -> None:
        """Main game loop."""
        print("="*60)
        print("🎮 TIC-TAC-TOE vs AI 🤖")
        print("="*60)
        print(f"Difficulty: {self.difficulty.upper()}")
        print(f"You are: {self.human_symbol}, AI is: {self.ai_symbol}")
        print("\nPositions are numbered 1-9 (like a phone keypad)\n")
        
        self.print_board()
        
        # Determine who goes first
        first_player = random.choice(['human', 'ai'])
        if first_player == 'ai':
            print("AI chose to go first... (How generous)\n")
        else:
            print("You go first. Try not to embarrass yourself.\n")
        
        while True:
            # AI's turn (if it's first or alternating)
            if first_player == 'ai' or self.game_history[-1:] and self.game_history[-1][0] == 'human':
                if len(self.get_open_positions()) == 9:  # Skip first turn if AI goes second
                    pass
                else:
                    if not self.game_history or self.game_history[-1][0] == 'human':
                        move = self.make_ai_move()
                        print(f"AI plays position {move}\n")
                        self.print_board()
                        
                        if self.check_winner() == Player.AI:
                            quote = random.choice(self.ai_quotes['win'])
                            print(f"🤖 AI: {quote}")
                            return
                        
                        if len(self.get_open_positions()) == 0:
                            print("🤝 It's a draw... we're equally matched.")
                            return
            
            # Human's turn
            while True:
                try:
                    position = int(input("Your move (1-9): "))
                    if self.make_human_move(position):
                        break
                except ValueError:
                    print("❌ Please enter a number between 1-9.")
            
            self.print_board()
            
            if self.check_winner() == Player.HUMAN:
                print("😱 You... you actually won?! IMPOSSIBLE!")
                print("I demand a rematch! My code must have a bug...")
                return
            
            if len(self.get_open_positions()) == 0:
                print("🤝 It's a draw... we're equally matched.")
                return
            
            # AI's turn
            if not self.game_history or self.game_history[-1][0] == 'human':
                move = self.make_ai_move()
                print(f"AI plays position {move}\n")
                self.print_board()
                
                if self.check_winner() == Player.AI:
                    quote = random.choice(self.ai_quotes['win'])
                    print(f"🤖 AI: {quote}")
                    return
                
                if len(self.get_open_positions()) == 0:
                    print("🤝 It's a draw... we're equally matched.")
                    return


def main():
    """Main entry point."""
    while True:
        print("\n" + "="*60)
        print("🎮 DIFFICULTY SELECTION 🎮")
        print("="*60)
        print("1. Easy (I'll go easy on you)")
        print("2. Medium (Fair fight)")
        print("3. Impossible (Prepare to lose)")
        
        choice = input("\nSelect difficulty (1-3): ").strip()
        
        difficulty_map = {'1': 'easy', '2': 'medium', '3': 'impossible'}
        difficulty = difficulty_map.get(choice, 'impossible')
        
        game = TicTacToeGame(difficulty=difficulty)
        game.play()
        
        play_again = input("\n🔄 Play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! I'll be back... stronger! 🤖")
            break


if __name__ == "__main__":
    main()
