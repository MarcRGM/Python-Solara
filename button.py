import solara

clicks = solara.reactive(0)

@solara.component
def Page():
    color = "green"

    if clicks.value >= 5:
        color = "red"
    
    def increment():
        clicks.value += 1
        print("Clicks", clicks)

    def reset():
        clicks.value = 0
        print("Clicks have been reset")

    with solara.VBox():
        solara.Text(f"Clicks: {clicks.value}")
        with solara.HBox():
            solara.Button(Label="Increment", on_click=increment, color=color)
            solara.Button(Label="Reset", on_click=reset, color="gray")

    