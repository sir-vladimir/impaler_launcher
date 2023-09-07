# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_new.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_dialog_new(object):
    def setupUi(self, dialog_new):
        if not dialog_new.objectName():
            dialog_new.setObjectName(u"dialog_new")
        dialog_new.resize(242, 315)
        self.gridLayoutWidget = QWidget(dialog_new)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 241, 301))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.text_name = QLineEdit(self.gridLayoutWidget)
        self.text_name.setObjectName(u"text_name")

        self.vertical_layout.addWidget(self.text_name)

        self.box_version = QComboBox(self.gridLayoutWidget)
        self.box_version.setObjectName(u"box_version")

        self.vertical_layout.addWidget(self.box_version)

        self.check_fabric = QCheckBox(self.gridLayoutWidget)
        self.check_fabric.setObjectName(u"check_fabric")

        self.vertical_layout.addWidget(self.check_fabric)

        self.text_java = QLineEdit(self.gridLayoutWidget)
        self.text_java.setObjectName(u"text_java")

        self.vertical_layout.addWidget(self.text_java)

        self.text_jvm = QLineEdit(self.gridLayoutWidget)
        self.text_jvm.setObjectName(u"text_jvm")

        self.vertical_layout.addWidget(self.text_jvm)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vertical_layout.addItem(self.spacer)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setObjectName(u"horizontal_layout")
        self.button_accept = QPushButton(self.gridLayoutWidget)
        self.button_accept.setObjectName(u"button_accept")

        self.horizontal_layout.addWidget(self.button_accept)

        self.button_cancel = QPushButton(self.gridLayoutWidget)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontal_layout.addWidget(self.button_cancel)


        self.vertical_layout.addLayout(self.horizontal_layout)


        self.grid_layout.addLayout(self.vertical_layout, 0, 0, 1, 1)


        self.retranslateUi(dialog_new)

        QMetaObject.connectSlotsByName(dialog_new)
    # setupUi

    def retranslateUi(self, dialog_new):
        dialog_new.setWindowTitle(QCoreApplication.translate("dialog_new", u"Dialog", None))
        self.text_name.setText("")
        self.text_name.setPlaceholderText(QCoreApplication.translate("dialog_new", u"Name", None))
        self.box_version.setPlaceholderText(QCoreApplication.translate("dialog_new", u"Version", None))
        self.check_fabric.setText(QCoreApplication.translate("dialog_new", u"Use Fabric", None))
        self.text_java.setPlaceholderText(QCoreApplication.translate("dialog_new", u"Java Path", None))
        self.text_jvm.setPlaceholderText(QCoreApplication.translate("dialog_new", u"JVM Arguments", None))
        self.button_accept.setText(QCoreApplication.translate("dialog_new", u"Accept", None))
        self.button_cancel.setText(QCoreApplication.translate("dialog_new", u"Cancel", None))
    # retranslateUi

