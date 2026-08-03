# 🌊 GIS-Based Urban Flood Susceptibility Mapping using CartoDEM V3 and QGIS

> A GIS-based flood susceptibility assessment of the Ambazari–Sitabuldi–Mor Bhawan corridor, Nagpur, using CartoDEM V3, hydrological terrain analysis, and spatial overlay techniques.

![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)
![QGIS](https://img.shields.io/badge/QGIS-3.x-green)
![GIS](https://img.shields.io/badge/Domain-GIS-blue)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Project Overview

Urban flooding has become a recurring challenge in rapidly growing cities due to increasing impervious surfaces, inadequate drainage infrastructure, and complex terrain characteristics. Identifying flood-prone areas is essential for urban planning, infrastructure development, and disaster risk reduction.

This project develops a **GIS-based Urban Flood Susceptibility Map** for the **Ambazari–Sitabuldi–Mor Bhawan corridor in Nagpur, Maharashtra**, using **CartoDEM V3** and hydrological terrain analysis in **QGIS**.

Terrain parameters including **elevation**, **slope**, and **stream proximity** were derived from the Digital Elevation Model (DEM). These thematic layers were reclassified into flood susceptibility classes and combined using raster overlay analysis to generate the final flood-risk map. The results are being validated against historical flood-event locations reported within the study area.

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

The selected corridor frequently experiences urban flooding during intense rainfall events, making it an appropriate case study for terrain-based flood susceptibility assessment.

---

# 🛰 Dataset

- ISRO CartoDEM V3 Digital Elevation Model (DEM)
- Study Area Boundary
- Historical Flood Locations
- OpenStreetMap (Reference Layers)

---

# 🛠 Software & Tools

- QGIS
- GRASS GIS Processing Tools
- GDAL
- Raster Calculator
- CartoDEM V3
- Python *(planned for workflow automation)*

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
flood_risk_smoothed.tif
```

---

## Phase 4 – Validation (In Progress)

Validation is being performed by comparing predicted high-risk areas with historical flood-event locations within the study area.

Current Progress:

- ✅ Ambazari Lake
- ✅ Sitabuldi (Location 1)
- ✅ Sitabuldi (Location 2)
- 🔄 Variety Chowk / Mor Bhawan

---

## Phase 5 – Future Enhancement

Planned improvements include:

- Python-based workflow automation
- Statistical summary generation
- Automatic raster classification
- Export of analysis results
- Integration of rainfall and land-use datasets

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

The project successfully generated a GIS-based flood susceptibility map that classifies the study area into different flood-risk categories based on terrain characteristics.

Key outputs include:

- Digital Elevation Model (DEM)
- Slope Map
- Flow Accumulation Map
- Drainage Network
- Stream Proximity Raster
- Flood Susceptibility Map

Initial validation indicates good agreement between predicted high-risk zones and known flood-event locations.

---

# 📂 Repository Structure

```
urban-flood-susceptibility-mapping/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── images/
│   ├── study_area.png
│   ├── workflow.png
│   ├── dem.png
│   ├── slope.png
│   ├── flow_accumulation.png
│   ├── drainage_network.png
│   ├── stream_proximity.png
│   ├── flood_risk_map.png
│   └── validation.png
│
├── qgis_project/
│   └── UrbanFloodMapping.qgz
│
├── outputs/
│   ├── flood_risk_smoothed.tif
│   └── flood_risk_map.pdf
│
├── docs/
│   └── Project_Report.pdf
│
└── scripts/
    └── flood_analysis.py
```

---

# 📷 Sample Outputs

> screenshots of the following maps:

- Study Area
- CartoDEM
- Slope
- Flow Accumulation
- Drainage Network
- Stream Proximity
- Final Flood Susceptibility Map

---

# 🚀 Future Improvements

- Integrate rainfall intensity datasets
- Include land-use and land-cover (LULC) analysis
- Incorporate soil permeability
- Apply Multi-Criteria Decision Analysis (MCDA)
- Develop an automated Python processing workflow
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
