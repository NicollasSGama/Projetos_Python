from PySimpleGUI import (
    Text, Input, Button,
    Multiline, Canvas,
    Table, CalendarButton,
    Window, WIN_CLOSED,
    popup_get_text, Frame,
    Column, Combo, Push,
    theme, VSeparator,
    HSeparator
)

tema = 'LightBlue2'


def tabela():
    theme(tema)
    layout = [
        [
            Table
        ]
    ]
