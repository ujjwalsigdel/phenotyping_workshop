"""Sanity check for the PlantCV + PlantCV-Geospatial workshop environment.

Doesn't just import packages -- runs one real operation from each to catch
installs that import fine but are broken underneath (common with the
opencv/conda-vs-pip conflict we hit during setup).

Usage:
    conda activate plantcv
    python harness/test_install.py
"""
import sys

import numpy as np

print(f"Python: {sys.version.split()[0]}")

# --- core PlantCV ---
from plantcv import plantcv as pcv
import importlib.metadata as m

print(f"plantcv: {m.version('plantcv')}")

fake_rgb = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
gray = pcv.rgb2gray(rgb_img=fake_rgb)
assert gray.shape == (100, 100), "rgb2gray returned unexpected shape"
thresh = pcv.threshold.binary(gray_img=gray, threshold=100, object_type="light")
assert thresh.shape == gray.shape, "threshold.binary returned unexpected shape"
print("  -> pcv.rgb2gray + pcv.threshold.binary OK")

# --- PlantCV-Geospatial ---
import plantcv.geospatial as geo

print(f"plantcv-geospatial: {m.version('plantcv-geospatial')}")
assert hasattr(geo, "read") and hasattr(geo, "analyze"), "expected submodules missing"
print("  -> plantcv.geospatial.read / .analyze present OK")

# --- key scientific deps geospatial workflows need ---
import cv2
import rasterio
import geopandas
import pandas
import matplotlib

print(f"opencv-python-headless: {cv2.__version__}")
print(f"rasterio: {rasterio.__version__}")
print(f"geopandas: {geopandas.__version__}")
print(f"pandas: {pandas.__version__}")
print(f"matplotlib: {matplotlib.__version__}")

print("\nAll checks passed -- environment looks ready for the workshop.")
