# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    #Main of window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 440)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        MainWindow.setCursor(QtCore.Qt.ArrowCursor)
        MainWindow.setMouseTracking(False)
        self.horizontalLayoutWidget = QtGui.QWidget(MainWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 700, 75))
        self.horizontalLayoutWidget.setMinimumSize(QtCore.QSize(40, 0))
        self.horizontalLayoutWidget.setMaximumSize(QtCore.QSize(700, 16777215))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Button for add a band
        self.btn_new = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_new.setMinimumSize(QtCore.QSize(115, 25))
        self.btn_new.setMaximumSize(QtCore.QSize(115, 25))
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)

        #Button for edit a band
        self.btn_edit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_edit.setMinimumSize(QtCore.QSize(110, 25))
        self.btn_edit.setMaximumSize(QtCore.QSize(110, 25))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)

        #Button for delete a band
        self.btn_delete = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setMinimumSize(QtCore.QSize(115, 25))
        self.btn_delete.setMaximumSize(QtCore.QSize(115, 25))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)

        #Button for add a style
        self.btn_newstyle = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_newstyle.setMinimumSize(QtCore.QSize(110, 25))
        self.btn_newstyle.setMaximumSize(QtCore.QSize(110, 25))
        self.btn_newstyle.setObjectName("btn_newstyle")
        self.horizontalLayout.addWidget(self.btn_newstyle)

        #Button for edit a style
        self.btn_editstyle = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_editstyle.setMinimumSize(QtCore.QSize(110, 25))
        self.btn_editstyle.setMaximumSize(QtCore.QSize(110, 25))
        self.btn_editstyle.setObjectName("btn_editstyle")
        self.horizontalLayout.addWidget(self.btn_editstyle)

        #Button for delete a style
        self.btn_delstyle = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btn_delstyle.setMinimumSize(QtCore.QSize(110, 25))
        self.btn_delstyle.setMaximumSize(QtCore.QSize(110, 25))
        self.btn_delstyle.setObjectName("btn_delstyle")
        self.horizontalLayout.addWidget(self.btn_delstyle)


        self.horizontalLayoutWidget_2 = QtGui.QWidget(MainWindow)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 70, 680, 40))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Search
        self.search_box = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.search_box.setMinimumSize(QtCore.QSize(300, 25))
        self.search_box.setMaximumSize(QtCore.QSize(300, 25))
        self.search_box.setText("")
        self.search_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.search_box.setObjectName("search_box")
        self.horizontalLayout_2.addWidget(self.search_box)

        #Search by style
        self.label = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label.setMinimumSize(QtCore.QSize(40, 25))
        self.label.setMaximumSize(QtCore.QSize(40, 25))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        #SelectStyle
        self.selectStyle = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.selectStyle.setMinimumSize(QtCore.QSize(180, 25))
        self.selectStyle.setMaximumSize(QtCore.QSize(180, 25))
        self.selectStyle.setMouseTracking(False)
        self.selectStyle.setEditable(False)
        self.selectStyle.setMaxVisibleItems(30)
        self.selectStyle.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.selectStyle.setObjectName("selectStyle")
        self.horizontalLayout_2.addWidget(self.selectStyle)

        #Table that containing the information on database
        self.table = QtGui.QTableView(MainWindow)
        self.table.setGeometry(QtCore.QRect(10, 110, 680, 310))
        self.table.setMinimumSize(QtCore.QSize(771, 350))
        self.table.setMaximumSize(QtCore.QSize(771, 350))
        self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("table")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #Name of the objects
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bandas Musicales", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new.setText(QtGui.QApplication.translate("MainWindow", "Nueva Banda", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_edit.setText(QtGui.QApplication.translate("MainWindow", "Editar Banda", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Banda", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_newstyle.setText(QtGui.QApplication.translate("MainWindow", "Nuevo Estilo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editstyle.setText(QtGui.QApplication.translate("MainWindow", "Editar Estilo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delstyle.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Estilo", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Buscar por Estilo:", None, QtGui.QApplication.UnicodeUTF8))



