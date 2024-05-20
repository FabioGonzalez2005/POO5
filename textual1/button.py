from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static, Footer

class ButtonsApp(App):
    CSS_PATH = "button.tcss"

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="delete", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),
    ]

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("Saludar al mundo", classes="header"),
                Button("Saludar", id="saludar"),
                Button.error("Salir", id="salir"),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "saludar":
            self.notify(
                "Desde el IES Haría\n[b]El 1º Ciclo del Ciclo Superior[/b] saluda al mundo!",
                title="Saludo",
                severity="warning",
            )
        elif event.button.id == "salir":
            self.exit("Saliendo")

if __name__ == "__main__":
    app = ButtonsApp()
    app.run()
