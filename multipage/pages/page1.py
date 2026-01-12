import solara

from multipage.shared import SharedComponent


@solara.component
def Sub():
    with solara.Card("Sub component", margin=0, classes=["my-2"]):
        solara.Markdown("This sub component is the best")
        with solara.Sidebar():
            with solara.Card("Sidebar of sub component", margin=0, elevation=0):
                solara.Markdown("*Markdown* **is** 👍")
            SharedComponent()


@solara.component
def Page():
    with solara.Sidebar():
        with solara.Card("Sidebar of page 1", margin=0, elevation=0):
            solara.Markdown("Hi there 👋!")
    with solara.Card("Page 1"):
        Sub()
        solara.Markdown("Page 1 is the best")