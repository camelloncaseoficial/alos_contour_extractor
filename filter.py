contour_layer = QgsProject.instance().mapLayersByName('fabdem_contour')[0]
filtered_layer = QgsVectorLayer("LineString?crs=EPSG:4326", "Filtered contour", "memory")
provider = filtered_layer.dataProvider()
closed_contours = []  # To store closed contour features
features = []
# Loop through contour features
for feature in contour_layer.getFeatures():
#    print(feature)
    geometry = feature.geometry()
#    if geometry.isMultipart():
#        continue  # Skip multipart geometries

    if geometry.isMultipart():
        polyline = geometry.asMultiPolyline()[0]
        print('isMultipart')
    else:
        polyline = geometry.asPolyline()

    # Check if the first and last vertices are the same (closed line)
#    polyline = geometry.asPolyline()
#    print(polyline)
    first_point = polyline[0]
    last_point = polyline[-1]
    if first_point == last_point:
        closed_contours.append(feature)
        features.append(feature)
#print(features)
provider.addFeatures(features)

# Add the layer to the map canvas
QgsProject.instance().addMapLayer(filtered_layer)