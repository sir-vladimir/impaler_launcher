# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_account.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_dialog_account(object):
    def setupUi(self, Dialog_account):
        if not Dialog_account.objectName():
            Dialog_account.setObjectName(u"Dialog_account")
        Dialog_account.resize(239, 200)
        self.gridLayoutWidget = QWidget(Dialog_account)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 241, 201))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_vayout = QVBoxLayout()
        self.vertical_vayout.setObjectName(u"vertical_vayout")
        self.text_user = QLineEdit(self.gridLayoutWidget)
        self.text_user.setObjectName(u"text_user")

        self.vertical_vayout.addWidget(self.text_user)

        self.text_password = QLineEdit(self.gridLayoutWidget)
        self.text_password.setObjectName(u"text_password")

        self.vertical_vayout.addWidget(self.text_password)

        self.label_info = QLabel(self.gridLayoutWidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setAlignment(Qt.AlignCenter)

        self.vertical_vayout.addWidget(self.label_info)

        self.check_offline = QCheckBox(self.gridLayoutWidget)
        self.check_offline.setObjectName(u"check_offline")

        self.vertical_vayout.addWidget(self.check_offline)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_vayout.addItem(self.spacer)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.button_accept = QPushButton(self.gridLayoutWidget)
        self.button_accept.setObjectName(u"button_accept")

        self.horizontal_layout.addWidget(self.button_accept)

        self.button_cancel = QPushButton(self.gridLayoutWidget)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontal_layout.addWidget(self.button_cancel)


        self.vertical_vayout.addLayout(self.horizontal_layout)


        self.grid_layout.addLayout(self.vertical_vayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog_account)

        QMetaObject.connectSlotsByName(Dialog_account)
    # setupUi

    def retranslateUi(self, Dialog_account):
        Dialog_account.setWindowTitle(QCoreApplication.translate("Dialog_account", u"Accounts", None))
        self.text_user.setPlaceholderText(QCoreApplication.translate("Dialog_account", u"Username", None))
        self.text_password.setPlaceholderText(QCoreApplication.translate("Dialog_account", u"Password", None))
        self.label_info.setText(QCoreApplication.translate("Dialog_account", u"Register at ely.by", None))
        self.check_offline.setText(QCoreApplication.translate("Dialog_account", u"Offline Mode", None))
        self.button_accept.setText(QCoreApplication.translate("Dialog_account", u"Accept", None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog_account", u"Cancel", None))
    # retranslateUi

