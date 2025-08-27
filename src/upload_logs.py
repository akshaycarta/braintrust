#!/usr/bin/env python3
"""
Script to process PDFs using prompts from Braintrust and log interactions.
Complete the TODO items and run this script.
"""

import os
import glob
from braintrust import init_logger, load_prompt, wrap_openai, Prompt
from openai import OpenAI

# TODO: Initialize Braintrust logger with your project name
logger = init_logger(project="Your Project Name")


def process_test_dataset():
    """Process all PDFs in the test dataset using a saved prompt from Braintrust."""
    
    # TODO: Load a prompt from Braintrust

    prompt : Prompt =  load_prompt("your_project_name", "your_prompt_slug")
    
    # TODO: Initialize OpenAI client with Braintrust tracking
    # Hint: Use wrap_openai(OpenAI()) to enable automatic logging
    client = None  # Your code here

    # Get all PDF files in the test dataset directory
    test_pdf_dir = "./input_docs/PCAP docs/Test dataset"
    pdf_files = glob.glob(os.path.join(test_pdf_dir, "*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {test_pdf_dir}")
        return {}

    results = {}

    for pdf_path in pdf_files:
        filename = os.path.basename(pdf_path)
        print(f"Processing {filename}...")

        try:
            with open(pdf_path, "rb") as pdf_file:
                file = None  # Your code here

            # TODO: Create completion using the prompt and uploaded file. Be sure to include the file in the messages.
            completion = None  # Your code here using chat completions or responses API . Your call.
            
            # TODO: Extract the response content
            result = None
            
            results[filename] = result
            print(f"Completed processing {filename}")

            # TODO: Log the interaction to Braintrust
            # Hint: Use logger.log(inputs={"filename": filename}, output=result)
            # Your code here


        except Exception as e:
            print(f"Error processing {filename}: {e}")

    return results


if __name__ == "__main__":

    
    results = process_test_dataset()
    
