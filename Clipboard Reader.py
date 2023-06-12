import pyttsx3
import pyperclip
from PyQt5 import QtWidgets, QtCore

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Create a Qt application
app = QtWidgets.QApplication([])

# Create a Qt label to display the program description and instructions
label = QtWidgets.QLabel(
    "Clipboard Reader\n\n"
    "This program allows you to listen to the contents of your clipboard.\n\n"
    "Instructions:\n"
    "1. Copy some text to your clipboard.\n"
    "2. Click the 'Read Clipboard' button to listen to the copied text.\n\n"
    "Note: Make sure your speakers or headphones are connected and turned on.\n"
)
label.setWordWrap(True)
label.setAlignment(QtCore.Qt.AlignCenter)

# Create a Qt button to trigger text-to-speech conversion
button = QtWidgets.QPushButton("Read Clipboard")

# Define the button click event handler
def read_clipboard():
    # Get the contents of the clipboard
    text = pyperclip.paste()

    # Use pyttsx3 to convert the text to speech
    engine.say(text)
    engine.runAndWait()

# Connect the button click event to the handler
button.clicked.connect(read_clipboard)

# Create a Qt widget to hold the label and button
widget = QtWidgets.QWidget()

# Create a Qt layout and add the label and button to it
layout = QtWidgets.QVBoxLayout(widget)
layout.addWidget(label)
layout.addWidget(button)

# Create a Qt main window and set the widget as its central widget
window = QtWidgets.QMainWindow()
window.setWindowTitle("Clipboard Reader")
window.setCentralWidget(widget)

# Show the main window
window.show()

# Run the Qt application
app.exec_()

