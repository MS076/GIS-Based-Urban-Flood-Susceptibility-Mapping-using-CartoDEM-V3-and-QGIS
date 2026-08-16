# 🌊 GIS-Based Urban Flood Susceptibility Mapping using CartoDEM V3 and QGIS

> A GIS-based flood susceptibility assessment of the Ambazari–Sitabuldi–Mor Bhawan corridor, Nagpur, using CartoDEM V3, hydrological terrain analysis, and spatial overlay techniques.

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![QGIS](https://img.shields.io/badge/QGIS-4.2.0-green)
![GIS](https://img.shields.io/badge/Domain-GIS-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Project Overview

Urban flooding has become a recurring challenge in rapidly growing cities due to increasing impervious surfaces, inadequate drainage infrastructure, and complex terrain characteristics. Identifying flood-prone areas is essential for urban planning, infrastructure development, and disaster risk reduction.

This project develops a **GIS-based Urban Flood Susceptibility Map** for the **Ambazari–Sitabuldi–Mor Bhawan corridor in Nagpur, Maharashtra**, using **CartoDEM V3** and hydrological terrain analysis in **QGIS**.

Terrain parameters including **elevation**, **slope**, and **stream proximity** were derived from the Digital Elevation Model (DEM). These thematic layers were reclassified into flood susceptibility classes and combined using raster overlay analysis to generate the final flood-risk map. The results were validated against documented flood locations from the severe Nagpur flood event of 23 September 2023.

---

# 🎯 Objectives

- Develop a GIS-based urban flood susceptibility model.
- Process CartoDEM V3 to derive hydrological terrain characteristics.
- Generate drainage networks using DEM analysis.
- Identify flood-prone zones using terrain-based spatial analysis.
- Validate model outputs using historical flood-event locations.
- Demonstrate the application of GIS in urban flood-risk assessment.

---

# 📍 Study Area

**Location:** Ambazari – Sitabuldi – Mor Bhawan Corridor

**City:** Nagpur

**State:** Maharashtra

**Country:** India

The selected corridor frequently experiences urban flooding during intense rainfall events, making it an appropriate case study for terrain-based flood susceptibility assessment. This corridor was deliberately selected to correspond to the area most severely affected during the September 2023 Nagpur flood event, allowing the model's predictions to be validated against real, documented flood locations.

---

# 🛰 Dataset

- ISRO CartoDEM V3 Digital Elevation Model (DEM)
- Study Area Boundary
- Historical Flood Locations (September 2023 Nagpur flood event)
- OpenStreetMap (Reference Layers)

---

# 🛠 Software & Tools

- QGIS
- GRASS GIS Processing Tools
- GDAL
- Raster Calculator
- CartoDEM V3
- Python (QGIS Python Console) — for quantitative post-processing and validation statistics

---

# ⚙ Methodology

## Phase 1 – Data Preparation

- Prepared study area boundary
- Imported CartoDEM V3
- Clipped DEM to study area
- Fixed NoData values
- Reprojected raster to UTM coordinate system

---

## Phase 2 – Hydrological Terrain Processing

- Filled terrain sinks
- Generated flow direction
- Computed flow accumulation using **r.watershed**
- Delineated drainage network
- Verified drainage pattern against terrain characteristics

---

## Phase 3 – Flood Susceptibility Mapping

Generated thematic layers:

- Elevation
- Slope
- Stream Proximity

Each thematic layer was reclassified into flood susceptibility scores.

The reclassified layers were integrated using raster overlay analysis to generate the final flood susceptibility map.

A sieve filter was applied to remove isolated raster pixels and improve the visual quality of the output map.

Final Output:

```
final_output/flood_risk_classified.tif
final_output/accumulation.tif
```

---

## Phase 4 – Validation

Validation was performed by comparing predicted risk classification against documented locations affected during the 23 September 2023 Nagpur flood event, both by direct pixel sampling and by statistical summary of risk composition within a 100m buffer around each point (see `scripts/02_validation_buffer_stats.py`).

Locations checked:

- ✅ Ambazari
- ✅ Sitabuldi
- ✅ Mor Bhawan

**Results:**

- **Ambazari** — strong agreement. The exact point and 100% of its 100m buffer were classified as **high risk**, consistent with the naturally terrain-driven flooding at this location.
- **Sitabuldi corridor (both points)** — the model **under-predicted** risk here. Both points, and their surrounding 100m buffers, showed **no high-risk classification**, despite being severely affected during the actual 2023 event.

This pattern is consistent with documented drivers of the 2023 flood: encroachment reduced natural water retention areas, and built-up area in Nagpur nearly tripled between 2000 and 2023 — anthropogenic factors that a purely terrain-based DEM model cannot capture. The result demonstrates that DEM-derived terrain models are most reliable for naturally terrain-driven flood mechanisms (like Ambazari Lake), and require supplementary land-use and drainage-infrastructure data to adequately represent flood risk in dense urban corridors like Sitabuldi.

---

## Phase 5 – Future Enhancement

Planned improvements include:

- Integration of land-use/land-cover (LULC) and impervious-surface data
- Integration of rainfall intensity datasets
- Incorporation of engineered stormwater drainage-network data
- Export of analysis results in additional formats

---

# 🔄 Workflow

```text
CartoDEM V3
      │
      ▼
Study Area Clipping
      │
      ▼
DEM Preprocessing
      │
      ▼
Fill Sinks
      │
      ▼
Flow Direction
      │
      ▼
Flow Accumulation
      │
      ▼
Drainage Extraction
      │
      ▼
Slope Generation
      │
      ▼
Stream Proximity Analysis
      │
      ▼
Raster Reclassification
      │
      ▼
Raster Overlay Analysis
      │
      ▼
Flood Susceptibility Map
      │
      ▼
Validation using Historical Flood Events
```

---

# 📊 Results

The project successfully generated a GIS-based flood susceptibility map that classifies the study area into three flood-risk categories (Low, Medium, High) based on terrain characteristics.

Quantitative breakdown of the study area by risk category:

| Risk Category | Area (km²) | Percentage |
|---|---|---|
| Low Risk | 17.70 | 36.6% |
| Medium Risk | 24.33 | 50.3% |
| High Risk | 6.37 | 13.2% |

Key outputs include:

- Digital Elevation Model (DEM)
- Slope Map
- Flow Accumulation Map
- Drainage Network
- Stream Proximity Raster
- Flood Susceptibility Map

Validation showed strong agreement at Ambazari Lake, but under-prediction of risk in the urbanized Sitabuldi corridor — see Phase 4 above for full discussion.

---

# 📂 Repository Structure

```
GIS-Based-Urban-Flood-Susceptibility-Mapping-using-CartoDEM-V3-and-QGIS/
│
├── README.md
├── LICENSE
│
└── Nagpur Flood Mapping/
    │
    ├── report.pdf
    │
    ├── images/
    │   ├── Study area.png
    │   ├── workflow.png
    │   ├── dem.png
    │   ├── slope.png
    │   ├── slope risk.png
    │   ├── elevation Risk.png
    │   ├── Proximity Risk.png
    │   ├── flow_acculumation.png
    │   ├── fill_sinks_flow_direction.png
    │   ├── fill_sinks_watershed_basins.png
    │   └── final risk map.png
    │
    ├── qgis_project/
    │   └── Flood_mapping.qgz
    │
    ├── final_output/
    │   ├── flood_risk_classified.tif
    │   └── accumulaion.tif
    │
    ├── tif/
    │   └── (intermediate raster files: DEM, slope, elevation_risk,
    │        slope_risk, proximity_risk, stream_mask, etc.)
    │
    └── scripts/
        ├── 01_risk_area_summary.py
        └── 02_validation_buffer_stats.py
```

---

# 📷 Sample Outputs

> screenshots of the following maps:

- Study Area
- CartoDEM
- Slope
- Elevation Risk
- Slope Risk
- Stream Proximity Risk
- Flow Accumulation
- Drainage Network
- Final Flood Susceptibility Map

---

# 🚀 Future Improvements

- Integrate rainfall intensity datasets
- Include land-use and land-cover (LULC) analysis
- Incorporate soil permeability
- Apply Multi-Criteria Decision Analysis (MCDA)
- Extend the methodology to larger urban regions

---

# 👩‍💻 Author

**Muskaan Suraj Sharma**

B.Tech Civil Engineering

Visvesvaraya National Institute of Technology (VNIT), Nagpur

---

# 📜 License

This project is released under the MIT License.

---

# ⭐ Acknowledgements

- ISRO Bhuvan for CartoDEM data
- QGIS Development Team
- GRASS GIS
- GDAL Developers
- OpenStreetMap Contributors
