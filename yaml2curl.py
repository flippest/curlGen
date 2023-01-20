#!/usr/bin/env python3

import yaml
import requests

# Load the YAML file
with open("file.yaml") as f:
    data = yaml.safe_load(f)

# Extract the necessary information from the YAML file
url = data["url"]
method = data["method"]
headers = data.get("headers", {})
data = data.get("data", {})

# Construct the curl command
curl_command = f"curl -X {method} {url}"

# Add headers
for key, value in headers.items():
    curl_command += f" -H '{key}: {value}'"

# Add data
if data:
    curl_command += f" -d '{data}'"

# Print the curl command
print(curl_command)

