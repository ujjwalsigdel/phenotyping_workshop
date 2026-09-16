"""Minimal PlantCV analysis demo: segment a plant from its background and
extract shape/size traits. This mirrors the kind of single-plant workflow
covered in the morning session (fundamentals) before the afternoon's
geospatial walkthroughs.

Uses a synthetic image (a green blob on brown "soil") instead of a real
photo, so it runs standalone with no data files needed. Swap
`make_fake_plant_image()` for `cv2.imread("your_photo.jpg")` to run this on
a real picture.

Usage:
    conda activate plantcv
    python harness/plantcv_demo.py
"""
import numpy as np
import cv2

from plantcv import plantcv as pcv


def make_fake_plant_image(size=400):
    """Brown background + a green, leaf-shaped blob in the middle."""
    img = np.zeros((size, size, 3), dtype=np.uint8)
    img[:, :] = (30, 60, 90)  # BGR "soil" brown

    mask = np.zeros((size, size), dtype=np.uint8)
    cv2.ellipse(mask, (size // 2, size // 2), (90, 60), 30, 0, 360, 255, -1)
    cv2.ellipse(mask, (size // 2 - 40, size // 2 + 20), (50, 30), -20, 0, 360, 255, -1)

    green = np.zeros_like(img)
    green[:, :] = (40, 160, 60)  # BGR green
    img = np.where(mask[..., None] > 0, green, img)
    return img


def main():
    pcv.params.debug = None  # no plot pop-ups; we're running headless

    img = make_fake_plant_image()

    # 1. Isolate the plant: saturation channel makes green stand out from soil.
    sat = pcv.rgb2gray_hsv(rgb_img=img, channel="s")
    mask = pcv.threshold.otsu(gray_img=sat, object_type="light")

    # 2. Clean up small noise specks.
    clean_mask = pcv.fill(bin_img=mask, size=50)

    # 3. Label connected plant regions.
    labeled_mask, n_labels = pcv.create_labels(mask=clean_mask)
    print(f"Detected {n_labels} plant object(s).")

    # 4. Extract shape/size traits (area, height, width, convex hull, etc.).
    pcv.outputs.clear()
    _ = pcv.analyze.size(img=img, labeled_mask=labeled_mask, n_labels=n_labels)

    traits = pcv.outputs.observations["default_1"]
    print("\nExtracted traits:")
    for name, obs in traits.items():
        print(f"  {name}: {obs['value']} {obs['scale']}")

    out_path = "plantcv_demo_output.png"
    cv2.imwrite(out_path, clean_mask)
    print(f"\nSaved segmented mask to {out_path}")


if __name__ == "__main__":
    main()
