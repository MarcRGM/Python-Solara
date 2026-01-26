import solara
from multipage._utils.shared import SharedComponent


@solara.component
def Page():
    with solara.Sidebar():
        solara.Markdown("This is the sidebar at the home page!")
    with solara.Card("Home"):
        solara.Markdown("This is the home page")
        SharedComponent()