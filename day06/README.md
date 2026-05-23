# Day 06: Genomic Regulatory Feature Fetcher

## Overview
This assignment queries the **Ensembl REST API**, a major scientific database providing programmatic access to comprehensive genomic data. 

While the basic NCBI API is often used for retrieving nucleotide sequences, this script targets the Ensembl `overlap` endpoint specifically to download **Regulatory Features** (such as promoters, enhancers, and transcription factor binding sites). 

The script downloads JSON data for a specific genomic region, processes the raw dictionary to extract biological metadata, calculates length statistics, summarizes the feature types, and exports a clean CSV.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run with default parameters (Human Chromosome 11 beta-globin region): 
   `python ensembl_fetcher.py`
3. Run with custom parameters:
   `python ensembl_fetcher.py --species mouse --chrom 17 --start 30000000 --end 30050000 --output mouse_enhancers.csv`

## AI Interaction
I used AI to help identify an API that was relevant to my specific field of study (epigenetics and cis-regulatory elements). The AI suggested the Ensembl REST API and helped me correctly format the HTTP headers to request `application/json` data, rather than the default XML, making the downstream processing much cleaner.