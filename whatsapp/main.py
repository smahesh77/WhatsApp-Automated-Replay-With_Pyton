import pyautogui as pt
from time import sleep
import pyperclip
import random
def click(g):
    pt.doubleClick(g)
whatsapp = (353, 298)
mini=(1135,179)
reply=(471,910)
copy=(482,924)
typebox=(537,994)
paste=(567,883)
name=(520,98)
name2=(464,462)
copy2=(516,485)
close=(430,99)
newc=(484,928)
#color=(38,45,49)
#sleep(5)
#click(whatsapp)
#sleep(5)
#this returs the senders message
def val(mes):
    sleep(3)
    p=str(mes).lower()
    if "sad" in p or "saad" in p:
        return "no, I'm happy"
    elif "good" in p:
        return "what makes you think its bad"
    elif "nice" in p:
        return "dont say nice it sucks"
    elif "cool" in p:
        return "thats not cool"
    elif "streamer" in p:
        return "streamers suck"
    elif "now" in p:
        return "yes"
    elif "yes" in p:
        return "no"
    elif "sucks" in p:
        return "no you suck"
    elif "mo" in p:
        return "are you a cow"
    elif "no" in p:
        return "yes"
    elif "this" in p:
        return "ya that seems good"
    elif "bad" in p:
        return "no its good"
    elif "hi" in p:
        return "hello how are you doing"
    elif "haya" in p:
        return "spell hey correctly"
    else:
        return "ya okay, please stop watching bts"
def sud(mes):
    p=str(mes).lower()
    if "hi" in p:
        return "hello"
#checks who has sent the message
def assign(name):
    if "valorant" in name.lower():
        return val(getmes())
def getmes():
    pt.tripleClick(reply)
    pt.rightClick()
    pt.click(copy)
    j=pyperclip.paste()
    print("message received:",j)
    return j
#this will get the name of the sender
def uname():
    click(name)
    sleep(1)
    pt.tripleClick(name2)
    pt.rightClick()
    pt.click(copy2)
    j = pyperclip.paste()
    print("message from:",j.lower())
    pt.click(close)
    return j
#this checks for new messages
def namee(nam):
    return nam
def checker():
    while True:
        try:
            pos=pt.locateOnScreen("whatsapp/greendot.png",confidence=.7)
            sleep(3)
            print("scanning for active chats....")
            if pos is not None:
                print("found one")
                pt.moveTo(pos)
                pt.moveRel(-100,0)
                pt.click()
                sleep(1)
        except(Exception):
            print("there was a error")
        try:
            if pt.pixelMatchesColor(newc[0], newc[1], (38, 45, 49), tolerance=10):
                print("new message found")
                print("auto reply initiated...  ")
                sleep(1)
                post(val(getmes()))
        except(Exception):
            print("error in processing, retrying...")
#posts our automated reply
def post(mes):
    click(typebox)
    #pt.typewrite("This is an automated reply:")
    pt.press("enter")
    pt.typewrite(mes)
    pt.press("enter")
def process(mes):
    p=str(mes).lower()
    if "hi" in p and "?" in p:
        return "sorry, I dont know"
    if "hi" in p:
        return "hello"
    if "?" in p:
        return "i dont know"
checker()

"""
(x=353, y=his is an automated reply:
yes
)
(x=1135, y=179)
(x=447, y=994)
(x=471, y=910)
(x=482, y=924)
(x=537, y=994)
"""