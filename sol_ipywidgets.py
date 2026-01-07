import ipywidgets as widgets
import solara

clicks = 0

print("I get run at startup, and for every page request")

def on_click(button):
    global clicks
    clicks += 1
    button.description = f"Clicked {clicks} times"



button = widgets.Button(description="Clicked 0 times")
button.on_click(on_click)

# solara run sol-ipywidgets.py:button
# The :button part on the command line tells the Solara server the variable name of the widget it should render. 
# The default name for a widget variable Solara will look for is page.

page = widgets.VBox(
    [
        button,
        # using .widget(..) we can create a classic ipywidget from a solara component
        solara.FileDownload.widget(data="some text data", filename="solara-demo.txt"),
    ]
)

# For every page request (for instance, you open a second tab, or do a page refresh) you will see the same text printed out in the terminal. This tell you that each "tab" gets its own run, and its own namespace, which means that the clicks variable is not shared between multiple users.

# If you refresh the page, the script is executed again, and the clicks is set to 0 again.

# solara.Button is a reactive UI component for building deployable Solara apps, 
# while ipywidgets.Button is an event-driven widget mainly for direct use inside Jupyter notebooks.