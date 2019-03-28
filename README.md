# python3-escher-pattern

Generates:
* Escher pattern
* Checker board pattern

Used for camera systems optical calibration.
Outputs is a PDF file. No borders. Ready for printing.

![](https://community.elphel.com/pictures/escher_vs_checker.png)

# Recommendations

* Overall pattern rotation angle 0 is bad for correct MTF computation - because sensor pixel grid

# Requirements
* matplotlib

# Usage

## Docker

```
docker build --tag ep .
docker run -d -p 3113:5000 ep
```

Then:
```
http://localhost:3113/?PAGE_WIDTH=1524&PAGE_HEIGHT=3048&LPM=2.705449885575893&ROTATE=14.036243467
```

Parameters:
* **PAGE_WIDTH**  - page width in mm
* **PAGE_HEIGHT** - page width in mm
* **LPM**         - cell pairs per meter
* **ROTATE**      - pattern rotation angle
* **ESCHER**      - cell border curvature - at 0 or inf becomes a normal checker board. Max curvature is at ~2.4. Optimal - 2.0


## Command line

escher.py:
```
from escher_pattern import Escher_Pattern
ep = Escher_Pattern(width= 1524, height= 3048, escher=2, lpm=2.705449885575893, rotate=14.036243467)
ep.generate()
ep.save()
```

checkerboard.py:
```
from escher_pattern import Escher_Pattern
ep = Escher_Pattern(width= 1524, height= 3048, escher=0, lpm=2.705449885575893, rotate=14.036243467)
ep.generate()
ep.save()
```

Parameters:
* **width**  - page width in mm
* **height** - page width in mm
* **lpm**    - cell pairs per meter
* **rotate** - pattern rotation angle
* **escher** - cell border curvature - at 0 or inf becomes a normal checker board. Max curvature is at ~2.4. Optimal - 2.0
