from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class JuncoApp(App):
    """A Textual app that serves as a simple harness for AI models."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Toggle light and dark mode."""
        if self.theme == "textual-light":
            self.theme = "textual-dark"
        else:
            self.theme = "textual-light"

def main():
    app = JuncoApp()
    app.run()

if __name__ == "__main__":
    main()
