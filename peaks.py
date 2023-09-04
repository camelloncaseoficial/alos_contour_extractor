from qgis.core import QgsRasterLayer
import numpy as np
from scipy.signal import find_peaks

raster_layer = QgsProject.instance().mapLayersByName('FABDEM_2296-4-SE')[0]
fields_map = QgsFields()
fields_map.append(QgsField('cota', QVariant.Double))
point_layer = QgsVectorLayer("Point?crs=EPSG:4326", "Spot Points", "memory")
provider = point_layer.dataProvider()
provider.addAttributes(fields_map)
point_layer.updateFields()

raster_values = {}
threshold = 0.0
# Convert raster layer to NumPy array
extent = raster_layer.extent()
rows, cols = raster_layer.height(), raster_layer.width()
cell_size = raster_layer.rasterUnitsPerPixelX()
block = raster_layer.dataProvider().block(1, extent, rows, cols)
raster_array = np.array([block.value(row, col) for row in range(rows) for col in range(cols)]).reshape(rows, cols)

# Flatten the raster array
flat_raster = raster_array.flatten()

# Find peaks in the raster array
peak_indices, _ = find_peaks(flat_raster, height=threshold)

# Convert indices to row and column coordinates
peak_points = []
features = []
for idx in peak_indices:
    row = idx // cols
    col = idx % cols
    x = extent.xMinimum() + col * cell_size
    y = extent.yMaximum() - row * cell_size
    peak_points.append((x, y))
    raster_value = raster_layer.dataProvider().sample(QgsPointXY(x, y), 1)[0]
    raster_values[(row, col)] = raster_value
    feat = QgsFeature()
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
    feat.setAttributes([raster_value])
    features.append(feat)

provider.addFeatures(features)

# Add the layer to the map canvas
QgsProject.instance().addMapLayer(point_layer)
print( peak_points)