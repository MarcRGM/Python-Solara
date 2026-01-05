import solara

clicks = solara.reactive(0)


@solara.component
def Page():
    def increase_clicks():
        clicks.value += 1

    solara.Button(label=f"Clicked {clicks} times", on_click=increase_clicks)
