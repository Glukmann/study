import urwid
from urwid import MainLoop, SolidFill, LineBox

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def question():
    return urwid.Pile([urwid.Edit(('I say', u"What is your name?\n"))])

def answer(name):
    return urwid.Text(('banner', u"Nice to meet you, " + name + "\n"))

class ConversationListBox(urwid.ListBox):
    def __init__(self):
        body = urwid.SimpleFocusListWalker([question()])
        super(ConversationListBox, self).__init__(body)

    def keypress(self, size, key):
        key = super(ConversationListBox, self).keypress(size, key)
        if key != 'enter':
            return key
        name = self.focus[0].edit_text
        if not name:
            raise urwid.ExitMainLoop()
        # replace or add response
        txt = answer(name)
        map1 = urwid.AttrMap(txt, 'streak')
        fill = urwid.Filler(map1)
        map2 = urwid.AttrMap(fill, 'bg')
        self.focus.contents[1:] = [(map2, self.focus.options())]
        pos = self.focus_position
        # add a new question
        self.body.insert(pos + 1, question())
        self.focus_position = pos + 1

palette = [('I say', 'default,bold', 'default'),
           ('banner', 'black', 'light gray'),
           ('streak', 'black', 'dark red'),
           ('bg', 'black', 'dark blue'),]



# loop = urwid.MainLoop(ConversationListBox(), palette, unhandled_input=exit_on_q)
# loop.run()
