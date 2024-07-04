import sys
from PySide6 import QtWidgets
from UiMainWindow import Ui_MainWindow
from ReadWriteSaves import ini_reader
from ShifterConfig import joystick_lister
from Gearbox import joystick_loop

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
       QtWidgets.QMainWindow.__init__(self) 
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)


if __name__ == '__main__':    
    
    # Read config from ini file
    options = ini_reader()
    # Get list of joystick ids and save them into joys list
    joys, num_joy = joystick_lister()  # Get joystick list and count

    
    def updateWindow():
        
        ui.shifterComboBox.addItems(joys)
        ui.shifterComboBox.setCurrentIndex(int(options['joy_id']))
        ui.ClutchComboBox.addItems(joys)
        ui.ClutchComboBox.setCurrentIndex(int(options['clutch_id']))
        ui.bitepointLineEdit.setText(str(options['bitepoint']))
        if options['clutch'] == 'True':
            ui.clutchRadioButton.setChecked(True)
        
        ui.firstGearLabel.setText(str(options['first']))
        ui.secondGearLabel.setText(str(options['second']))
        ui.thirdGearLabel.setText(str(options['third']))
        ui.fourthGearLabel.setText(str(options['fourth']))
        ui.FifthGearLabel.setText(str(options['fifth']))
        ui.sixthGearLabel.setText(str(options['sixth']))
        ui.seventhGearLabel.setText(str(options['seventh']))
        ui.reverseGearLabel.setText(str(options['reverse']))
        ui.clutchAxisLabel.setText(str(options['clutch_axis']))   

        ui.UpshiftLineEdit.setText(str(options['up_key']))
        ui.downshiftLineEdit.setText(str(options['down_key']))
        ui.neutralLineEdit.setText(str(options['neut_key'])) 
        ui.reverseLineEdit.setText(str(options['rev_key']))    
        ui.presskeydelayLineEdit.setText(str(options['presskey_timer']))
        ui.reversekeydelayLineEdit.setText(str(options['releasekey_timer']))                  
        
        if options['mem_mode'] == 'True':
            ui.memmodeRadioButton.setChecked(True)
        ui.processNameLineEdit.setText(str(options['process']))
        ui.baseAddressLineEdit.setText(str(options['db_base_addr']))
        ui.offsetLineEdit.setText(str(options['offset']))
        ui.firstValueLineEdit.setText(str(options['first_value']))
        ui.secondValueLineEdit.setText(str(options['second_value']))
        ui.thirdValueLineEdit.setText(str(options['third_value']))
        ui.fourthValueLineEdit.setText(str(options['fourth_value']))
        ui.fifthValueLineEdit.setText(str(options['fifth_value']))
        ui.sixthValueLineEdit.setText(str(options['sixth_value']))
        ui.seventhValueLineEdit.setText(str(options['seventh_value']))
        ui.neutralValueLineEdit.setText(str(options['neutral_value']))
        ui.reverseValueLineEdit.setText(str(options['reverse_value']))

        if options['seven_gears'] == 'True':
            ui.sevenGearsCheckBox.setChecked(True)
        if options['neutral'] == 'True':
            ui.neutralCheckBox.setChecked(True)        
        if options['nascar_mode'] == 'True':
            ui.nascarCheckBox.setChecked(True)
        if options['rev_button'] == 'True':
            ui.reverseCheckBox.setChecked(True)
        ui.neutralDelayLineEdit.setText(str(options['neutral_wait_time']))
        ui.ArduinoLineEdit.setText(str(options['comport']))


    def readWindow():
        #aqui tengo que meter el codigo para leer la pantalla y guardala en options
        options['joy_id'] = ui.shifterComboBox.currentIndex()
        options['clutch_id'] = ui.ClutchComboBox.currentIndex()
        if ui.clutchRadioButton.isChecked():
            options['clutch'] == True
        else:
            options['clutch'] == False

        options['first'] == ui.firstGearLabel.text()
        options['second'] == ui.secondGearLabel.text()
        options['third'] == ui.thirdGearLabel.text()
        options['fourth'] == ui.fourthGearLabel.text()
        options['fifth'] == ui.FifthGearLabel.text()
        options['sixth'] == ui.sixthGearLabel.text()
        options['seventh'] == ui.seventhGearLabel.text()
        options['reverse'] == ui.reverseGearLabel.text()
        options['clutch_axis'] == ui.clutchAxisLabel.text()
        options['bitepoint'] == ui.bitepointLineEdit.text()

        options['up_key'] == ui.UpshiftLineEdit.text()
        options['down_key'] == ui.downshiftLineEdit.text()
        options['neut_key'] == ui.neutralLineEdit.text()
        options['rev_key'] == ui.reverseLineEdit.text()
        options['presskey_timer'] == ui.presskeydelayLineEdit.text()
        options['releasekey_timer'] == ui.reversekeydelayLineEdit.text()

        if ui.memmodeRadioButton.isChecked():
            options['mem_mode'] == True
        else:    
            options['mem_mode'] == False
        options['process'] == ui.processNameLineEdit.text()
        options['db_base_addr'] == ui.baseAddressLineEdit.text()
        options['offset'] == ui.offsetLineEdit.text()
        options['first_value'] == ui.firstValueLineEdit.text()
        options['second_value'] == ui.secondValueLineEdit.text()
        options['third_value'] == ui.thirdValueLineEdit.text()
        options['fourth_value'] == ui.fourthValueLineEdit.text()
        options['fifth_value'] == ui.fifthValueLineEdit.text()
        options['sixth_value'] == ui.sixthValueLineEdit.text()
        options['seventh_value'] == ui.seventhValueLineEdit.text()
        options['reverse_value'] == ui.reverseValueLineEdit.text()
        options['neutral_value'] == ui.neutralValueLineEdit.text()

        if ui.neutralCheckBox.isChecked():
            options['neutral'] == True
        else:
            options['neutral'] == False
        if ui.sevenGearsCheckBox.isChecked():
            options['seven_gears'] == True
        else:
            options['seven_gears'] == False
        if ui.nascarCheckBox.isChecked():
            options['nascar_mode'] == True
        else:
            options['nascar_mode'] == False
        if ui.reverseCheckBox.isChecked():
            options['rev_button'] == True
        else:
            options['rev_button'] == False
        options['neutral_wait_time'] == ui.neutralDelayLineEdit.text()
        options['comport'] == ui.ArduinoLineEdit.text()       
        

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()    
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    updateWindow()  
    readWindow()  
    sys.exit(app.exec())