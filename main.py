import os
import openai
import argparse
from dotenv import load_dotenv

# parse arguments
parser = argparse.ArgumentParser(description='OpenAI Codex CLI cheatsheet')
parser.add_argument('-t', '--temp', default=0.0, type=float, help='Codex model temperature (randomness)')
parser.add_argument('-n', '--num', default=1, type=int, help='Number of codex predictions to return')
args = parser.parse_args()

user_temp = args.temp
user_num = args.num

# load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# read prompt file
prompt_file = "prompts"
prompt_input = "".join(open(prompt_file))

# get user query
user_query = input("Query: ")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt=prompt_input + user_query + "\nCommand:",
  temperature=user_temp,
  max_tokens=250,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["Query", "\n"],
  n=user_num,
)

if user_num == 1:
  cheat_answer = response["choices"][0]["text"].strip()
  print(cheat_answer)
else:
  cheat_answer = "\n".join([choice["text"].strip() for choice in response["choices"]])
  # make user_num bold and red
  user_num = "\033[1;31m" + str(user_num) + "\033[0m"
  print(f"You generated {user_num} completions with temperature {str(user_temp)}: \n{cheat_answer}")
