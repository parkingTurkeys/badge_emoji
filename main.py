import os
class App(badge.BaseApp):
    def on_open():
        0
    def loop():
        0


def showEmojis():
    global emoji_list
    emoji_list = os.listdir("imgs")
    emoji_list.shuffle()

def showPBM(name):
    temp = badge.display.import_pbm("imgs/" + name)
