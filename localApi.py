import json
import secrets
import sys

gdb = json.load(open("data.json"))


def fillPhrase(phrase, db):
    phrase = phrase.split(" ")
    for i in range(len(phrase)):
        for j in db["replacers"].keys():
            if phrase[i].startswith(j):
                replacives = db[db["replacers"][j]]
                current_phrase = " ".join(phrase)
                to_replace_with = secrets.choice(replacives)
                if to_replace_with not in current_phrase:
                    phrase[i] = phrase[i].replace(j, to_replace_with)
                    break
                else:
                    replacives.remove(to_replace_with)
                    phrase[i] = phrase[i].replace(j, secrets.choice(replacives))
                    break
    return " ".join(phrase)


def getPhrase(db):
    return secrets.choice(db["phrases"])


def generateRandomPhrase(community):
    db = gdb[community]
    return fillPhrase(getPhrase(db), db)


if __name__ == "__main__":
    print(generateRandomPhrase(sys.argv[1]))
