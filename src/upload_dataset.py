#!/usr/bin/env python3
"""
Script to create a Braintrust dataset from document files.
Complete the TODO items and run this script.
"""

import os
import glob
from braintrust import init_dataset, Attachment


def create_dataset_from_files():
    """Create a Braintrust dataset from files in the input_docs directory."""
    
    # TODO: Initialize a dataset with your project name and dataset name
    dataset = init_dataset(project="Your Project", name="Your Dataset")
    
    # TODO: Get all files from input_docs directory
    # Hint: Use glob.glob() to find files (e.g., "./input_docs/**/*.pdf")
    input_dir = "./input_docs/Training Dataset"
    files = []  # Your code here
    
    print(f"Found {len(files)} files to upload")
    
    for file_path in files:
        filename = os.path.basename(file_path)
        print(f"Uploading {filename}...")
        
        # TODO: Insert file into dataset
        # Hint: Use dataset.insert() with Attachment
        # dataset.insert(
        #     input={"file": Attachment(filename=filename, data=file_path)},
        #     expected="expected_output" <-- This needs to be pulled in from the ground_truth_pcap_extractions.json
        # )
        # Your code here
        pass
    
    print("Dataset upload completed!")

if __name__ == "__main__":
    print("Uploading dataset from files...")
    create_dataset_from_files()

