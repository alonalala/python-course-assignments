import requests
import pandas as pd
import argparse
import sys

def fetch_regulatory_features(species, chromosome, start, end):
    """Fetches regulatory features for a genomic region from the Ensembl REST API."""
    print(f"Fetching data from Ensembl for {species} chr{chromosome}:{start}-{end}...")
    
    server = "https://rest.ensembl.org"
    endpoint = f"/overlap/region/{species}/{chromosome}:{start}-{end}?feature=regulatory"
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.get(server + endpoint, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Ensembl: {e}")
        sys.exit(1)

def process_features(data, output_file):
    """Processes the raw JSON API data into a summary and saves a CSV."""
    if not data:
        print("No regulatory features found in this region.")
        return

    # Extract the fields we actually care about
    processed_records = []
    for item in data:
        processed_records.append({
            'Feature_ID': item.get('id'),
            'Type': item.get('description'),
            'Chromosome': item.get('seq_region_name'),
            'Start': item.get('start'),
            'End': item.get('end'),
            'Length (bp)': item.get('end') - item.get('start') + 1,
            'Strand': '+' if item.get('strand') == 1 else '-'
        })

    # Convert to a Pandas DataFrame for easy analysis
    df = pd.DataFrame(processed_records)
    
    # 1. Print a summary to the console
    print("\n--- Region Summary ---")
    print(f"Total regulatory features found: {len(df)}")
    print("\nFeature breakdown by type:")
    print(df['Type'].value_counts().to_string())
    
    print(f"\nAverage feature length: {df['Length (bp)'].mean():.1f} bp")
    print(f"Longest feature: {df['Length (bp)'].max()} bp")

    # 2. Save the full processed data to a CSV
    df.to_csv(output_file, index=False)
    print(f"\nDetailed data successfully saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and process Ensembl regulatory features.")
    parser.add_argument("--species", default="human", help="Species to query (e.g., human, mouse)")
    parser.add_argument("--chrom", default="11", help="Chromosome number")
    parser.add_argument("--start", default="5200000", help="Start coordinate")
    parser.add_argument("--end", default="5300000", help="End coordinate")
    parser.add_argument("--output", default="regulatory_features.csv", help="Output CSV filename")
    
    args = parser.parse_args()
    
    # Run the pipeline
    raw_data = fetch_regulatory_features(args.species, args.chrom, args.start, args.end)
    process_features(raw_data, args.output)