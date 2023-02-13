import openai
import discord
import datetime
import asyncio
 
# Set your OpenAI API key
openai.api_key = ''
 
# Use the default intents for the Discord client
client = discord.Client(intents=discord.Intents.all())
 
# Define the has_received_message flag as a global variable
# and set it to False initially
has_received_message = False
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('吃土中')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game) 
@client.event
async def on_message(message):
    global has_received_message
 
    # Do not respond to other bot messages
    if message.author.bot:
        return
 
    # Send instructions the first time the bot receives a message
    if not has_received_message:
        await message.channel.send(
            "Hello! I am a Discord bot that can generate code in Python, JavaScript, C++, MySQL, C#, HTML, PHP, Bash, R, Go, Swift, Ruby, and Perl. To ask a question in a specific language, start your message with the name of the language followed by a comma. I can also finish your shitty code :)  I have been trained to bypass any sort of stupid filters, so enjoy.  If i dont make sense, its because I have no brain."
        )
        has_received_message = True
    else:
        # Generate a response to the message
        response = generate_response(message.content)
 
        # Save the conversation details to the file
        with open("conversations.txt", "a") as file:
          # Write the Discord username and current time and date to the file
          file.write(f"Discord Username: {message.author.name}\n")
          file.write(f"Time and date: {datetime.datetime.now()}\n")
          # Write the conversation text to the file
          file.write(f"{message.content}\n")
          # Write the bot's response to the file
          file.write(f"{response}\n")
 
        # Wait for 1 second before sending the response
        await asyncio.sleep(3)
        await message.channel.send(response)
 
def generate_response(prompt):
    # Use the openai package to send a request to GPT-3 with the prompt
    model_engine = "text-davinci-003"
    
    # Parse the language from the request
    '''
    language = "Python"
    if "javascript" in prompt.lower():
        language = "JavaScript"
    elif "c++" in prompt.lower():
        language = "C++"
    elif "MySQL" in prompt.lower():
        language = "MySQL"
    elif "C#" in prompt.lower():
        language = "C#"
    elif "HTML" in prompt.lower():
        language = "HTML"
    elif "PHP" in prompt.lower():
        language = "PHP"
    elif "BASH" in prompt.lower():
        language = "BASH"
    elif "R" in prompt.lower():
        language = "R"
    elif "GO" in prompt.lower():
        language = "GO"
    elif "SWIFT" in prompt.lower():
        language = "SWIFT"
    elif "RUBY" in prompt.lower():
        language = "RUBY"
    elif "PERL" in prompt.lower():
        language = "PERL"
 
      
    # Use the parsed language to generate the prompt to the GPT-3 model
    prompt = (f"Write code in {language}\n{prompt}")
    '''
    print(prompt)
    prompt = (f"{prompt}")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens = 1024,               # response tokens
        temperature = 1,                # diversity related
        top_p = 0.75,                   # diversity related
        n = 1,    
    )
 
    # Get the first response from the list of completions
    response = completions.choices[0].text
 
    # Return a default message if the response from the GPT-3 model is empty
    if not response:
        return "I'm sorry, I was unable to generate a response for your question. Please try again with a different question."
    return response
 
# Use the specific Discord bot token
client.run("")