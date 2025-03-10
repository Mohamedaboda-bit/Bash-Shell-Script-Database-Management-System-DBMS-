import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtCore import QProcess, Qt
from PyQt5.QtGui import QTextCursor

class BashGuiApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up window
        self.setWindowTitle("Database Management System")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("""
    QWidget {
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #121212, stop:1 #1e1e1e);
        color: white;
    }
    QTextEdit {
        background: transparent;
        color: white;
        font-family: monospace;
        font-size: 16px;
        border: none;
    }
    QLineEdit {
        background-color: #333;
        color: white;
        font-size: 16px;
        border: 1px solid #555;
    }
    QPushButton {
        background-color: #007acc;
        color: white;
        font-size: 16px;
        padding: 5px;
        border-radius: 5px;
    }
            QPushButton:hover {
                background-color: #005f99;
            }
        """)

        # Layout
        self.layout = QVBoxLayout()
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet("font-family: monospace; font-size: 16px; color: white;")

        self.input_field = QLineEdit(self)
        self.input_field.returnPressed.connect(self.send_input)

        self.run_button = QPushButton("Start the database system", self)
        self.run_button.clicked.connect(self.run_script)

        # Add widgets
        self.layout.addWidget(self.output_area)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.run_button)
        self.setLayout(self.layout)

        # QProcess to run bash script
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.readyReadStandardError.connect(self.read_output)
        self.process.finished.connect(self.process_finished)

    def run_script(self):
        """Start the Bash script."""
        self.output_area.clear()
        self.append_output("<b style='color:#FFD700;'>Starting Database Management System...</b><br>")  # Gold/Yellow color
        self.process.start("/bin/bash", ["-i", "entryPoint"])  # Interactive mode

    def read_output(self):
        """Capture output from the script and display it."""
        output = self.process.readAllStandardOutput().data().decode()
        error_output = self.process.readAllStandardError().data().decode()
        if output:
            cleaned_output = self.clean_output(output)
            self.format_output(cleaned_output)
        if error_output:
            cleaned_error = self.clean_output(error_output)
            self.format_output(cleaned_error, error=True)

    def clean_output(self, text):
        """Remove ANSI escape sequences."""
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

    def format_output(self, text, error=False):
        """Format output with colors to match the reference image."""
        formatted_text = ""
        for line in text.split("\n"):
            line = line.strip()

            # Colorize menu options (cyan)
            if any(line.startswith(f"{i})") for i in range(1, 10)):
                formatted_text += f"<span style='color:#00FFFF;'>{line}</span><br>"  # Cyan
            
            # Colorize "MAIN MENU >" (Red)
            elif "MAIN MENU" in line:
                formatted_text += f"<span style='color:#FF0000;'><b>{line}</b></span><br>"  # Red
            
            # Colorize user input (`> d1`) (Orange)
            elif line.startswith(">"):
                formatted_text += f"<span style='color:#FFA500;'><b>{line}</b></span><br>"  # Orange
            
            # Normal output text (White)
            else:
                formatted_text += f"{line}<br>"

        if error:
            formatted_text = f"<span style='color:#FF0000;'>{formatted_text}</span>"  # Red for errors

        self.append_output(formatted_text)

    def append_output(self, text):
        """Append formatted output to the text area."""
        self.output_area.moveCursor(QTextCursor.End)
        self.output_area.insertHtml(text)
        self.output_area.moveCursor(QTextCursor.End)
        self.output_area.ensureCursorVisible()

    def send_input(self):
        """Send user input to the Bash script."""
        text = self.input_field.text().strip()
        if text:
            self.append_output(f"<span style='color:#FFA500;'>> {text}</span><br>")  # Orange for user input
            self.process.write((text + "\n").encode())
            self.process.waitForBytesWritten()
            self.input_field.clear()

    def process_finished(self):
        """Handle process completion."""
        self.append_output("<span style='color:gray;'>Process finished.</span>\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BashGuiApp()
    window.show()
    sys.exit(app.exec_())
