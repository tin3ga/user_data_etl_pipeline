#!/bin/bash

# Set Python interpreter path if needed
PYTHON=python

# Run extract.py
echo "Extracting data..."
$PYTHON src/extract.py

# Check if extract.py executed successfully
if [ $? -ne 0 ]; then
  echo "extract.py failed. Exiting."
  exit 1
fi

# Run transform.py
echo "Transforming data..."
$PYTHON src/transform.py

# Check if transform.py executed successfully
if [ $? -ne 0 ]; then
  echo "transform.py failed. Exiting."
  exit 1
fi


# Run load.py
echo "Loading data..."
$PYTHON src/load.py

# Check if transform.py executed successfully
if [ $? -ne 0 ]; then
  echo "load.py failed. Exiting."
  exit 1
fi

echo "Successfully loaded data"