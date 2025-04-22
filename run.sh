#!/bin/bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Streamlit
pip install streamlit

# Run Streamlit app
streamlit run app.py
