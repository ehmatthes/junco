import argparse
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal, Vertical

class JuncoApp(App):
    """A Textual app that serves as a simple harness for AI models."""

    CSS_PATH = "junco.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self, project_dir=None):
        """Initialize startup attributes."""
        super().__init__()
        self.project_dir = project_dir
        self.title = f"Junco - {self.project_dir.resolve()}"

    def on_mount(self) -> None:
        """Start junco in light mode."""
        self.theme = "textual-light"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        
        with Horizontal(classes="columns"):
            # Left column.
            with Vertical(classes="rows"):
                yield Static("My messages")
                yield Static("Tool calls")
                yield Static("Alerts")

            # Right column.
            yield Static("Running conversation")
            
        yield Footer()

    def action_toggle_dark(self) -> None:
        """Toggle light and dark mode."""
        if self.theme == "textual-light":
            self.theme = "textual-dark"
        else:
            self.theme = "textual-light"

def main():
    # Define a minimal CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-dir",
        required=True,
        help="Project directory Junco will have access to.")
    args = parser.parse_args()

    # Make sure we're given a directory.
    project_dir = Path(args.project_dir)
    assert project_dir.is_dir()

    # Pass the project directory to the app.
    app = JuncoApp(project_dir)
    app.run()

if __name__ == "__main__":
    main()
