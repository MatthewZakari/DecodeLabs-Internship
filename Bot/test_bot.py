import unittest
from Bot.bot import AIChatbot

class TestAIChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = AIChatbot(name="TestBot", max_history=2)

    def test_history_storage(self):
        self.bot.get_response("Hello")
        self.bot.get_response("How are you?")
        
        # Check if context has 4 entries (2 pairs of user-bot)
        self.assertEqual(len(self.bot.context), 4)
        self.assertEqual(self.bot.context[0]["role"], "user")
        self.assertEqual(self.bot.context[0]["content"], "Hello")
        self.assertEqual(self.bot.context[1]["role"], "bot")
        
    def test_history_limit(self):
        # max_history is 2, so max 4 entries
        self.bot.get_response("1")
        self.bot.get_response("2")
        self.bot.get_response("3")
        
        self.assertEqual(len(self.bot.context), 4)
        self.assertEqual(self.bot.context[0]["content"], "2")
        self.assertEqual(self.bot.context[2]["content"], "3")

if __name__ == "__main__":
    unittest.main()
