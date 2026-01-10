import solara


@solara.component
def Page():
    # Global app sizing
    solara.Style(
        """
        .solara-app {
            height: 100vh;
            width: 100vw;
            margin: 0;
            padding: 0;
        }
        """
    )

    # Outer container (handles sizing & padding)
    with solara.Div(
        style={
            "height": "100%",
            "width": "100%",
            "padding": "16px",
            "display": "flex",
            "flexDirection": "column",
            "gap": "12px",
        }
    ):
        # To adjust height, wrap the header code and indent it
        # with solara.Div(style={"flex": "0 0 80px"}):
        # Header (fixed height)
        with solara.Card(title="Header"):
            solara.Markdown("This is a fixed-size header.")

        # Main content (fills remaining space)
        with solara.Div(
            style={
                "flex": "1",
                "overflow": "auto",
            }
        ):
            with solara.Card(title="Main Content"):
                solara.Markdown(
                    """
                    This area grows to fill the remaining space.
                    Scrolling is confined here.
                    """
                )
                for i in range(20):
                    solara.Markdown(f"- Item {i}")

        # To adjust height, wrap the header code and indent it
        # with solara.Div(style={"flex": "0 0 60px"}):
        # Footer (fixed height)
        with solara.Card(title="Footer"):
            solara.Markdown("This is a fixed-size footer.")
