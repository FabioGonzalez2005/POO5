from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static

class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("Saludar al mundo", classes="header"),
                Button("Saludar", id="saludar"),
                Button.error("Salir", id="salir"),
            ),
        )

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
    print(app.run())