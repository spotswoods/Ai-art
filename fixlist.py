import random

# opening the file in read mode
def selectcharacter():
    with open("characters.txt", "r") as my_file:
        data = my_file.read()
        fix_list = data.replace('\n', ',')
        fix_list = fix_list.split(',')
    return selectrandomoption(fix_list)


def selectadjective():
    with open("adjectives.txt", "r") as my_file:
        data = my_file.read()
        fix_list = data.replace('\n', ',')
        fix_list = fix_list.split(',')
    return selectrandomoption(fix_list)


def addstyle():
    my_file = open("art_style.txt", "r")
    data = my_file.read()
    fix_list = data.replace('\n', ',')
    fix_list = fix_list.split(',')
    my_file.close()
    return selectrandomoption(fix_list)


def createprompt():
    randomtag = random.randrange(1, 5)
    if randomtag == 1:
        print(f"{selectadjective()} {selectcharacter()}, {addstyle()}, 8k")
    elif randomtag < 4:
        print(f"{selectadjective()} {selectcharacter()}, {addstyle()}, {addstyle()}, 8k")
    else:
        print(f"{selectadjective()} {selectcharacter()}, {addstyle()}, {addstyle()}, {addstyle()}, 8k")


def selectrandomoption(list):
    randomseed = random.randrange(len(list))
    answer = list[randomseed]
    return answer.lower()


createprompt()
createprompt()
createprompt()
createprompt()
createprompt()






