from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button


class ButtonsApp(App[str]):

    def compose(self) -> ComposeResult:
        yield Horizontal(
                Button("Aceptar"),
                Button("Cancelar"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))


if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())