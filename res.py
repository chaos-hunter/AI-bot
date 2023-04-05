import discord
import openai

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
# Set your OpenAI API key
openai.api_key = "API KEY GOES HERE"

from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=intents)


# Create a chat response by providing prompts in the form of messages, and specifying the GPT model to use
def handle_response(message) -> str:
    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # Start the conversation with a system prompt
            {"role": "system", "content": "You are a chatbot"},
            # Ask the user to provide inputs for the cover letter
            {"role": "user", "content": message
             }
        ]
    )

    # Extract the response from ChatGPT
    info = ''

    for choice in ai_response.choices:
        info += choice.message.content
        return info
    print(info)
    print(message)
# Print the response generated by GPT


# def handle_response(message) -> str:
# p_message = message.lower()

# if p_message == 'hello':
# return 'Hello there!'

# if p_message == ('roll a dice' , 'roll') :
# return str(random.randint(1, 6))

# if p_message == 'test!':
# return '👎'

# if p_message == 'annoy!':
# return 'Booo💀'

# if p_message == 'joke':
# return joke.info

# if p_message == 'fortune':
# return Fortune.fortune
