import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

user_query = input("What would you like to search for? ")

response = openai.Completion.create(
    model="text-davinci-002",
    prompt=
    "The response is giving a specific shell command that is most relevant to the given query.\n\nQuery: unzip bz2\nResponse: tar -xf\n\nQuery: how to update pacman packages in Arch Linux\nResponse: pacman -Syu\n\nQuery: how to update deb package ubuntu\nResponse: apt-get update && apt-get upgrade\n\nQuery: "
    + user_query + "\nResponse:",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.31,
    presence_penalty=0.15)

# print response
print(response["choices"][0]["text"])