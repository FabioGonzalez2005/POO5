from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static


class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("Saludar al mundo", classes="header"),
                Button("Saludar"),
                Button.error("Salir"),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        ##self.exit(str(event.button))
        self.notify(
            "Desde el IES Haría"
            "[b]El 1º Ciclo del Ciclo Superior[/b] saluda al mundo!",
            title="Saludo",
            severity="warning",
        )


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())