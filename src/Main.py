#########################################################################################################
# Anyshift GUI
#
# There is no warranty for the program, to the extent permitted by applicable law. Except 
# when otherwise stated in writing the copyright holders and/or other parties provide the
# program "as is" without warranty of any kind, either expressed or implied, including, but
# not limited to, the implied warranties of merchantability and fitness for a particular purpose.  
# The entire risk as to the quality and performance of the program is with you.  
# Should the program prove defective, you assume the cost of all necessary servicing, 
# repair or correction.
#
# 2023 Menkaura Soft
#########################################################################################################

from PySide6.QtWidgets import (QMainWindow, QMessageBox, QFileDialog)
from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
import sys
from ReadWriteSaves import *
from Joystick import *
import Global
import webbrowser
from UI import Ui_MainWindow
from Presets import *
import os

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # Set up the user interface from Designer.
        self.setupUi(self)        
        # Make some local modifications. 
        anyIco = application_path + "/Resources/any_ico.ico"               
        self.setWindowIcon(QIcon(anyIco))
        self.runAnyButton.clicked.connect(self.runAny)
        self.actionSave_and_Exit.triggered.connect(lambda: self.menuButton('e'))
        self.actionGuides.triggered.connect(lambda: self.menuButton('g'))
        self.actionAbout_2.triggered.connect(lambda: self.menuButton('a'))
        self.actionLoad_Profile.triggered.connect(self.loadProfile)
        self.actionSave_Profile.triggered.connect(self.saveProfile)        
        self.configFistButton.clicked.connect(lambda: self.shifterConfigButton('first'))
        self.configSecondButton.clicked.connect(lambda: self.shifterConfigButton('second'))
        self.configThirdButton.clicked.connect(lambda: self.shifterConfigButton('third'))
        self.configFourthButton.clicked.connect(lambda: self.shifterConfigButton('fourth'))
        self.configFifthButton.clicked.connect(lambda: self.shifterConfigButton('fifth'))
        self.configSixthButton.clicked.connect(lambda: self.shifterConfigButton('sixth'))
        self.configSeventhButton.clicked.connect(lambda: self.shifterConfigButton('seventh'))
        self.configReverseButton.clicked.connect(lambda: self.shifterConfigButton('reverse'))
        self.clutchAxisButton.clicked.connect(lambda: self.shifterConfigButton('clutch_axis'))
        # Update window
        self.updateWindow()
    

    def shifterConfigButton(self, gear):
        global options
        # Read window options
        valid = self.readWindow()
        # Check for joystick connected
        if num_joy == 0:
            valid = False
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('No joystick found. Connect it before Anyshift')
            msg.setWindowTitle("Error")
            msg.exec()             
            return
         # If success configure axis
        if valid == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)            
            msg.setText("Joystick config")
            msg.setInformativeText(f'Select shifter position for {gear}')
            msg.setWindowTitle("Config")            
            msg.show() 
            if gear == 'clutch_axis':
                options = selectAxis(options)
            else:                
                options = selectGear(options, gear)            
            msg.done(1) 
        # Make some changes to display data
        options['up_key'] = charConvert(options['up_key'])
        options['down_key'] = charConvert(options['down_key'])
        options['rev_key']= charConvert(options['rev_key'])         
        # Update window        
        self.updateWindow()      


    def loadProfile(self):
        global options        
        path = application_path + "/Presets/"
        # Open select file window
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
        path,"Anyshift files (*.any)")
        # read options from the selected file
        options = iniReader(fname)
        # Update the window
        self.updateWindow()


    def saveProfile(self):
        global options        
        path = application_path + "/Presets/"
        fname = QFileDialog.getSaveFileName(self, 'Open file', 
        path,"Anyshift files (*.any)")
        # read options from window
        self.readWindow()
        # make some changes to the data to store it
        upshift = charConvert(options['up_key'])
        downshift = charConvert(options['down_key'])
        rev_key = charConvert(options['rev_key'])
        # Write ini file
        iniWriter(options, upshift, downshift, rev_key, fname[0])
        

    # Method for help menubar buttons
    def menuButton(self, page): 
        global options 
        # Open guides webpage           
        if page == 'g':
            webbrowser.open('https://github.com/Menkaura81/Anyshift/tree/main/Guides') 
            return
        # Open anyshift repository
        if page == 'a':            
            webbrowser.open('https://github.com/Menkaura81/Anyshift/')                         
            return       
        # Save options into ini file
        if page == 'e':            
            self.readWindow()
            upshift = charConvert(options['up_key'])
            downshift = charConvert(options['down_key'])
            rev_key = charConvert(options['rev_key'])
            file = 'Anyshift.ini'
            iniWriter(options, upshift, downshift, rev_key, file) 
            # sys.exit()           
            return   


    # Method for Run Anyshift button
    def runAny(self):   
        global options   
        global first_click     
        # Read the actual configuration displayed
        valid = self.readWindow()
        # Check for process running
        if first_click == True:
            if options['mem_mode'] == True:
                # Open DosBox process and check for process opened
                rwm = ReadWriteMemory()
                try:
                    process = rwm.get_process_by_name(options['process'])
                    process.open()        
                except:
                    valid = False
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('Process not found. Open it before Anyshift')
                    msg.setWindowTitle("Error")
                    msg.exec()             
                    return
            if num_joy == 0:
                valid = False
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('No joystick found. Connect it before Anyshift')
                msg.setWindowTitle("Error")
                msg.exec()             
                return
        if valid == True:# If it´s the first click of the button, launch anyshift and change the button text       
            if first_click == True:                      
                first_click = False
                Global.done = False
                self.runAnyButton.setText('Press to stop')            
                joystickLoop(options)
            # Else set Global.done True, end joystick loop and change button text
            else:
                Global.done = True
                first_click = True
                self.runAnyButton.setText('Run Anyshift')
       

    # Method for updating the window
    def updateWindow(self):
        global options
        # Joystick group
        self.shifterComboBox.addItems(joys)
        self.shifterComboBox.setCurrentIndex(int(options['joy_id']))
        self.ClutchComboBox.addItems(joys)
        self.ClutchComboBox.setCurrentIndex(int(options['clutch_id']))
        self.bitepointLineEdit.setText(str(options['bitepoint']))
        if options['clutch'] == True:
            self.clutchRadioButton.setChecked(True)
        else:
            self.clutchRadioButton.setChecked(False)
        # Gears and axis buttons
        self.firstGearLabel.setText(str(options['first']))
        self.secondGearLabel.setText(str(options['second']))
        self.thirdGearLabel.setText(str(options['third']))
        self.fourthGearLabel.setText(str(options['fourth']))
        self.FifthGearLabel.setText(str(options['fifth']))
        self.sixthGearLabel.setText(str(options['sixth']))
        self.seventhGearLabel.setText(str(options['seventh']))
        self.reverseGearLabel.setText(str(options['reverse']))
        self.clutchAxisLabel.setText(str(options['clutch_axis']))   
        # key values
        self.UpshiftLineEdit.setText(str(options['up_key']))
        self.downshiftLineEdit.setText(str(options['down_key']))
        self.neutralLineEdit.setText(str(options['neut_key'])) 
        self.reverseLineEdit.setText(str(options['rev_key']))    
        self.presskeydelayLineEdit.setText(str(options['presskey_timer']))
        self.reversekeydelayLineEdit.setText(str(options['releasekey_timer']))                  
        # Mem mode
        if options['mem_mode'] == True:
            self.memmodeRadioButton.setChecked(True)
        else:
            self.memmodeRadioButton.setChecked(False)
        self.processNameLineEdit.setText(str(options['process']))
        self.baseAddressLineEdit.setText(str(options['db_base_addr']))
        self.offsetLineEdit.setText(str(options['offset']))
        self.firstValueLineEdit.setText(str(options['first_value']))
        self.secondValueLineEdit.setText(str(options['second_value']))
        self.thirdValueLineEdit.setText(str(options['third_value']))
        self.fourthValueLineEdit.setText(str(options['fourth_value']))
        self.fifthValueLineEdit.setText(str(options['fifth_value']))
        self.sixthValueLineEdit.setText(str(options['sixth_value']))
        self.seventhValueLineEdit.setText(str(options['seventh_value']))
        self.neutralValueLineEdit.setText(str(options['neutral_value']))
        self.reverseValueLineEdit.setText(str(options['reverse_value']))
        # Options
        if options['seven_gears'] == True:
            self.sevenGearsCheckBox.setChecked(True)
        else:
            self.sevenGearsCheckBox.setChecked(False)
        if options['neutral'] == True:
            self.neutralCheckBox.setChecked(True)
        else:
            self.neutralCheckBox.setChecked(False)               
        if options['nascar_mode'] == True:
            self.nascarCheckBox.setChecked(True)
        else:
            self.nascarCheckBox.setChecked(False)
        if options['rev_button'] == True:
            self.reverseCheckBox.setChecked(True)
        else:
            self.reverseCheckBox.setChecked(False)
        self.neutralDelayLineEdit.setText(str(options['neutral_wait_time']))
        self.ArduinoLineEdit.setText(str(options['comport']))


    # Method for reading the window
    def readWindow(self):
        global options
        # Fist check the element that can throw error so function exits before changing options
        keys = []  # To keep track of already selected keys
        # Upshift key
        upshift = self.UpshiftLineEdit.text()[:1].lower()
        if ord(upshift) >= 97 and ord(upshift) <= 122:
            keys.append(upshift)
            options['up_key'] = hexConvert(upshift)
        else:            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Upshift key error. Only one char (a to z)')
            msg.setWindowTitle("Error")
            msg.exec_()            
            return False
        # Downshift key
        downshift = self.downshiftLineEdit.text()[:1].lower()
        if ord(downshift) >= 97 and ord(downshift) <= 122 and downshift not in keys:
            keys.append(downshift)
            options['down_key'] = hexConvert(downshift)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Downshift key error. Repeated or not a to z char')
            msg.setWindowTitle("Error")
            msg.exec_()             
            return False
        # Reverse key
        rev_key = self.reverseLineEdit.text()[:1].lower() 
        if ord(rev_key) >= 97 and ord(rev_key) <= 122 and rev_key not in keys:
            options['rev_key'] = hexConvert(rev_key)
            keys.append(rev_key)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Reverse key error. Repeated or not a to z char')
            msg.setWindowTitle("Error")
            msg.exec_()   
            return False
        # Neutral key
        neut_key = self.neutralLineEdit.text()[:1].lower()
        if ord(neut_key) >= 97 and ord(neut_key) <= 122 and neut_key not in keys:
            options['neut_key'] = neut_key
            keys.append(neut_key)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Neutral key error. Only one char (a to z)')
            msg.setWindowTitle("Error")
            msg.exec_()           
            return False
        # Neutral delay
        neutDelay = self.neutralDelayLineEdit.text()
        try:
            if float(neutDelay) > 0 and float(neutDelay) < 2:
                options['neutral_wait_time'] = float(neutDelay)  
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Neutral delay error. Must be a float between 0 and 2')
                msg.setWindowTitle("Error")
                msg.exec_()                 
                return False
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Neutral delay error. Must be a float between 0 and 2')
            msg.setWindowTitle("Error")
            msg.exec_()                 
            return False
        # Shifter and Clutch combobox
        options['joy_id'] = self.shifterComboBox.currentIndex()
        options['clutch_id'] = self.ClutchComboBox.currentIndex()
        if self.clutchRadioButton.isChecked():                       
            options['clutch'] = True
        else:
            options['clutch'] = False
        # Gear values
        options['first'] = int(self.firstGearLabel.text())
        options['second'] = int(self.secondGearLabel.text())
        options['third'] = int(self.thirdGearLabel.text())
        options['fourth'] = int(self.fourthGearLabel.text())
        options['fifth'] = int(self.FifthGearLabel.text())
        options['sixth'] = int(self.sixthGearLabel.text())
        options['seventh'] = int(self.seventhGearLabel.text())
        options['reverse'] = int(self.reverseGearLabel.text())
        options['clutch_axis'] = int(self.clutchAxisLabel.text())
        options['bitepoint'] = int(self.bitepointLineEdit.text())         
        # Key timers
        options['presskey_timer'] = self.presskeydelayLineEdit.text()
        options['releasekey_timer'] = self.reversekeydelayLineEdit.text()
        # Mem mode
        if self.memmodeRadioButton.isChecked():
            options['mem_mode'] = True
        else:    
            options['mem_mode'] = False
        options['process'] = self.processNameLineEdit.text()
        options['db_base_addr'] = self.baseAddressLineEdit.text()
        options['offset'] = self.offsetLineEdit.text()
        options['first_value'] = self.firstValueLineEdit.text()
        options['second_value'] = self.secondValueLineEdit.text()
        options['third_value'] = self.thirdValueLineEdit.text()
        options['fourth_value'] = self.fourthValueLineEdit.text()
        options['fifth_value'] = self.fifthValueLineEdit.text()
        options['sixth_value'] = self.sixthValueLineEdit.text()
        options['seventh_value'] = self.seventhValueLineEdit.text()
        options['reverse_value'] = self.reverseValueLineEdit.text()
        options['neutral_value'] = self.neutralValueLineEdit.text()
        # Options
        if self.neutralCheckBox.isChecked():             
            options['neutral'] = True
        else:
            options['neutral'] = False
        if self.sevenGearsCheckBox.isChecked():
            options['seven_gears'] = True
        else:
            options['seven_gears'] = False
        if self.nascarCheckBox.isChecked():
            options['nascar_mode'] = True
        else:
            options['nascar_mode'] = False
        if self.reverseCheckBox.isChecked():
            options['rev_button'] = True
        else:
            options['rev_button'] = False        
        # Extras
        options['neutral_wait_time'] = float(self.neutralDelayLineEdit.text())
        options['comport'] = self.ArduinoLineEdit.text() 
        # Result (no exceptions)
        return True 


    # Override closeEvent method
    def closeEvent(self, event):
        # Make sure Anyshift is not running
        Global.done = True
        self.runAnyButton.setText('Run Anyshift')
        # Ask for confirmation before closing
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you want to close the application?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            event.accept()  # Close the app
        else:
            event.ignore()  # Don't close the app   
        

if __name__ == '__main__': 
    global options
    global first_click    
    first_click = True
    # Get path for app location    
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)   
    # Read options
    options = iniReader('Anyshift.ini')
    # Get list of joystick ids and save them into joys list
    joys, num_joy = joystickLister()  # Get joystick list and count     
    # Launch GUI
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())    