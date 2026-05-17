class AIChatbot:
    def __init__(self):
        # Map multiple triggers to the same response
        self.responses = {
            "hello": "Hello! Nice to meet you.",
            "hi": "Hello! Nice to meet you.",
            "hey": "Hello! Nice to meet you.",
            "how are you": "I'm doing great!",
            "what is your name": "I am a Rule-Based AI Chatbot.",
            "who created you": "I was created by Matthew.",
            "bye": "Goodbye!"
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        return self.responses.get(user_input, "Sorry, I don't understand that.")

    def run(self):
        print("===== RULE-BASED AI CHATBOT =====")
        print("Type 'bye' to exit.\n")
        
        while True:
            user_input = input("You: ")
            response = self.get_response(user_input)
            print(f"Bot: {response}")
            
            if user_input.lower().strip() == "bye":
                break

if __name__ == "__main__":
    chatbot = AIChatbot()
    chatbot.run()
