from pathlib import Path
import pandas as pd
from src.utils.io import read_csv, write_csv, ensure_dir

def ingest(raw_path: str, output_path: str) -> Path:
    """Ingest raw data from CSV, perform basic cleaning and save cleaned data."""
    df = read_csv(raw_path) #read raw data
    df = df.drop_duplicates() #simple cleanup
    out = Path(output_path)
    ensure_dir(out.parent) #ensure folder exists
    write_csv(df, out) #save cleaned raw
    return out    
