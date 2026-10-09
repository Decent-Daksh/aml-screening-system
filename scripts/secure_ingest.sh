#!/bin/bash
set -e 

chmod 600 ../data/incoming_customers.csv
python3 ../src/screening_engine.py
mv ../data/incoming_customers.csv ../data/processed_customers_$(date +%F).csv