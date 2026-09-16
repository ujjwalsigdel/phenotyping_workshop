"""Real single-plant PlantCV analysis, adapted from the Danforth Center's
official tutorial:
https://github.com/danforthcenter/plantcv-tutorial-v4-VIS-single-plant

Runs on a real photo (data/B73_sand_2023-04-14.jpg, a maize B73 seedling in
sand, downloaded from that tutorial repo) instead of synthetic data:
color-correct against the color card in frame -> threshold the plant out of
the background -> restrict to a region of interest -> extract shape and
color traits.

Usage:
    conda activate plantcv
    python scripts/analyze_plant.py
"""
import os

from plantcv import plantcv as pcv

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(HERE, "data", "B73_sand_2023-04-14.jpg")
OUT_DIR = os.path.join(HERE, "output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    pcv.params.debug = None  # headless: we save images instead of plotting
    pcv.params.sample_label = "default"

    # 1. Read the image.
    img, _, _ = pcv.readimage(filename=IMG_PATH)

    # 2. Crop to the region containing the plant + color card (tuned to this
    #    camera's framing, per the original tutorial).
    crop_img = pcv.crop(img=img, x=1500, y=0, h=2900, w=2500)

    # 3. Color-correct using the color card visible in the photo, so
    #    downstream thresholds are consistent regardless of lighting.
    source_matrix = pcv.transform.detect_color_card(rgb_img=crop_img)
    std_matrix = pcv.transform.std_color_matrix(pos=3)
    img_cc = pcv.transform.affine_color_correction(crop_img, source_matrix, std_matrix)
    pcv.print_image(img_cc, filename=os.path.join(OUT_DIR, "01_color_corrected.png"))

    # 4. Threshold the plant out of the background using the Lab a/b channels
    #    (green plant pixels separate cleanly from soil/card there).
    thresh = pcv.threshold.dual_channels(
        rgb_img=img_cc, x_channel="a", y_channel="b", points=[(80, 80), (125, 140)], above=True
    )
    filled = pcv.fill(bin_img=thresh, size=50)
    filled = pcv.fill_holes(filled)
    pcv.print_image(filled, filename=os.path.join(OUT_DIR, "02_mask.png"))

    # 5. Restrict to a region of interest that covers the plant but excludes
    #    the color card.
    roi = pcv.roi.rectangle(img=img_cc, x=540, y=0, h=2500, w=1500)
    kept_mask = pcv.roi.filter(mask=filled, roi=roi, roi_type="partial")

    # 6. Extract shape and color traits.
    pcv.outputs.clear()
    size_img = pcv.analyze.size(img=img_cc, labeled_mask=kept_mask)
    pcv.print_image(size_img, filename=os.path.join(OUT_DIR, "03_size_analysis.png"))

    color_img = pcv.analyze.color(rgb_img=img_cc, labeled_mask=kept_mask, colorspaces="all")
    pcv.print_image(color_img, filename=os.path.join(OUT_DIR, "04_color_analysis.png"))

    # 7. Print + save the extracted trait values.
    print("Extracted traits:")
    for sample, traits in pcv.outputs.observations.items():
        for name, obs in traits.items():
            value = obs["value"]
            if isinstance(value, list):
                continue  # skip full histograms/spectra in the printout
            print(f"  [{sample}] {name}: {value} {obs['scale']}")

    results_path = os.path.join(OUT_DIR, "results.json")
    pcv.outputs.save_results(filename=results_path)
    print(f"\nFull results (including histograms) saved to {results_path}")
    print(f"Annotated images saved to {OUT_DIR}/")


if __name__ == "__main__":
    main()
