from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient, QIcon,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QGroupBox,
    QLabel, QLineEdit, QMenu, QMessageBox, QFileDialog,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 494)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())        
        
        self.actionLoad_Profile = QAction(MainWindow)
        self.actionLoad_Profile.setObjectName(u"actionLoad_Profile")
        self.actionSave_Profile = QAction(MainWindow)
        self.actionSave_Profile.setObjectName(u"actionSave_Profile")
        self.actionGuides = QAction(MainWindow)
        self.actionGuides.setObjectName(u"actionGuides")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.actionSave_and_Exit = QAction(MainWindow)
        self.actionSave_and_Exit.setObjectName(u"actionSave_and_Exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.runAnyButton = QPushButton(self.centralwidget)
        self.runAnyButton.setObjectName(u"runAnyButton")
        self.runAnyButton.setGeometry(QRect(380, 370, 91, 51))        
        
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 521, 80))
        self.shifterComboBox = QComboBox(self.groupBox)
        self.shifterComboBox.setObjectName(u"shifterComboBox")
        self.shifterComboBox.setGeometry(QRect(10, 50, 221, 22))
        self.shifterLabel = QLabel(self.groupBox)
        self.shifterLabel.setObjectName(u"shifterLabel")
        self.shifterLabel.setGeometry(QRect(10, 30, 49, 16))
        self.ClutchComboBox = QComboBox(self.groupBox)
        self.ClutchComboBox.setObjectName(u"ClutchComboBox")
        self.ClutchComboBox.setGeometry(QRect(290, 50, 221, 22))
        self.clutchRadioButton = QRadioButton(self.groupBox)
        self.clutchRadioButton.setObjectName(u"clutchRadioButton")
        self.clutchRadioButton.setGeometry(QRect(290, 30, 89, 20))        
        
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 90, 211, 121))
        self.percentLabel = QLabel(self.groupBox_2)
        self.percentLabel.setObjectName(u"percentLabel")
        self.percentLabel.setGeometry(QRect(190, 80, 16, 16))
        self.configFifthButton = QPushButton(self.groupBox_2)
        self.configFifthButton.setObjectName(u"configFifthButton")
        self.configFifthButton.setGeometry(QRect(50, 20, 21, 31))
        self.configThirdButton = QPushButton(self.groupBox_2)
        self.configThirdButton.setObjectName(u"configThirdButton")
        self.configThirdButton.setGeometry(QRect(30, 20, 21, 31))
        self.configSeventhButton = QPushButton(self.groupBox_2)
        self.configSeventhButton.setObjectName(u"configSeventhButton")
        self.configSeventhButton.setGeometry(QRect(70, 20, 21, 31))
        self.reverseGearLabel = QLabel(self.groupBox_2)
        self.reverseGearLabel.setObjectName(u"reverseGearLabel")
        self.reverseGearLabel.setGeometry(QRect(78, 100, 16, 21))
        font = QFont()
        font.setPointSize(10)
        self.reverseGearLabel.setFont(font)
        self.sixthGearLabel = QLabel(self.groupBox_2)
        self.sixthGearLabel.setObjectName(u"sixthGearLabel")
        self.sixthGearLabel.setGeometry(QRect(58, 100, 16, 21))
        self.sixthGearLabel.setFont(font)
        self.FifthGearLabel = QLabel(self.groupBox_2)
        self.FifthGearLabel.setObjectName(u"FifthGearLabel")
        self.FifthGearLabel.setGeometry(QRect(58, 50, 16, 21))
        self.FifthGearLabel.setFont(font)
        self.fourthGearLabel = QLabel(self.groupBox_2)
        self.fourthGearLabel.setObjectName(u"fourthGearLabel")
        self.fourthGearLabel.setGeometry(QRect(38, 100, 16, 21))
        self.fourthGearLabel.setFont(font)

        self.clutchAxisButton = QPushButton(self.groupBox_2)
        self.clutchAxisButton.setObjectName(u"clutchAxisButton")        
        self.clutchAxisButton.setGeometry(QRect(110, 20, 75, 24))
        
        self.configFistButton = QPushButton(self.groupBox_2)
        self.configFistButton.setObjectName(u"configFistButton")
        self.configFistButton.setGeometry(QRect(10, 20, 21, 31))
        self.bitepointLabel = QLabel(self.groupBox_2)
        self.bitepointLabel.setObjectName(u"bitepointLabel")
        self.bitepointLabel.setGeometry(QRect(110, 82, 49, 16))
        self.thirdGearLabel = QLabel(self.groupBox_2)
        self.thirdGearLabel.setObjectName(u"thirdGearLabel")
        self.thirdGearLabel.setGeometry(QRect(38, 50, 16, 21))
        self.thirdGearLabel.setFont(font)
        self.firstGearLabel = QLabel(self.groupBox_2)
        self.firstGearLabel.setObjectName(u"firstGearLabel")
        self.firstGearLabel.setGeometry(QRect(18, 50, 16, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firstGearLabel.sizePolicy().hasHeightForWidth())
        self.firstGearLabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setKerning(True)
        self.firstGearLabel.setFont(font1)
        self.configSixthButton = QPushButton(self.groupBox_2)
        self.configSixthButton.setObjectName(u"configSixthButton")
        self.configSixthButton.setGeometry(QRect(50, 70, 21, 31))
        self.seventhGearLabel = QLabel(self.groupBox_2)
        self.seventhGearLabel.setObjectName(u"seventhGearLabel")
        self.seventhGearLabel.setGeometry(QRect(78, 50, 16, 21))
        self.seventhGearLabel.setFont(font)
        self.clutchAxisLabel = QLabel(self.groupBox_2)
        self.clutchAxisLabel.setObjectName(u"clutchAxisLabel")
        self.clutchAxisLabel.setGeometry(QRect(145, 40, 16, 21))
        self.secondGearLabel = QLabel(self.groupBox_2)
        self.secondGearLabel.setObjectName(u"secondGearLabel")
        self.secondGearLabel.setGeometry(QRect(18, 100, 16, 21))
        self.secondGearLabel.setFont(font)
        self.bitepointLineEdit = QLineEdit(self.groupBox_2)
        self.bitepointLineEdit.setObjectName(u"bitepointLineEdit")
        self.bitepointLineEdit.setGeometry(QRect(160, 80, 31, 22))
        self.configFourthButton = QPushButton(self.groupBox_2)
        self.configFourthButton.setObjectName(u"configFourthButton")
        self.configFourthButton.setGeometry(QRect(30, 70, 21, 31))
        self.configReverseButton = QPushButton(self.groupBox_2)
        self.configReverseButton.setObjectName(u"configReverseButton")
        self.configReverseButton.setGeometry(QRect(70, 70, 21, 31))
        self.configSecondButton = QPushButton(self.groupBox_2)
        self.configSecondButton.setObjectName(u"configSecondButton")
        self.configSecondButton.setGeometry(QRect(10, 70, 21, 31))        
        
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(230, 90, 301, 121))
        self.reversekeydelayLineEdit = QLineEdit(self.groupBox_3)
        self.reversekeydelayLineEdit.setObjectName(u"reversekeydelayLineEdit")
        self.reversekeydelayLineEdit.setGeometry(QRect(250, 90, 41, 22))
        self.UpshiftLineEdit = QLineEdit(self.groupBox_3)
        self.UpshiftLineEdit.setObjectName(u"UpshiftLineEdit")
        self.UpshiftLineEdit.setGeometry(QRect(100, 30, 31, 22))
        self.upshiftLabel = QLabel(self.groupBox_3)
        self.upshiftLabel.setObjectName(u"upshiftLabel")
        self.upshiftLabel.setGeometry(QRect(30, 30, 49, 16))
        self.reverseLineEdit = QLineEdit(self.groupBox_3)
        self.reverseLineEdit.setObjectName(u"reverseLineEdit")
        self.reverseLineEdit.setGeometry(QRect(250, 60, 31, 22))
        self.downshiftLabel = QLabel(self.groupBox_3)
        self.downshiftLabel.setObjectName(u"downshiftLabel")
        self.downshiftLabel.setGeometry(QRect(20, 60, 61, 16))
        self.presskeydelayLabel = QLabel(self.groupBox_3)
        self.presskeydelayLabel.setObjectName(u"presskeydelayLabel")
        self.presskeydelayLabel.setGeometry(QRect(10, 90, 81, 16))
        self.reverseLabel = QLabel(self.groupBox_3)
        self.reverseLabel.setObjectName(u"reverseLabel")
        self.reverseLabel.setGeometry(QRect(170, 60, 49, 16))
        self.downshiftLineEdit = QLineEdit(self.groupBox_3)
        self.downshiftLineEdit.setObjectName(u"downshiftLineEdit")
        self.downshiftLineEdit.setGeometry(QRect(100, 60, 31, 22))
        self.releasekeydelayLabel = QLabel(self.groupBox_3)
        self.releasekeydelayLabel.setObjectName(u"releasekeydelayLabel")
        self.releasekeydelayLabel.setGeometry(QRect(150, 90, 101, 16))
        self.neutralLineEdit = QLineEdit(self.groupBox_3)
        self.neutralLineEdit.setObjectName(u"neutralLineEdit")
        self.neutralLineEdit.setGeometry(QRect(250, 30, 31, 22))
        self.presskeydelayLineEdit = QLineEdit(self.groupBox_3)
        self.presskeydelayLineEdit.setObjectName(u"presskeydelayLineEdit")
        self.presskeydelayLineEdit.setGeometry(QRect(100, 90, 41, 22))
        self.neutralLabel = QLabel(self.groupBox_3)
        self.neutralLabel.setObjectName(u"neutralLabel")
        self.neutralLabel.setGeometry(QRect(170, 30, 49, 16))
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(50, 220, 441, 131))
        self.reverseValueLineEdit = QLineEdit(self.groupBox_4)
        self.reverseValueLineEdit.setObjectName(u"reverseValueLineEdit")
        self.reverseValueLineEdit.setGeometry(QRect(400, 100, 31, 22))
        self.gearValuesLabel = QLabel(self.groupBox_4)
        self.gearValuesLabel.setObjectName(u"gearValuesLabel")
        self.gearValuesLabel.setGeometry(QRect(270, 20, 111, 16))
        self.baseAddressLabel = QLabel(self.groupBox_4)
        self.baseAddressLabel.setObjectName(u"baseAddressLabel")
        self.baseAddressLabel.setGeometry(QRect(10, 70, 81, 16))
        self.memmodeRadioButton = QRadioButton(self.groupBox_4)
        self.memmodeRadioButton.setObjectName(u"memmodeRadioButton")
        self.memmodeRadioButton.setGeometry(QRect(10, 20, 61, 20))
        self.neutralValueLabel = QLabel(self.groupBox_4)
        self.neutralValueLabel.setObjectName(u"neutralValueLabel")
        self.neutralValueLabel.setGeometry(QRect(320, 70, 16, 16))
        self.fourthValueLineEdit = QLineEdit(self.groupBox_4)
        self.fourthValueLineEdit.setObjectName(u"fourthValueLineEdit")
        self.fourthValueLineEdit.setGeometry(QRect(300, 100, 31, 22))
        self.thirdValueLineEdit = QLineEdit(self.groupBox_4)
        self.thirdValueLineEdit.setObjectName(u"thirdValueLineEdit")
        self.thirdValueLineEdit.setGeometry(QRect(400, 40, 31, 22))
        self.offsetLineEdit = QLineEdit(self.groupBox_4)
        self.offsetLineEdit.setObjectName(u"offsetLineEdit")
        self.offsetLineEdit.setGeometry(QRect(90, 100, 91, 22))
        self.processNameLabel = QLabel(self.groupBox_4)
        self.processNameLabel.setObjectName(u"processNameLabel")
        self.processNameLabel.setGeometry(QRect(10, 40, 81, 16))
        self.seventhValueLineEdit = QLineEdit(self.groupBox_4)
        self.seventhValueLineEdit.setObjectName(u"seventhValueLineEdit")
        self.seventhValueLineEdit.setGeometry(QRect(350, 40, 31, 22))
        self.offsetLabel = QLabel(self.groupBox_4)
        self.offsetLabel.setObjectName(u"offsetLabel")
        self.offsetLabel.setGeometry(QRect(30, 100, 41, 16))
        self.sixthValueLabel = QLabel(self.groupBox_4)
        self.sixthValueLabel.setObjectName(u"sixthValueLabel")
        self.sixthValueLabel.setGeometry(QRect(340, 100, 16, 16))
        self.secondValueLineEdit = QLineEdit(self.groupBox_4)
        self.secondValueLineEdit.setObjectName(u"secondValueLineEdit")
        self.secondValueLineEdit.setGeometry(QRect(250, 100, 31, 22))
        self.reverseValueLabel = QLabel(self.groupBox_4)
        self.reverseValueLabel.setObjectName(u"reverseValueLabel")
        self.reverseValueLabel.setGeometry(QRect(390, 100, 16, 16))
        self.processNameLineEdit = QLineEdit(self.groupBox_4)
        self.processNameLineEdit.setObjectName(u"processNameLineEdit")
        self.processNameLineEdit.setGeometry(QRect(90, 40, 91, 22))
        self.firstValueLineEdit = QLineEdit(self.groupBox_4)
        self.firstValueLineEdit.setObjectName(u"firstValueLineEdit")
        self.firstValueLineEdit.setGeometry(QRect(250, 40, 31, 22))
        self.secondValueLabel = QLabel(self.groupBox_4)
        self.secondValueLabel.setObjectName(u"secondValueLabel")
        self.secondValueLabel.setGeometry(QRect(240, 100, 16, 16))
        self.fifthValueLineEdit = QLineEdit(self.groupBox_4)
        self.fifthValueLineEdit.setObjectName(u"fifthValueLineEdit")
        self.fifthValueLineEdit.setGeometry(QRect(300, 40, 31, 22))
        self.neutralValueLineEdit = QLineEdit(self.groupBox_4)
        self.neutralValueLineEdit.setObjectName(u"neutralValueLineEdit")
        self.neutralValueLineEdit.setGeometry(QRect(330, 70, 31, 22))
        self.sixthValueLineEdit = QLineEdit(self.groupBox_4)
        self.sixthValueLineEdit.setObjectName(u"sixthValueLineEdit")
        self.sixthValueLineEdit.setGeometry(QRect(350, 100, 31, 22))
        self.fourthValueLabel = QLabel(self.groupBox_4)
        self.fourthValueLabel.setObjectName(u"fourthValueLabel")
        self.fourthValueLabel.setGeometry(QRect(290, 100, 16, 16))
        self.thirdValueLabel = QLabel(self.groupBox_4)
        self.thirdValueLabel.setObjectName(u"thirdValueLabel")
        self.thirdValueLabel.setGeometry(QRect(290, 40, 16, 16))
        self.fifthValueLabel = QLabel(self.groupBox_4)
        self.fifthValueLabel.setObjectName(u"fifthValueLabel")
        self.fifthValueLabel.setGeometry(QRect(340, 40, 16, 16))
        self.firstValueLabel = QLabel(self.groupBox_4)
        self.firstValueLabel.setObjectName(u"firstValueLabel")
        self.firstValueLabel.setGeometry(QRect(240, 40, 16, 16))
        self.baseAddressLineEdit = QLineEdit(self.groupBox_4)
        self.baseAddressLineEdit.setObjectName(u"baseAddressLineEdit")
        self.baseAddressLineEdit.setGeometry(QRect(90, 70, 91, 22))
        self.sevenValueLabel = QLabel(self.groupBox_4)
        self.sevenValueLabel.setObjectName(u"sevenValueLabel")
        self.sevenValueLabel.setGeometry(QRect(390, 40, 16, 16))
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 350, 321, 91))
        self.reverseCheckBox = QCheckBox(self.groupBox_5)
        self.reverseCheckBox.setObjectName(u"reverseCheckBox")
        self.reverseCheckBox.setGeometry(QRect(150, 20, 121, 20))
        self.ArduinoLineEdit = QLineEdit(self.groupBox_5)
        self.ArduinoLineEdit.setObjectName(u"ArduinoLineEdit")
        self.ArduinoLineEdit.setGeometry(QRect(250, 60, 61, 22))
        self.neutralCheckBox = QCheckBox(self.groupBox_5)
        self.neutralCheckBox.setObjectName(u"neutralCheckBox")
        self.neutralCheckBox.setGeometry(QRect(10, 40, 101, 20))
        self.sevenGearsCheckBox = QCheckBox(self.groupBox_5)
        self.sevenGearsCheckBox.setObjectName(u"sevenGearsCheckBox")
        self.sevenGearsCheckBox.setGeometry(QRect(10, 20, 111, 20))
        self.nascarCheckBox = QCheckBox(self.groupBox_5)
        self.nascarCheckBox.setObjectName(u"nascarCheckBox")
        self.nascarCheckBox.setGeometry(QRect(170, 40, 91, 20))
        self.arduinoLabel = QLabel(self.groupBox_5)
        self.arduinoLabel.setObjectName(u"arduinoLabel")
        self.arduinoLabel.setGeometry(QRect(140, 60, 101, 16))
        self.neutralDelayLineEdit = QLineEdit(self.groupBox_5)
        self.neutralDelayLineEdit.setObjectName(u"neutralDelayLineEdit")
        self.neutralDelayLineEdit.setGeometry(QRect(90, 60, 41, 22))
        self.neutralDelayLabel = QLabel(self.groupBox_5)
        self.neutralDelayLabel.setObjectName(u"neutralDelayLabel")
        self.neutralDelayLabel.setGeometry(QRect(10, 60, 71, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)        
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.actionLoad_Profile)
        self.menuMenu.addAction(self.actionSave_Profile)
        
        # Save and exit menu
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionSave_and_Exit)
        
        
        # Guides menu
        self.menuHelp.addAction(self.actionGuides)
        
        
        # About menu
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_2)
        

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        # update created window with config values
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Anyshift", None))
        self.actionLoad_Profile.setText(QCoreApplication.translate("MainWindow", u"Load Profile", None))
        self.actionSave_Profile.setText(QCoreApplication.translate("MainWindow", u"Save Profile", None))
        self.actionGuides.setText(QCoreApplication.translate("MainWindow", u"Guides", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionSave_and_Exit.setText(QCoreApplication.translate("MainWindow", u"Remember Options", None))
        self.runAnyButton.setText(QCoreApplication.translate("MainWindow", u"Run AnyShift", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Joystick Selection", None))
        self.shifterLabel.setText(QCoreApplication.translate("MainWindow", u"Shifter", None))
        self.clutchRadioButton.setText(QCoreApplication.translate("MainWindow", u"Clutch", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Joystick Buttons", None))
        self.percentLabel.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.configFifthButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.configThirdButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.configSeventhButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.reverseGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.sixthGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.FifthGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.fourthGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.clutchAxisButton.setText(QCoreApplication.translate("MainWindow", u"Clutch Axis", None))
        self.configFistButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.bitepointLabel.setText(QCoreApplication.translate("MainWindow", u"Bitepoint", None))
        self.thirdGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.firstGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.configSixthButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.seventhGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.clutchAxisLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.secondGearLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.configFourthButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.configReverseButton.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.configSecondButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Key Selection", None))
        self.upshiftLabel.setText(QCoreApplication.translate("MainWindow", u"Upshift", None))
        self.downshiftLabel.setText(QCoreApplication.translate("MainWindow", u"Downshift", None))
        self.presskeydelayLabel.setText(QCoreApplication.translate("MainWindow", u"Press Key Delay", None))
        self.reverseLabel.setText(QCoreApplication.translate("MainWindow", u"Reverse", None))
        self.releasekeydelayLabel.setText(QCoreApplication.translate("MainWindow", u"Release Key Delay", None))
        self.neutralLabel.setText(QCoreApplication.translate("MainWindow", u"Neutral", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Memory Mode", None))
        self.gearValuesLabel.setText(QCoreApplication.translate("MainWindow", u"Gear Values Ingame", None))
        self.baseAddressLabel.setText(QCoreApplication.translate("MainWindow", u"Base Address", None))
        self.memmodeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.neutralValueLabel.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.processNameLabel.setText(QCoreApplication.translate("MainWindow", u"Process Name", None))
        self.offsetLabel.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.sixthValueLabel.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.reverseValueLabel.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.secondValueLabel.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.fourthValueLabel.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.thirdValueLabel.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.fifthValueLabel.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.firstValueLabel.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.sevenValueLabel.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.reverseCheckBox.setText(QCoreApplication.translate("MainWindow", u"Reverse is a Button", None))
        self.neutralCheckBox.setText(QCoreApplication.translate("MainWindow", u"Detect Neutral", None))
        self.sevenGearsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Use Seventh Gear", None))
        self.nascarCheckBox.setText(QCoreApplication.translate("MainWindow", u"Nascar Mode", None))
        self.arduinoLabel.setText(QCoreApplication.translate("MainWindow", u"Arduino COM port", None))
        self.neutralDelayLabel.setText(QCoreApplication.translate("MainWindow", u"Neutral Delay", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi  