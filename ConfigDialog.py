"""
***************************************************************************
Name			 	 : Geocoding
Description          : Geocoding and reverse Geocoding using Google
Date                 : 2/May/13
copyright            : (C) 2013 by ItOpen
email                : info@itopen.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os

# Import the PyQt and QGIS libraries
from qgis.core import Qgis
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt import uic
# create the dialog for Config
class ConfigDialog(QDialog ):

    def __init__(self, caller):
        super(ConfigDialog, self ).__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'Ui_Config.ui'), self)

        # stupid qvariant return a tuple...
        zoom_scale = caller.get_config('ZoomScale', 0)
        # Use pdb for debugging
        #import pdb
        ## These lines allow you to set a breakpoint in the app
        #pyqtRemoveInputHook()
        #pdb.set_trace()

        self.ZoomScale.setValue(int(zoom_scale))
        self.debugCheckBox.setChecked(caller.get_config('writeDebug', '') == True)


