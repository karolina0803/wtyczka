# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaQGIS
                                 A QGIS plugin
 Obliczenie różnicy wysokości pomiędzy punktami lub obliczenie pola powierzchni metodą Gaussa.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-06
        copyright            : (C) 2024 by Weronika Zienkiewicz, Karolina Żuber
        email                : weronika.zienkiewicz.stud@pw.edu.pl, karolina.zuber.stud@pw.edu.pl
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
    """Load WtyczkaQGIS class from file WtyczkaQGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qgis_wtyczka import WtyczkaQGIS
    return WtyczkaQGIS(iface)