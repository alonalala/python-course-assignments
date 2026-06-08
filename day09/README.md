# Day 09: Genomic Sequence Predictor (Machine Learning)

## Overview
This project applies Machine Learning to genomic sequence data. It uses the **E. coli Promoter Gene Sequences Dataset** to train a Random Forest Classifier. The goal is to predict whether a given DNA sequence is a promoter (a regulatory element that initiates transcription) or a non-promoter, based entirely on its sequence grammar and nucleotide frequency.

## Dataset
* **Source:** UCI Machine Learning Repository
* **Data:** 106 DNA sequences, each 57 base pairs long.
* **Target:** `+` (Promoter) or `-` (Non-Promoter).

## How to Run
1. Navigate into the `day09` directory.
2. Install the required machine learning dependencies:
   ```bash
   python3 -m pip install -r requirements.txt

## AI Prompts Used
"Recommend a lightweight, publicly available biological dataset that involves DNA sequences or regulatory elements suitable for a basic machine learning classification task."

"Write a Python script using pandas and scikit-learn that automatically downloads this dataset, extracts sequence features like GC content and CpG counts, and trains a Random Forest model to predict the class."