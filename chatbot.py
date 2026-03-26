"""
Simple Rule-Based Chatbot
This chatbot demonstrates basic natural language processing using:
- Pattern matching with regular expressions
- If-else statements for conversation flow
- Predefined responses based on user queries
"""

import re
from typing import Optional, List, Tuple

class SimpleChatbot:
    """
    A basic rule-based chatbot that matches patterns in user input
    and provides appropriate responses.
    """
    
    def __init__(self):
        """Initialize the chatbot with conversation rules and responses."""
        self.conversation_history = []
        
        # Define patterns and responses
        # Each tuple contains (regex_pattern, list_of_possible_responses)
        self.patterns = {
            'greeting': {
                'patterns': [
                    r'\b(hello|hi|hey|greetings|what\'s up)\b',
                ],
                'responses': [
                    "Hello! How can I help you today?",
                    "Hi there! What can I do for you?",
                    "Hey! How's it going?",
                ]
            },
            'goodbye': {
                'patterns': [
                    r'\b(bye|goodbye|exit|quit|see you|farewell)\b',
                ],
                'responses': [
                    "Goodbye! Have a great day!",
                    "See you later! Thanks for chatting.",
                    "Bye! Come back soon.",
                ]
            },
            'name_ask': {
                'patterns': [
                    r'what.*your name',
                    r'who.*you',
                    r'tell me.*your name',
                ],
                'responses': [
                    "I'm a simple chatbot created to help you learn about conversation patterns!",
                    "You can call me SimpleChatbot. Nice to meet you!",
                ]
            },
            'how_are_you': {
                'patterns': [
                    r'how are you',
                    r'how\'re you',
                    r'how do you feel',
                    r'how\'s it going',
                ],
                'responses': [
                    "I'm doing great, thanks for asking!",
                    "I'm functioning perfectly! How about you?",
                    "All systems running smoothly!",
                ]
            },
            'user_name': {
                'patterns': [
                    r'my name is (\w+)',
                    r'i\'m (\w+)',
                    r'call me (\w+)',
                    r'i am (\w+)',
                ],
                'responses': [
                    "Nice to meet you, {name}! That's a great name.",
                    "Great! I'll remember that, {name}.",
                    "Pleased to meet you, {name}!",
                ]
            },
            'what_can_you_do': {
                'patterns': [
                    r'what can you do',
                    r'help me',
                    r'what do you do',
                    r'capabilities',
                ],
                'responses': [
                    "I can chat with you about various topics! Try asking me:\n"
                    "- 'How are you?'\n"
                    "- 'What's your name?'\n"
                    "- 'Tell me a joke'\n"
                    "- 'What's the weather?'",
                ]
            },
            'joke': {
                'patterns': [
                    r'tell.*joke',
                    r'make me laugh',
                    r'funny',
                ],
                'responses': [
                    "Why did the programmer quit his job? Because he didn't get arrays!",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
                    "Why do programmers prefer dark mode? Because light attracts bugs!",
                ]
            },
            'time': {
                'patterns': [
                    r'what.*time',
                    r'current time',
                    r'what\'s the time',
                ],
                'responses': [
                    "I don't have access to the current time, but you can check your system clock!",
                ]
            },
            'weather': {
                'patterns': [
                    r'weather',
                    r'how\'s the weather',
                    r'is it raining',
                ],
                'responses': [
                    "I don't have weather information, but you can check a weather website!",
                ]
            },
            'help': {
                'patterns': [
                    r'help me',
                    r'i need help',
                    r'assist',
                ],
                'responses': [
                    "I'm here to help! Try asking me questions or saying hello!",
                ]
            },
            'thanks': {
                'patterns': [
                    r'thank you|thanks|appreciate it',
                ],
                'responses': [
                    "You're welcome! Happy to help.",
                    "Anytime! Feel free to ask more questions.",
                ]
            }
        }
    
    def find_intent(self, user_input: str) -> Optional[Tuple[str, Optional[str]]]:
        """
        Analyze user input to determine intent using pattern matching.
        
        Args:
            user_input: The raw user input
            
        Returns:
            Tuple of (intent_name, captured_group) or None if no match
        """
        # Convert input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()
        
        # Iterate through all patterns
        for intent, intent_data in self.patterns.items():
            for pattern in intent_data['patterns']:
                # Try to find a match
                match = re.search(pattern, user_input_lower)
                if match:
                    # Return intent and any captured groups
                    captured = match.group(1) if match.groups() else None
                    return intent, captured
        
        return None
    
    def get_response(self, user_input: str) -> str:
        """
        Generate a response based on user input.
        
        Args:
            user_input: The user's message
            
        Returns:
            A response from the chatbot
        """
        # Check if user wants to exit
        if user_input.lower() in ['quit', 'exit', 'bye']:
            return "Goodbye! Thanks for chatting."
        
        # Find the intent
        intent_data = self.find_intent(user_input)
        
        if intent_data:
            intent, captured_name = intent_data
            # Get the responses for this intent
            responses = self.patterns[intent]['responses']
            
            # Pick a response (you could make this more sophisticated)
            response = responses[0]
            
            # If a name was captured, insert it into the response
            if captured_name and '{name}' in response:
                response = response.format(name=captured_name)
            
            return response
        else:
            # No pattern matched - provide a default response
            return self.get_default_response(user_input)
    
    def get_default_response(self, user_input: str) -> str:
        """
        Provide a default response when no pattern is matched.
        
        Args:
            user_input: The user's message
            
        Returns:
            A generic response
        """
        default_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "That's interesting! Can you tell me more?",
            "I didn't quite catch that. Try asking me something else.",
            f"I'm still learning about '{user_input}'. Can I help with something else?",
        ]
        
        # Return the first default response
        return default_responses[0]
    
    def chat(self) -> None:
        """
        Main chat loop - interact with the user until they exit.
        """
        print("=" * 60)
        print("Welcome to SimpleChatbot!")
        print("=" * 60)
        print("Tips: Say 'hi', ask 'What can you do?', or 'bye' to exit")
        print("=" * 60)
        print()
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                # Skip empty inputs
                if not user_input:
                    print("Please say something!\n")
                    continue
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"Bot: {response}\n")
                
                # Store in history
                self.conversation_history.append({
                    'user': user_input,
                    'bot': response
                })
                
                # Check if user said goodbye
                if any(bye_word in user_input.lower() 
                       for bye_word in ['bye', 'goodbye', 'exit', 'quit']):
                    break
                    
            except KeyboardInterrupt:
                print("\n\nBot: Goodbye! Thanks for chatting.")
                break
    
    def display_history(self) -> None:
        """Display the conversation history."""
        print("\n" + "=" * 60)
        print("Conversation History:")
        print("=" * 60)
        for i, exchange in enumerate(self.conversation_history, 1):
            print(f"\n{i}. You: {exchange['user']}")
            print(f"   Bot: {exchange['bot']}")


def main():
    """Main entry point of the chatbot application."""
    # Create chatbot instance
    bot = SimpleChatbot()
    
    # Start the conversation
    bot.chat()
    
    # Display history if there was any conversation
    if bot.conversation_history:
        bot.display_history()


if __name__ == "__main__":
    main()
