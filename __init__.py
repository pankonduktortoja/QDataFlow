# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QDataFlow
                                 A QGIS plugin
 The plugin improves data flow in QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-12-28
        copyright            : (C) 2024 by Bartosz Łęczycki
        email                : bartosz.leczycki98@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QDataFlow class from file QDataFlow.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .QDataFlow import QDataFlow
    return QDataFlow(iface)
