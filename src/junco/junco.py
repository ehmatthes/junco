from textual.app import App, ComposeResult
from textual.widgets import Header

class JuncoApp(App):
    """A Textual app that serves as a simple harness for AI models."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()

if __name__ == "__main__":
    app = JuncoApp()
    app.run()
