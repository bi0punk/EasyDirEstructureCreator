# PySide 2 
# pip install PySide2
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
app = QApplication(sys.argv)
window = QWidget()
# Resize the Window
window.resize(500, 500)
# Set the Window Title
window.setWindowTitle("PySide2 Window")
# Add Buttons
button = QPushButton("Click Me", window)
button.move(200, 200)
# Add Label Text
label = QLabel("Hello Medium", window)
label.move(200, 150)
# Add Input Box
input_box = QLineEdit(window)
input_box.move(200, 250)
print(input_box.text())
# Add Radio Buttons
radio_button = QRadioButton("Radio Button", window)
radio_button.move(200, 300)
# Add Checkbox
checkbox = QCheckBox("Checkbox", window)
checkbox.move(200, 350)
# Add Slider
slider = QSlider(window)
slider.move(200, 400)
# Add Progress Bar
progress_bar = QProgressBar(window)
progress_bar.move(200, 450)
# Add Image 
image = QLabel(window)
image.setPixmap(QPixmap("image.png"))
# Add Message Box
msg = QMessageBox(window)
msg.setText("Message Box")
msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
window.show()
sys.exit(app.exec())