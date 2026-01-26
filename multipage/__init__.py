import solara

import multipage.home as home
import multipage.page1 as page1
import multipage.page2 as page2

routes = [
    solara.Route(path="/", component=home.Page, label="Home"),
    solara.Route(path="page1", component=page1.Page, label="Page 1"),
    solara.Route(path="page2", component=page2.Page, label="Page 2"),
]

@solara.component
def Layout(children=[]):
    return solara.AppLayout(
        children=children,
        navigation=True,  # This will now display the tabs
        title="My Multi-Page App"
    )
