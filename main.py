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

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# read prompt file

# get user query

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="The Command is giving a specific shell command that is most relevant to the given query.\n\nQuery: unzip bz2\nCommand: tar -xf\n\nQuery: how to update pacman packages in Arch Linux\nCommand: pacman -Syu\n\nQuery: how to update deb package ubuntu\nCommand: apt-get update && apt-get upgrade\n\nQuery: paru uninstall\nCommand: paru -R\n\nQuery: terraform show outputs\nCommand: terraform output\n\nQuery: write \"hello world\" in ascii art\nCommand: echo -e \"hello world\" | figlet\n\nQuery: initialize a new git repository\nCommand: git init\n\nQuery: git remove dist dir\nCommand: git rm -r --cached dist\n\nQuery: git undo\nCommand: git reset HEAD~1\n\nQuery: new docker image\nCommand: docker build -t myimage .\n\nQuery: filter duplicate files\nCommand: fdupes -r -d -N .\n\nQuery: new git submodule\nCommand: git submodule add <url> <path>\n\nQuery: reinstall youtube-dl with brew\nCommand: brew reinstall youtube-dl\n\nQuery: loop over all jpgs in folder\nCommand: for i in *.jpg; do echo $i; done\n\nQuery: clone a repo\nCommand: git clone <repository-url>\n\nQuery: commit staged changes\nCommand: git commit -m \"message\"\n\nQuery: delete eks cluster with awscli\nCommand: aws eks delete-cluster --name <cluster_name>\n\nQuery: list eks clusters with awscli\nCommand: aws eks list-clusters\n\nQuery: login to awscli\nCommand: aws configure\n\nQuery: get eks status with awscli\nCommand: aws eks describe-cluster --name <cluster_name>\n\nQuery: copy ssh public key to remote server via ssh\nCommand:  ssh-copy-id user@server\n\nQuery: how to disable sudo prompt for local user\nCommand: sudo visudo $USER ALL=(ALL) NOPASSWD: ALL\n\nQuery: add pip install path to .bashrc\nCommand: export PATH=$HOME/.local/bin:$PATH\n\nQuery: change default editor on arch for visudo to vim\nCommand: sudo EDITOR=vim visudo\n\nQuery: how to install pip\nCommand: curl https://bootstrap.pypa.io/get-pip.py -o get-pip\n\nQuery: add \"$HOME/.local/bin\" to .bashrc in a one-line command\nCommand: echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc\n\nQuery: add \"$HOME/bin\" to bashrc in a one-line command\nCommand: echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc\n\nQuery: add alias for ls -> lsd to .zshrc in a one-line command\nCommand: echo 'alias ls=\"lsd\"' >> ~/.zshrc\n\nQuery: print global git config\nCommand: git config --global --list\n\nQuery: edit global git config\nCommand: git config --global --edit\n\nQuery: " + user_query + "\nCommand:",
  temperature=0,
  max_tokens=250,
  top_p=1,
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
