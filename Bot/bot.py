import os
import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def load_env(file_path=".env"):
    """
    Simple manual .env loader.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

# Load configuration
load_env()

# Configure logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AIChatbot:
    """
    A sophisticated AI Chatbot designed for modularity and LLM integration.
    """
    def __init__(self, name=None, max_history=None):
        self.name = name or os.environ.get("BOT_NAME", "GeminiBot")
        self.max_history = int(max_history or os.environ.get("MAX_HISTORY", 10))
        self.context = []
        logger.info(f"{self.name} initialized with max_history={self.max_history}.")

    def get_response(self, user_input: str) -> str:
        """
        Processes user input, stores it in history, and returns a response.
        """
        # Store user input
        self.context.append({"role": "user", "content": user_input})
        
        user_input_lower = user_input.lower().strip()
        
        # Determine response
        if "hello" in user_input_lower or "hi" in user_input_lower:
            response = f"Hello! I am {self.name}. How can I help you today?"
        elif "how are you" in user_input_lower:
            response = "I'm functioning at optimal capacity, thank you for asking!"
        elif "who created you" in user_input_lower:
            response = "I am a product of advanced AI development."
        elif "bye" in user_input_lower:
            response = "Goodbye! Have a great day."
        else:
            response = f"That's an interesting point about '{user_input}'. Could you tell me more?"

        # Store bot response
        self.context.append({"role": "bot", "content": response})

        # Keep history within limits
        if len(self.context) > self.max_history * 2:
            self.context = self.context[-self.max_history * 2:]

        return response

    def run(self):
        """
        Main loop for the chatbot interaction.
        """
        print(f"\n{Fore.CYAN}{Style.BRIGHT}===== {self.name.upper()} STARTED =====")
        print(f"{Fore.YELLOW}Type 'exit' or 'bye' to quit. Type 'history' to see context.\n")
        
        try:
            while True:
                user_input = input(f"{Fore.GREEN}{Style.BRIGHT}You: {Style.RESET_ALL}").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ["exit", "bye", "quit"]:
                    exit_msg = self.get_response('bye')
                    print(f"{Fore.MAGENTA}{Style.BRIGHT}{self.name}: {Style.RESET_ALL}{exit_msg}")
                    break
                
                if user_input.lower() == "history":
                    print(f"\n{Fore.BLUE}--- Conversation History ---")
                    for entry in self.context:
                        if entry["role"] == "user":
                            role = f"{Fore.GREEN}You"
                        else:
                            role = f"{Fore.MAGENTA}{self.name}"
                        print(f"{role}: {Fore.WHITE}{entry['content']}")
                    print(f"{Fore.BLUE}---------------------------\n")
                    continue
                
                response = self.get_response(user_input)
                print(f"{Fore.MAGENTA}{Style.BRIGHT}{self.name}: {Style.RESET_ALL}{response}")
                
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}{self.name}: Session interrupted. Goodbye!")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            print(f"{Fore.RED}{self.name}: I encountered an error. Please try again.")

if __name__ == "__main__":
    # Settings are now automatically loaded from .env or environment variables
    chatbot = AIChatbot()
    chatbot.run()
