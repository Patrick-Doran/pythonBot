# 4 Parts of the polling process
# I. User creates polling question and options
# II. System recieves poll and prints it out, ready for votes
# III. Users send votes and system counts
# IV. User ends poll and relays results

# This file is to be a terminal based version of the bot. It will be translated into discord.py architecture. This is for 
# thought process

class Poll:
    def __init__(self):
        question = ""
        options = []
    def getQuestion():
        print(question)

#creation of myPoll object
myPoll = Poll()

# Part I
myPoll.question = input(f"Enter your question")
num = int(input(f"Enter the number of options"))

#Keep asking for options, store options in array as strings
for x in range(0, num):
    myPoll.options.append(input(f"Enter your option."))

#Part II



#def createPoll():
