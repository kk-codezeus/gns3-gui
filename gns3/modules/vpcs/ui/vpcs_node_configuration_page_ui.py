# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/modules/vpcs/ui/vpcs_node_configuration_page.ui'
#
# Created: Sun Jul 10 16:55:31 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VPCSNodeConfigPageWidget(object):
    def setupUi(self, VPCSNodeConfigPageWidget):
        VPCSNodeConfigPageWidget.setObjectName("VPCSNodeConfigPageWidget")
        VPCSNodeConfigPageWidget.resize(445, 209)
        self.gridLayout = QtWidgets.QGridLayout(VPCSNodeConfigPageWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(VPCSNodeConfigPageWidget)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(VPCSNodeConfigPageWidget)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 2, 1, 1)
        self.uiDefaultNameFormatLabel = QtWidgets.QLabel(VPCSNodeConfigPageWidget)
        self.uiDefaultNameFormatLabel.setObjectName("uiDefaultNameFormatLabel")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLabel, 1, 0, 1, 2)
        self.uiDefaultNameFormatLineEdit = QtWidgets.QLineEdit(VPCSNodeConfigPageWidget)
        self.uiDefaultNameFormatLineEdit.setObjectName("uiDefaultNameFormatLineEdit")
        self.gridLayout.addWidget(self.uiDefaultNameFormatLineEdit, 1, 2, 1, 1)
        self.uiScriptFileLabel = QtWidgets.QLabel(VPCSNodeConfigPageWidget)
        self.uiScriptFileLabel.setObjectName("uiScriptFileLabel")
        self.gridLayout.addWidget(self.uiScriptFileLabel, 2, 0, 1, 2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uiScriptFileEdit = QtWidgets.QLineEdit(VPCSNodeConfigPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiScriptFileEdit.sizePolicy().hasHeightForWidth())
        self.uiScriptFileEdit.setSizePolicy(sizePolicy)
        self.uiScriptFileEdit.setObjectName("uiScriptFileEdit")
        self.horizontalLayout_6.addWidget(self.uiScriptFileEdit)
        self.uiScriptFileToolButton = QtWidgets.QToolButton(VPCSNodeConfigPageWidget)
        self.uiScriptFileToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiScriptFileToolButton.setObjectName("uiScriptFileToolButton")
        self.horizontalLayout_6.addWidget(self.uiScriptFileToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(VPCSNodeConfigPageWidget)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 3, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(VPCSNodeConfigPageWidget)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(VPCSNodeConfigPageWidget)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 2, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(VPCSNodeConfigPageWidget)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 4, 0, 1, 2)
        self.uiCategoryComboBox = QtWidgets.QComboBox(VPCSNodeConfigPageWidget)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(263, 212, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 2)

        self.retranslateUi(VPCSNodeConfigPageWidget)
        QtCore.QMetaObject.connectSlotsByName(VPCSNodeConfigPageWidget)

    def retranslateUi(self, VPCSNodeConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        VPCSNodeConfigPageWidget.setWindowTitle(_translate("VPCSNodeConfigPageWidget", "VPCS device configuration"))
        self.uiNameLabel.setText(_translate("VPCSNodeConfigPageWidget", "Name:"))
        self.uiDefaultNameFormatLabel.setText(_translate("VPCSNodeConfigPageWidget", "Default name format:"))
        self.uiScriptFileLabel.setText(_translate("VPCSNodeConfigPageWidget", "Base script file:"))
        self.uiScriptFileToolButton.setText(_translate("VPCSNodeConfigPageWidget", "&Browse..."))
        self.uiSymbolLabel.setText(_translate("VPCSNodeConfigPageWidget", "Symbol:"))
        self.uiSymbolToolButton.setText(_translate("VPCSNodeConfigPageWidget", "&Browse..."))
        self.uiCategoryLabel.setText(_translate("VPCSNodeConfigPageWidget", "Category:"))

