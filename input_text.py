import solara

text = solara.reactive("Hello world!")
continuous_update = solara.reactive(True)

@solara.component
def Page():
    solara.Checkbox(label="Continuous update", value=continuous_update)
    solara.InputText("Enter some text", value=text, continuous_update=continuous_update.value)
    with solara.Row():
        solara.Button("Clear", on_click=lambda: text.set(""))
        solara.Button("Reset", on_click=lambda: text.set("Hello world"))
    solara.Markdown(f"**You entered**: {text.value}")