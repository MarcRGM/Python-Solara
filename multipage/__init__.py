import solara
import solara.lab
from multipage.pages import home, page1, page2

@solara.component
def Layout(children=[]):
    # Get current routing information
    route, routes = solara.use_route()
    
    with solara.AppLayout(title="My Application"):
        with solara.AppBar():
            # This creates the upper tabs manually
            with solara.lab.Tabs(
                value=0 if route is None or route.path == "/" else ["page1", "page2"].index(route.path) + 1
            ):
                solara.lab.Tab("Home", icon_name="mdi-home", path_or_route="/")
                solara.lab.Tab("Page 1", path_or_route="/page1")
                solara.lab.Tab("Page 2", path_or_route="/page2")
        
        # Render the current page content
        solara.Column(children=children)

# Define routes globally so Solara knows which components to render at which URL
routes = [
    solara.Route(path="/", component=home.Page),
    solara.Route(path="page1", component=page1.Page),
    solara.Route(path="page2", component=page2.Page),
]
