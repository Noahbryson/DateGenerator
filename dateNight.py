from datetime import datetime
from PySide6.QtWidgets import QApplication
import os
from pathlib import Path
from DateGenerator import DateGenerator
from DateGUI import DateGUI

if __name__ == "__main__":
    app = QApplication([])
    userPath = os.path.expanduser('~') #gets path to user on any computer
    filePath = userPath  + "\Box\sam_And_Noah\sam-noah-stl-adventure-goals.xlsx"
    now = datetime.now()
    Today = now.strftime("%m/%d/%Y")
    dateNight = DateGenerator(filePath=filePath)
    widget = DateGUI(dateTime=Today, dateNight=dateNight, app=app)
    widget.show()
    app.exec()