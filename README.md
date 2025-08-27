# Braintrust Coding Session

This repository contains examples and tools for working with Braintrust to upload datasets and load prompts.

## Setup Instructions

### 1. Install Dependencies

Choose either Poetry or pip:

#### Option A: Using pip (Recommended)
```bash
pip install -e .
```
#### Option B: Using Poetry

```bash
poetry install
```



### 2. Environment Setup

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```
export BRAINTRUST_API_KEY=your_api_key_here
export OPENAI_API_KEY=your_openai_api_key_here
```

Load the environment variables:

```bash
source .env
```

### 3. Activate Environment (Poetry only)

If you used Poetry, activate the shell:
```bash
poetry shell
```

If you used pip, you're ready to go!

## Session Goals

This session focuses on two main tasks:

### 1. Upload Datasets (`upload_dataset.py`)
- Upload documents from `input_docs/Training Dataset` to Braintrust
- Create datasets with file attachments
- Simple TODO items to complete

### 2. Upload Logs (`upload_logs.py`) 
- Load prompts from Braintrust
- Make API calls to OpenAI
- Log interactions for tracking and evaluation

## Getting Started

### Step 1: Place Your Documents

Download documents from the google drive and place them in the `input_docs/` directory. 

**DO NOT COMMIT THE DOCS** since this is a public repo





### Step 2: Upload Dataset
```bash
# Complete the TODOs in this file, then run:
python upload_dataset.py
```

### Step 3: Upload Logs
```bash
# Complete the TODOs in this file, then run:
python upload_logs.py
```

