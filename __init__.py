# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AlosContourExtractor
                                 A QGIS plugin
 Creates contour and elevation points from Alos Palsar DEM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-07-20
        copyright            : (C) 2021 by CamellOnCase
        email                : camelloncase@gmail.com
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

__author__ = 'CamellOnCase'
__date__ = '2021-07-20'
__copyright__ = '(C) 2021 by CamellOnCase'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AlosContourExtractor class from file AlosContourExtractor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .alos_contour_extractor import AlosContourExtractorPlugin
    return AlosContourExtractorPlugin()
