import solara
@solara.component
def Layout(children=[]):
    # 1. STYLE ENGINE FIRST (The "Environment")
    with solara.lab.Tailwind():
        
        # 2. THEME SECOND (The "Colors")
        with solara.lab.Theme(dark=True):
            
            # 3. STRUCTURE THIRD (The "Frame")
            return solara.AppLayout(
                children=children,
                navigation=True,
                title="My App",
                # The AppLayout can now use Tailwind classes
                classes=["border-b-2", "border-indigo-500"] 
            )
