import tkinter.font as tkFont

def defaultfont():
    font = tkFont.Font(
        family='Helvetica',
        size=12,
        weight='normal',
        slant='italic',
        underline=0,
        overstrike=0
    )
    return font

def header3(family='Modern'):
    font = tkFont.Font(
        family=family,
        size=20,
        weight='normal',
        slant='roman',

    )
    return font

def header2(family='Modern'):
    font = tkFont.Font(
        family=family,
        size=25,
        weight='normal',
        slant='roman',

    )
    return font

def header1(family='Modern'):
    font = tkFont.Font(
        family=family,
        size=35,
        weight='normal',
        slant='roman',

    )
    return font


