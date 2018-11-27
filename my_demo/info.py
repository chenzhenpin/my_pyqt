# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QDialog



from Ui_info import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(str)
    def on_spinBox_valueChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        value=self.spinBox.value()
        _translate = QCoreApplication.translate
        print(value)
        if value==1:
            self.spinBox.setSpecialValueText(_translate("Dialog", "女"))
            print('nv')
        else:
            self.spinBox.setSpecialValueText(_translate("Dialog", "男"))
            print('nan')

            
   
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        lineEdit_2=self.lineEdit_2.text()
        lineEdit_4=self.lineEdit_4.text()
        lineEdit=self.lineEdit.text()
        spinBox=self.spinBox.value()
        print(lineEdit_2)
        print(lineEdit_4)
        print(lineEdit)
        print(spinBox)
        self.close()
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.close()
