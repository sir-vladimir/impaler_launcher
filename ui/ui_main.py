# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.10
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_info = QAction(MainWindow)
        self.action_info.setObjectName(u"action_info")
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_import = QAction(MainWindow)
        self.action_import.setObjectName(u"action_import")
        self.action_login = QAction(MainWindow)
        self.action_login.setObjectName(u"action_login")
        self.action_logout = QAction(MainWindow)
        self.action_logout.setObjectName(u"action_logout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.layout_instance = QVBoxLayout()
        self.layout_instance.setObjectName(u"layout_instance")
        self.list_instances = QListView(self.centralwidget)
        self.list_instances.setObjectName(u"list_instances")

        self.layout_instance.addWidget(self.list_instances)

        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.button_launch = QPushButton(self.centralwidget)
        self.button_launch.setObjectName(u"button_launch")

        self.layout_buttons.addWidget(self.button_launch)

        self.button_configure = QPushButton(self.centralwidget)
        self.button_configure.setObjectName(u"button_configure")

        self.layout_buttons.addWidget(self.button_configure)

        self.button_remove = QPushButton(self.centralwidget)
        self.button_remove.setObjectName(u"button_remove")

        self.layout_buttons.addWidget(self.button_remove)


        self.layout_instance.addLayout(self.layout_buttons)


        self.gridLayout_2.addLayout(self.layout_instance, 0, 0, 1, 1)

        self.text_browser_log = QTextBrowser(self.centralwidget)
        self.text_browser_log.setObjectName(u"text_browser_log")

        self.gridLayout_2.addWidget(self.text_browser_log, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 34))
        self.menu_instance = QMenu(self.menubar)
        self.menu_instance.setObjectName(u"menu_instance")
        self.menu_account = QMenu(self.menubar)
        self.menu_account.setObjectName(u"menu_account")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_instance.menuAction())
        self.menubar.addAction(self.menu_account.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_instance.addAction(self.action_new)
        self.menu_instance.addAction(self.action_import)
        self.menu_account.addAction(self.action_login)
        self.menu_account.addAction(self.action_logout)
        self.menu_help.addAction(self.action_info)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Impaler Launcher", None))
        self.action_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"New Instance", None))
        self.action_import.setText(QCoreApplication.translate("MainWindow", u"Import Instance", None))
        self.action_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.action_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.button_launch.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.button_configure.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.button_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.menu_instance.setTitle(QCoreApplication.translate("MainWindow", u"Instance", None))
        self.menu_account.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

