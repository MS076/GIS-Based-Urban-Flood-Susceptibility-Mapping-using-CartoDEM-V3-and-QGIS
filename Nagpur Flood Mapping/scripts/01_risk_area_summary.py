"""
Flood Risk Mapping - Nag River Basin, Nagpur
Script 1: Risk Category Area/Percentage Summary

Run this inside the QGIS Python Console (or Processing > Python Console script editor).
Requires the 'flood_risk_classified' raster layer to be loaded in the current project.

What it does:
Reads the final classified flood risk raster (values 1 = Low, 2 = Medium, 3 = High),
calculates the real-world area (km^2) covered by each risk class, and prints the
percentage share of the study area in each category.
"""

import numpy as np

# Get the classified risk layer from the project
layer = QgsProject.instance().mapLayersByName('flood_risk_classified')[0]
provider = layer.dataProvider()

# Read the raster as an array
block = provider.block(1, layer.extent(), layer.width(), layer.height())
data = np.array([[block.value(row, col) for col in range(layer.width())] for row in range(layer.height())])

# Pixel size (in map units - metres, since the layer is in UTM)
pixel_size_x = layer.rasterUnitsPerPixelX()
pixel_size_y = layer.rasterUnitsPerPixelY()
pixel_area_km2 = (pixel_size_x * pixel_size_y) / 1_000_000  # convert m^2 to km^2

# Count pixels per risk class (ignoring NoData / values outside 1-3)
total_valid = np.sum((data == 1) | (data == 2) | (data == 3))

print("=== Flood Risk Area Summary ===\n")
for risk_value, label in [(1, "Low Risk"), (2, "Medium Risk"), (3, "High Risk")]:
    count = np.sum(data == risk_value)
    area_km2 = count * pixel_area_km2
    percent = (count / total_valid) * 100 if total_valid > 0 else 0
    print(f"{label}: {area_km2:.2f} km^2 ({percent:.1f}%)")
