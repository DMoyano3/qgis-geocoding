"""
***************************************************************************
Name			 	 : Geocoding
Description          : Geocoding and reverse Geocoding using Google
Date                 : 28/May/09
copyright            : (C) 2009 by ItOpen
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

# create the dialog for GeoCoding
class PlaceSelectionDialog(QDialog):

  def __init__(self):
    super(PlaceSelectionDialog, self).__init__()
    uic.loadUi(os.path.join(os.path.dirname(__file__), 'Ui_PlaceSelection.ui'), self)
