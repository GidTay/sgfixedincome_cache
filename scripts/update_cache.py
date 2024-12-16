import pandas as pd
from datetime import datetime
import json
import os
from sgfixedincome_pkg import consolidate
from zoneinfo import ZoneInfo  # Python 3.9+

def update_cache():
    """Update the cache with new data, maintaining at most two versions:
    - current version (always the most recent)
    - latest successful version (only if different from current)
    """
    # Create cache directory if it doesn't exist
    os.makedirs("cache", exist_ok=True)
    
    # Load existing metadata or create new
    metadata_path = "cache/metadata.json"
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
    else:
        metadata = {"current_version": None, "latest_successful": None}
    
    # Get new data
    df, fetch_failures, warnings = consolidate.create_combined_df()
    
    # Generate timestamp in Singapore time
    sg_time = datetime.now(ZoneInfo("Asia/Singapore"))
    timestamp = sg_time.strftime("%Y%m%d_%H%M%S")
    
    # Create current version info
    current_version = {
        "timestamp": timestamp,
        "fetch_failures": fetch_failures,
        "warnings": warnings
    }
    
    # Save current data
    df.to_json("cache/data_current.json", orient="records")
    
    # Update metadata
    metadata["current_version"] = current_version
    
    # If this is a successful fetch, update latest_successful
    if not fetch_failures:
        metadata["latest_successful"] = current_version
        # Save successful version separately
        df.to_json("cache/data_latest_successful.json", orient="records")
    
    # Save metadata
    with open(metadata_path, "w") as f:
        json.dump(metadata, f)

if __name__ == "__main__":
    update_cache()