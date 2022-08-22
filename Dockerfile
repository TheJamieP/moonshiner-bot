FROM python:3.8-slim

WORKDIR /app
# install git and pip3
RUN apt-get update && apt-get install -y git && \
    apt-get install -y python3-pip 

# clone the github repo
RUN git clone https://github.com/mayoayoayo/moonshiner-bot.git

# cd to the repo and install requirements
RUN cd moonshiner-bot && pip3 install -r requirements.txt
# clean up the repo and remove the .gitignore and readme.md and requirements.txt
RUN rm -rf .git && rm -rf moonshiner-bot/{.gitignore,readme.md,requirements.txt}

WORKDIR /a/moonshiner-bot

# run the bot in the directory src/main.py

RUN python3 src/main.py