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
"""

__author__ = 'Francisco A Camello N'
__date__ = '2021-07-20'
__copyright__ = '(C) 2021 by CamellOnCase'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

SMOOTH_TOLERANCE = 0.3
FIRST_SIMPLIFY_TOLERANCE = 2
SECOND_SIMPLIFY_TOLERANCE = 1
GEOGRAPHIC_CONSTANT = 111110
SIMPLIFICATION_METHOD = 0
MAX_NODE_ANGLE = 180
COUNTER = 1
FILTER_TOLERANCE = {10: 20, 20: 100, 40: 80, 100: 200}


def get_tolerance_by_interval(contour_interval, crs):
    if crs.isGeographic():
        tolerance = FILTER_TOLERANCE.get(contour_interval)
        if tolerance is not None:
            return tolerance / GEOGRAPHIC_CONSTANT

    return FILTER_TOLERANCE.get(contour_interval)

