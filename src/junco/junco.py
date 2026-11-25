import argparse
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal, Vertical

class JuncoApp(App):
    """A Textual app that serves as a simple harness for AI models."""

    CSS_PATH = "junco.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self, project_dir):
        """Initialize startup attributes."""
        super().__init__()
        self.project_dir = project_dir
        self.title = f"Junco - {self.project_dir}"

    def on_mount(self) -> None:
        """Start junco in light mode."""
        self.theme = "textual-light"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        
        with Horizontal(classes="columns"):
            # Left column.
            with Vertical(classes="rows"):
                self.prompt_box = Static()
                self.prompt_box.border_title = "My messages"
                yield self.prompt_box

                self.tool_call_box = Static()
                self.tool_call_box.border_title = "Tool calls"
                yield self.tool_call_box

                self.alert_box = Static()
                self.alert_box.border_title = "Alerts"
                yield self.alert_box

            # Right column.
            self.running_conv_box = Static()
            self.running_conv_box.border_title = "Running conversation"
            yield self.running_conv_box
            
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
    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.is_dir():
        msg = f"{project_dir} is not a valid directory."
        parser.error(msg)

    # Pass the project directory to the app.
    app = JuncoApp(project_dir)
    app.run()

if __name__ == "__main__":
    main()
