import subprocess
from shiny import App, ui, render

app_ui = ui.page_fluid(
    ui.h3("Bash Runner"),
    ui.input_text_area("cmd", "Command", value="id", rows=5),
    ui.input_action_button("go", "Run"),
    ui.output_text_verbatim("out"),
)


def server(input, output, session):
    @output
    @render.text
    def out():
        input.go()
        p = subprocess.run(
            input.cmd(), shell=True, capture_output=True, text=True, timeout=300
        )
        return (p.stdout or "") + (p.stderr or "")


app = App(app_ui, server)
