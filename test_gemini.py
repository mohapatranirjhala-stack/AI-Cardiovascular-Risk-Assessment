from src.Heart.ai.gemini_chat import GeminiHealthAssistant

bot = GeminiHealthAssistant()

print(bot.ask("What is BMI?"))