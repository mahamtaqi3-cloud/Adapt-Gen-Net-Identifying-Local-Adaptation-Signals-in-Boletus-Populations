import rasterio
import pandas as pd
import os

# 1. Load the metadata
metadata = pd.read_csv('sample_metadata.csv')

# 2. Define path to  environment data folder
# Old path: climate_dir = '../data/environment_data'
# New path (that is correct according to folder structure):
climate_dir = '../data/environment_data'
# 2. Define path to your environment data folder
# Apne PC ka poora path yahan copy-paste karein:
climate_dir = r"C:\Users\abdul\OneDrive\Desktop\Adapt Gen\Adapt-Gen-Net\data\environment_data"
# 3. Get a list of all .tif files
tif_files = [f for f in os.listdir(climate_dir) if f.endswith('.tif')]
print(f"📁 Found {len(tif_files)} climate raster files.")

# 4. Extract climate data for each sample
for index, row in metadata.iterrows():
    lat, lon = row['Latitude'], row['Longitude']
    print(f"📍 Extracting data for {row['Sample_ID']}...")
    
    for tif in tif_files:
        tif_path = os.path.join(climate_dir, tif)
        with rasterio.open(tif_path) as src:
            # Get the pixel index from geographic coordinates
            try:
                py, px = src.index(lon, lat)
                val = src.read(1)[py, px]
                metadata.at[index, tif] = val
            except IndexError:
                print(f"⚠️ Warning: Coordinates for {row['Sample_ID']} are outside the map bounds.")

# 5. Save the new integrated dataset
metadata.to_csv('integrated_climate_data.csv', index=False)
print("\n✅ SUCCESS: Climate data saved to 'integrated_climate_data.csv'!")
