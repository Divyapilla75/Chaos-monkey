#!/bin/bash

# Set errexit and nounset to catch errors early
set -euo pipefail

# Define the YAML filename
yamlname="podfailure.yaml"  # Set the default YAML filename

# Function to execute a command and wait for user input before proceeding
run_command() {
  echo "Executing: $1"
  eval "$1"  # Use quotes to prevent word splitting
  read -p "Press [Enter] key to continue..."
  echo  # Add a newline after the prompt
}

# Apply the YAML file
run_command "kubectl apply -f \"$yamlname\" -n ps"  # Quote the filename

# Delete the YAML file
run_command "kubectl delete -f \"$yamlname\" -n ps"  # Quote the filename

echo "Script completed."