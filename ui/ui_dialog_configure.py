# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_configure_instance.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_dialog_configure(object):
    def setupUi(self, dialog_configure):
        if not dialog_configure.objectName():
            dialog_configure.setObjectName(u"dialog_configure")
        dialog_configure.resize(240, 320)
        self.gridLayoutWidget = QWidget(dialog_configure)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 241, 321))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.text_name = QLineEdit(self.gridLayoutWidget)
        self.text_name.setObjectName(u"text_name")

        self.vertical_layout.addWidget(self.text_name)

        self.label_version = QLabel(self.gridLayoutWidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setAlignment(Qt.AlignCenter)

        self.vertical_layout.addWidget(self.label_version)

        self.text_jvm = QLineEdit(self.gridLayoutWidget)
        self.text_jvm.setObjectName(u"text_jvm")

        self.vertical_layout.addWidget(self.text_jvm)

        self.text_java = QLineEdit(self.gridLayoutWidget)
        self.text_java.setObjectName(u"text_java")

        self.vertical_layout.addWidget(self.text_java)

        self.button_open_folder = QPushButton(self.gridLayoutWidget)
        self.button_open_folder.setObjectName(u"button_open_folder")

        self.vertical_layout.addWidget(self.button_open_folder)

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


        self.retranslateUi(dialog_configure)

        QMetaObject.connectSlotsByName(dialog_configure)
    # setupUi

    def retranslateUi(self, dialog_configure):
        dialog_configure.setWindowTitle(QCoreApplication.translate("dialog_configure", u"Configure Instance", None))
        self.text_name.setPlaceholderText(QCoreApplication.translate("dialog_configure", u"Name", None))
        self.label_version.setText(QCoreApplication.translate("dialog_configure", u"Version", None))
        self.text_jvm.setPlaceholderText(QCoreApplication.translate("dialog_configure", u"JVM Arguments", None))
        self.text_java.setPlaceholderText(QCoreApplication.translate("dialog_configure", u"Java Path", None))
        self.button_open_folder.setText(QCoreApplication.translate("dialog_configure", u"Open Folder", None))
        self.button_accept.setText(QCoreApplication.translate("dialog_configure", u"Accept", None))
        self.button_cancel.setText(QCoreApplication.translate("dialog_configure", u"Cancel", None))
    # retranslateUi

