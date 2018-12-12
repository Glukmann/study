import urwid


def __init__(self, title, message, entry_prompt=None,
             entry_text='', buttons=[], ring=None):
    button_widgets = []
    for button in buttons:
        button_widgets.append(('pack', button))
    button_columns = urwid.Columns(button_widgets, dividechars=2)
    rows = []
    rows.append(urwid.Text(message))
    if entry_prompt:
        self.entry = MyEdit(entry_prompt, edit_text=entry_text, ring=ring)
        rows.append(self.entry)
    else:
        self.entry = None
    rows.append(urwid.Divider())
    rows.append(button_columns)
    listbox = urwid.ListBox(rows)
    super(ButtonDialog, self).__init__(urwid.LineBox(listbox, title))