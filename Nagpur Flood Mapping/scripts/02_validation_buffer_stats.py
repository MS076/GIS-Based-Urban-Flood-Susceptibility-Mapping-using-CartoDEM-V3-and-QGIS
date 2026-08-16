"""
Flood Risk Mapping - Nag River Basin, Nagpur
Script 2: Validation Point Buffer Statistics

Run this inside the QGIS Python Console (or Processing > Python Console script editor).
Requires the 'flood_2023_locations' point layer and 'flood_risk_classified' raster
layer to be loaded in the current project.

What it does:
For each 2023 flood validation point, this script:
  1. Reprojects the points to match the risk raster's CRS (UTM, metres)
  2. Creates a 100m buffer around each point
  3. Runs a zonal histogram to find the risk-class composition inside each buffer
  4. Samples the exact risk class at each point's coordinates
  5. Prints a summary comparing exact-pixel classification vs. neighbourhood
     (100m buffer) classification for each validation point
"""

import processing


def find_layer(keyword):
    """Find a loaded layer by case-insensitive partial name match."""
    for lyr in QgsProject.instance().mapLayers().values():
        if keyword.lower() in lyr.name().lower():
            return lyr
    return None


points_layer = find_layer('flood_2023') or find_layer('flood 2023')
risk_layer = find_layer('flood_risk_classified') or find_layer('flood risk classified')

if points_layer is None or risk_layer is None:
    print("Could not find one or both layers. Available layers:")
    for lyr in QgsProject.instance().mapLayers().values():
        print(" -", lyr.name())
else:
    print(f"Using points layer: {points_layer.name()}")
    print(f"Using risk layer: {risk_layer.name()}\n")

    # Step 1: Reproject points to match the risk layer's CRS BEFORE buffering,
    # so the 100m buffer distance is meaningful (avoids a degrees-vs-metres mismatch)
    reproject_result = processing.run("native:reprojectlayer", {
        'INPUT': points_layer,
        'TARGET_CRS': risk_layer.crs(),
        'OUTPUT': 'memory:'
    })
    points_utm = reproject_result['OUTPUT']

    # Step 2: Buffer each point by 100 metres
    buffer_result = processing.run("native:buffer", {
        'INPUT': points_utm,
        'DISTANCE': 100,
        'SEGMENTS': 8,
        'OUTPUT': 'memory:'
    })
    buffer_layer = buffer_result['OUTPUT']

    # Step 3: Zonal histogram - counts pixels per risk class within each buffer
    histogram_result = processing.run("native:zonalhistogram", {
        'INPUT_RASTER': risk_layer,
        'RASTER_BAND': 1,
        'INPUT_VECTOR': buffer_layer,
        'COLUMN_PREFIX': 'HISTO_',
        'OUTPUT': 'memory:'
    })
    result_layer = histogram_result['OUTPUT']

    provider = risk_layer.dataProvider()

    print("=== Validation Point Summary (100m buffer) ===\n")
    for feat in result_layer.getFeatures():
        point_id = feat['id'] if 'id' in feat.fields().names() else feat.id()

        # Exact risk class at the point itself
        point_geom = points_utm.getFeature(feat.id()).geometry().asPoint()
        value, ok = provider.sample(point_geom, 1)
        exact_class = {1: "Low", 2: "Medium", 3: "High"}.get(int(value) if ok else None, "Unknown")

        print(f"Point ID {point_id}: exact pixel = {exact_class} risk")

        # Buffer composition
        h1 = feat['HISTO_1'] if 'HISTO_1' in feat.fields().names() else 0
        h2 = feat['HISTO_2'] if 'HISTO_2' in feat.fields().names() else 0
        h3 = feat['HISTO_3'] if 'HISTO_3' in feat.fields().names() else 0
        total = (h1 or 0) + (h2 or 0) + (h3 or 0)

        if total > 0:
            print(f"  Within 100m buffer -> Low: {(h1 or 0)/total*100:.0f}%, "
                  f"Medium: {(h2 or 0)/total*100:.0f}%, High: {(h3 or 0)/total*100:.0f}%\n")
        else:
            print("  Buffer stats unavailable\n")
