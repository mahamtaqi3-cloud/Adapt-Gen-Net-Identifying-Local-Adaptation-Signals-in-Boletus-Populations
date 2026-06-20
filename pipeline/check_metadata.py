import json
import rasterio
import csv
import os

# 1. Detect Paths automatically  
base_dir = os.getcwd()
# This will check line that assembly file is in 'data' folder
json_file = os.path.join(base_dir, "data", "assembly_data_report.jsonl")
# This line will find climate file in 'environment_data' folder 
tif_file = os.path.join(base_dir, "environment_data", "CHELSA_bio01_1981-2010_V.2.1.tif")
output_csv = "climate_genomic_data.csv"

print(f" Finding Dataset...")

# 2. File Check
if not os.path.exists(json_file):
    print(f"ERROR: File not found here: {json_file}")
    exit()

# 3. Processing
try:
    with open(json_file, 'r', encoding='utf-8') as f, rasterio.open(tif_file) as src, open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Sample_ID', 'Latitude', 'Longitude', 'Climate_Value'])
        
        for line in f:
            data = json.loads(line)
            biosample = data.get('assemblyInfo', {}).get('biosample', {})
            lat_lon = biosample.get('latLon', '')
            
            if lat_lon:
                parts = lat_lon.split()
                # Coordinate parsing (N/S/E/W support)
                lat = float(parts[0]) if 'N' in parts[1] else -float(parts[0])
                lon = float(parts[2]) if 'E' in parts[3] else -float(parts[3])
                
                # Raster value extraction
                row, col = src.index(lon, lat)
                val = src.read(1)[row, col]
                
                writer.writerow([data.get('accession'), lat, lon, val])
                print(f"Processed: {data.get('accession')} -> Climate Value: {val}")

    print(f"\nSUCCESS! Work Done. Data '{output_csv}' is saved.")

except Exception as e:
    print(f"Error: {e}")
