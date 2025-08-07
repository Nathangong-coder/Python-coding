# This script generates an SVG with puzzle outlines overlaid on a photo for laser cutting
# Note: The actual execution of this should be done in an environment that supports image and vector processing (e.g., Python with PIL and svgwrite)

from PIL import Image
import svgwrite
import numpy as np

# Load image
img_path = "C:/Users/NGong/Downloads/dad photo.JPG"
img = Image.open(img_path)
img = img.convert("L")  # convert to grayscale for engraving effect
width, height = img.size

# Define puzzle grid (e.g. 6x6 for 36 pieces)
puzzle_rows = 6
puzzle_cols = 6
cell_w = width / puzzle_cols
cell_h = height / puzzle_rows

# Create SVG
dwg = svgwrite.Drawing("dad_puzzle.svg", size=(f"{width}px", f"{height}px"))

# Add puzzle piece lines in red (0.01 thickness)
for i in range(puzzle_cols + 1):
    x = i * cell_w
    dwg.add(dwg.line(start=(x, 0), end=(x, height), stroke="red", stroke_width=0.01))
for j in range(puzzle_rows + 1):
    y = j * cell_h
    dwg.add(dwg.line(start=(0, y), end=(width, y), stroke="red", stroke_width=0.01))

# Save the SVG file
dwg.save()

# (In practice, you'd also overlay a halftone-processed or grayscale-engraved version of the image
# or raster it separately depending on the laser cutter's capability.)
