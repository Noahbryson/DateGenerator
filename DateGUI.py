import PySide6.QtGui as Qt
from PySide6.QtGui import *
from PySide6.QtCore import QTimer, Signal
from PySide6.QtWidgets import *
from DateGenerator import DateGenerator

class DateGUI(QWidget):
    def __init__(self, 
        dateTime,
        dateNight : DateGenerator,
        app: QApplication):

        super(DateGUI,self).__init__()
        # self.initUI()
        self.dateNight = dateNight
        self.displayFont = QFont()
        self.displayFont.setPointSize(70)
        self.setWindowTitle('Date Night %s' % dateTime)

        """Layouts"""
        self.mainLayout = QVBoxLayout()
        self.functions = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.checkBoxLayout = QHBoxLayout()

        """Brush"""
        self.brush = QBrush(QColor('Black'))

        """Text Widget"""
        self.scene = QGraphicsScene()
        self.text = QGraphicsTextItem('Select Date Options')
        self.text.setDefaultTextColor(QColor('White'))
        self.text.setFont(self.displayFont)
        self.scene.addItem(self.text)
        self.view = QGraphicsView(self.scene)
        self.scene.setBackgroundBrush(self.brush)
        # self.view.setSceneRect(-425.500000, -389.500000, 1450.500000, 920.000000)
        """Checkbox Widgets"""
        self.modes = QButtonGroup()
        self.eating = QCheckBox('Eating?', self)
        self.eating.setChecked(False)
        self.eating.setFixedHeight(80)
        self.drinking = QCheckBox("Drinking?", self)
        self.drinking.setChecked(False)
        self.drinking.setFixedHeight(80)
        self.activitiy = QCheckBox("Activity?", self)
        self.activitiy.setChecked(False)
        self.activitiy.setFixedHeight(80)
        self.travel = QCheckBox('Travel?', self)
        self.travel.setChecked(False)
        self.travel.setFixedHeight(80)
        self.modes.addButton(self.eating)
        self.modes.addButton(self.drinking)
        self.modes.addButton(self.activitiy)
        self.modes.addButton(self.travel)
        self.modes.setExclusive(False)
        self.modes.buttonClicked.connect(self.checkCheckBoxes)
        """Button Widgets"""
        self.generateButton = QPushButton("Create Date")
        self.generateButton.setFixedHeight(100)
        # self.generateButton.setFixedWidth(500)
        self.generateButton.pressed.connect(self.generateDate)
        """Add Widgets to Layouts"""
        self.checkBoxLayout.addWidget(self.eating)
        self.checkBoxLayout.addWidget(self.drinking)
        self.checkBoxLayout.addWidget(self.activitiy)
        self.checkBoxLayout.addWidget(self.travel)
        self.buttonLayout.addWidget(self.generateButton)
        self.mainLayout.addWidget(self.view)
        self.functions.addLayout(self.checkBoxLayout)
        self.functions.addLayout(self.buttonLayout)
        self.mainLayout.addLayout(self.functions)
        self.setLayout(self.mainLayout)

    # def initUI(self):
    #     ### this line here is what you'd be looking for
    #     self.setWindowState(Qt.WindowMaximized)
    #     ###
    #     self.show()

    def checkCheckBoxes(self):
        if self.eating.isChecked():
            self.dateNight.eatFlagT()
        else:
            self.dateNight.eatFlagF()
        if self.drinking.isChecked():
            self.dateNight.drinkFlagT()
        else:
            self.dateNight.drinkFlagF()
        if self.activitiy.isChecked():
            self.dateNight.actFlagT()
        else:
            self.dateNight.actFlagF()
        if self.travel.isChecked():
            self.dateNight.placeFlagT()
        else:
            self.dateNight.placeFlagF()
    
    def generateDate(self):
        self.dateInfo = self.dateNight.generate()
        # print(self.dateInfo[0:])
        self.updateWindow()
    
    def aggregateDate(self):
        data = self.dateInfo.copy()
        dateStr = '\n'.join(data)
        return dateStr
    
    def updateWindow(self):
        self.scene.removeItem(self.text)
        self.displayFont = QFont()
        self.displayFont.setPointSize(40)
        dateStr = self.aggregateDate()
        if len(dateStr) == 0:
            dateStr = 'Select at Least 1 Option'
        self.text = QGraphicsTextItem(dateStr)
        self.text.setFont(self.displayFont)
        # self.text.setPos(0,0)
        self.text.setDefaultTextColor('White')
        self.scene.addItem(self.text)