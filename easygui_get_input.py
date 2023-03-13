from easygui import *


def get_input(s="question",img=""):
    ans = enterbox(s,image=img)
    return ans


def show(s = 'message'):
    msgbox(s)
