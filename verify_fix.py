
import sys
import os
import asyncio
import logging
import pandas as pd
import numpy as np

# Add backend and scripts to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))
sys.path.append(os.path.join(os.getcwd(), 'backend', 'scripts'))

# Mock database module to avoid connection errors during import if DB is missing
sys.modules['database'] = type('MockDB', (), {'create_tables': lambda: None, 'init_sample_data': lambda: None})
sys.modules['db_service'] = type('MockDBService', (), {'db_service': None})

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    from backend.main import get_realtime_data, fill_noaa_missing_parameters
except ImportError:
    sys.path.append(os.getcwd())
    from backend.main import get_realtime_data, fill_noaa_missing_parameters

async def verify():
    print("Running verification of get_realtime_data...")
    
    # 1. Test fill_noaa_missing_parameters directly
    print("\nTest 1: fill_noaa_missing_parameters")
    df = pd.DataFrame({'bx_gsm': [1, 2, 3]}) # Missing speed, density, temperature
    print(f"Initial columns: {df.columns.tolist()}")
    
    df_filled = fill_noaa_missing_parameters(df)
    print(f"Filled columns: {df_filled.columns.tolist()}")
    
    if 'speed' in df_filled.columns and 'density' in df_filled.columns:
        print("✅ fill_noaa_missing_parameters correctly added missing columns.")
        print(f"Speed value: {df_filled['speed'].iloc[0]}")
    else:
        print("❌ fill_noaa_missing_parameters FAILED to add columns.")
    
    # 2. Test get_realtime_data endpoint logic
    print("\nTest 2: get_realtime_data endpoint")
    try:
        result = await get_realtime_data()
        
        print(f"Success: {result.get('success')}")
        sw = result.get('solar_wind', {})
        print("Solar Wind data:", sw)
        
        speed = sw.get('speed')
        density = sw.get('density')
        temp = sw.get('temperature')
        
        print(f"Speed: {speed} (Type: {type(speed)})")
        print(f"Density: {density} (Type: {type(density)})")
        print(f"Temperature: {temp} (Type: {type(temp)})")
        
        if speed is not None and density is not None and temp is not None:
             print("✅ VERIFICATION PASSED: All key parameters have values.")
        else:
             print("❌ VERIFICATION FAILED: Some parameters are None.")
             
    except Exception as e:
        print(f"❌ Execution failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(verify())
