import random, json, sys

gdb = json.load(open('data.json'))

def fillPhrase(phrase, db):
    phrase = phrase.split(' ')
    for i in range(len(phrase)):
        word = phrase[i]
        for j in db['replacers'].keys():
            if phrase[i].startswith(j):
                phrase[i] = phrase[i].replace(j, random.choice(db[db['replacers'][j]]))
                break
    return ' '.join(phrase)

def getPhrase(db):
    return random.choice(db['phrases'])

def generateRandomPhrase(community):
    db = gdb[community]
    return fillPhrase(getPhrase(db), db)

if __name__ == "__main__":
    print(generateRandomPhrase(sys.argv[1]))
