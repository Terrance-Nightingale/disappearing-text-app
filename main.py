from tkinter import *
from tkinter import ttk
# TODO Add a text entry box for typing
# TODO Add a 5 second timer that resets back to 5 whenever the user types
#     -This will be a bar that updates in length and turns more red as time passes.

BAR_COLOR = '#cc2342'
TROUGH_COLOR = '#ccc8c9'
SECONDS = 5 * 10

window = Tk()
window.title("Disappearing Text")
window.minsize(width=600, height=700)
window.config(padx=50, pady=20)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, darkcolor=BAR_COLOR, lightcolor=BAR_COLOR,
            foreground=BAR_COLOR, background=BAR_COLOR)

progressbar = ttk.Progressbar(window, style="red.Horizontal.TProgressbar", length=500, maximum=100, value=0)
progressbar.step(0.5)
progressbar.pack()
progressbar.start(SECONDS)
while progressbar['value'] != progressbar['maximum'] - 0.5:
    window.update()

progressbar.stop()

window.mainloop()
