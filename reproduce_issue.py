
import sys
import os
import logging
import pandas as pd
import numpy as np

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    from backend.noaa_realtime_data import get_combined_realtime_data, get_real_plasma_data
    print("Function imported successfully.")
except ImportError:
    # Try alternate import if run from inside backend
    sys.path.append(os.getcwd())
    from noaa_realtime_data import get_combined_realtime_data, get_real_plasma_data
    print("Function imported successfully (alternate).")

print("\n--- Testing Plasma Data Alone ---")
plasma_res = get_real_plasma_data()
print(f"Plasma Success: {plasma_res.get('success')}")
if not plasma_res.get('success'):
    print(f"Plasma Error: {plasma_res.get('error')}")
else:
    pdf = plasma_res.get('data')
    print(f"Plasma Columns: {pdf.columns.tolist()}")
    print(f"Plasma Rows: {len(pdf)}")

print("\n--- Testing Combined Data ---")
result = get_combined_realtime_data()

print(f"Combined Success: {result.get('success')}")
print(f"Source: {result.get('source')}")
print(f"Note: {result.get('note')}")

if result.get('success'):
    df = result.get('data')
    print(f"Combined Data shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    
    # Check for specific columns
    missing_cols = []
    for col in ['speed', 'density', 'temperature']:
        if col not in df.columns:
            missing_cols.append(col)
        else:
            # Check if all null
            if df[col].isna().all():
                print(f"Column '{col}' exists but is ALL NULL")

    if missing_cols:
        print(f"MISSING PLASMA COLUMNS: {missing_cols}")
    else:
        print("All plasma columns present.")
else:
    print("Error:", result.get('error'))
