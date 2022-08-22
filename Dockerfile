FROM python:3.8-slim

WORKDIR /app
# install git and pip3
RUN apt-get update && apt-get install -y git && \
    apt-get install -y python3-pip 

# clone the github repo
RUN git clone https://github.com/mayoayoayo/moonshiner-bot.git

# install requirements
RUN pip3 install -r moonshiner-bot/requirements.txt

#remove .gitignore, readme, and requirements.txt
RUN rm moonshiner-bot/.gitignore moonshiner-bot/README.md moonshiner-bot/requirements.txt

WORKDIR /app/moonshiner-bot
# run the bot
CMD ["python3", "main.py"]