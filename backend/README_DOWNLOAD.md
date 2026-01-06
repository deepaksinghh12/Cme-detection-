# OMNIWeb Data File Download Guide

## Browser se Download Kaise Karein

### Method 1: Direct Browser Download

1. **NASA SPDF Website pe jao:**
   ```
   https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/
   ```

2. **File list mein se year select karo:**
   - Example: `omni2_2023.dat` (2023 ke liye)
   - Example: `omni2_2024.dat` (2024 ke liye)

3. **File pe click karo:**
   - Browser automatically download start kar dega
   - Ya right-click → "Save Link As" / "Save Target As"

4. **File save location:**
   - Downloads folder mein save hoga
   - Ya apni preferred location choose karo

### Method 2: Python Script se Download

```bash
# Single year download
python download_omni_file.py 2023

# Multiple years (manually run for each)
python download_omni_file.py 2024
python download_omni_file.py 2022
```

### Method 3: Direct URL se Download

Browser address bar mein directly URL paste karo:

```
https://spdf.gsfc.nasa.gov/pub/data/omni/low_res_omni/omni2_2023.dat
```

Replace `2023` with your desired year.

## File Format

- **Format:** ASCII/space-separated text file
- **Size:** ~50-100 MB per year (depends on year)
- **Columns:** Multiple space-separated columns
- **Header:** Usually first few lines contain column descriptions

## File Structure Example

```
YEAR DOY HR BX BY BZ BT SPEED DENSITY TEMP ...
2023 274  0  2.2  0.1  1.1  4.2  321  5.2  60845 ...
2023 274  1  4.6 -1.3 -0.6  3.1  345  6.1  72010 ...
```

## Notes

- Files are large (50-100 MB per year)
- Download time depends on internet speed
- Files contain ALL parameters in one file (no API limitations!)
- Can be used directly with our CSV parsing approach









