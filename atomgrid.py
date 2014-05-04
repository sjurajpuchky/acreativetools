from PyQt4.QtCore import *
from PyQt4.QtGui import *
from numpy import *
import Avogadro

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

# always use 'Extension' for class name
class Extension(QObject):
  __pyqtSignals__ = ("message(const QString&)",)

    def __init__(self):
        QObject.__init__(self)

    def name(self):
        return "Atom Grid"

    def description(self):
        return "Make a grid of specified atom or molecule."

    def actions(self):
        actions = []
        return actions

    def performAction(self, action, glwidget):
        self.emit(SIGNAL("message(const QString&)"), "performing action...")
        self.molecule = glwidget.molecule

    def dockWidget(self):
        widget = QDockWidget("Build atom grid")
        self.setupWidget(widget)
        return widget

    def readSettings(self, settings):
        self.foo = settings.value("foo", QVariant(42))

    def writeSettings(self, settings):
        settings.setValue("foo", self.foo)

    def setupWidget(self, widget):
        self.formLayoutWidget = QWidget(widget)
        self.formLayoutWidget.setGeometry(QRect(10, 30, 141, 101))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)
        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayoutWidget = QWidget(widget)
        self.verticalLayoutWidget.setGeometry(QRect(160, 30, 121, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton = QPushButton(widget)
        self.pushButton.setGeometry(QRect(100, 200, 101, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
	self.pushButton.clicked.connect(self.generateHandle)
        self.label_4 = QLabel(widget)
        self.label_4.setGeometry(QRect(10, 130, 141, 26))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QLineEdit(widget)
        self.lineEdit_4.setGeometry(QRect(10, 150, 261, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.retranslateWidget(widget)
        QMetaObject.connectSlotsByName(widget)

  def retranslateWidget(self, widget):
        self.label.setText(_translate("AtomGridWidget", "X dim", None))
        self.lineEdit.setText(_translate("AtomGridWidget", "10", None))
        self.label_2.setText(_translate("AtomGridWidget", "Y dim", None))
        self.lineEdit_2.setText(_translate("AtomGridWidget", "10", None))
        self.label_3.setText(_translate("AtomGridWidget", "Z dim", None))
        self.lineEdit_3.setText(_translate("AtomGridWidget", "10", None))
        self.checkBox_3.setText(_translate("AtomGridWidget", "X fill", None))
        self.checkBox_2.setText(_translate("AtomGridWidget", "Y fill", None))
        self.checkBox.setText(_translate("AtomGridWidget", "Z fill", None))
        self.pushButton.setText(_translate("AtomGridWidget", "Generate Grid", None))
        self.label_4.setText(_translate("AtomGridWidget", "Selection name", None))
        self.lineEdit_4.setText(_translate("AtomGridWidget", "AtomGrid1", None))

  def generateHandle(self):
	print("Generating...")
	m = Avogadro.molecules.addMolecule()
	for x in range(0, 10):
	  for y in range(0, 10):
	    for z in range(0, 10):
		a = m.newAtom()
		a.atomicNumber = 6
		a.pos = numpy.array([x, y, z])
		m.addAtom(a)
		print(a.id)
	self.glwidget.molecule.copy(m)


# AtomGrid
# ========
# Author: Juraj Puchky - Devtech <sjurajpuchky@seznam.cz>
# Copyright (c) 2014
# Description: Make a grid of specified atom or molecule.
# License: GPLv3, free for use, donate any you would like.
# Donation: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2FXHJQCNREUHQ
# Version: 1.0
# Lastmod: 2014-05-02 23:30:12 

