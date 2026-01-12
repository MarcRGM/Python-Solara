import solara

# some app state that outlives a single page
app_state = solara.reactive(0)

@solara.component
def SharedComponent():
    with solara.Card("Shown on each page", style={"max-width": "500px"}, margin=0, classes=["my-2"]):
        solara.Markdown(
            f"""
            This component will be used on each page.

            It uses the `app_state` [reactive variable](https://solara.dev/documentation/api/utilities/reactive)
            so that the state outlives each page


            app_state: {app_state.value}
            """
        )
        solara.Button(label="Increment app_state", icon_name="mdi-plus", on_click=lambda: app_state.set(app_state.value + 1), outlined=True)
