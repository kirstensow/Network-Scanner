# Network Scanner

A Python tool that scans a list of IP addresses to check host 
availability and identify open ports, exporting results to JSON.

## Features
- Reads target IPs from a CSV file
- Checks if each host is alive by attempting connections on common ports
- Scans for open ports (80, 443, 22, 8080)
- Stores results in a structured dictionary
- Exports scan results to results.json

## How to Use
1. Add your target IP addresses to ips.csv
2. Run the script:
python3 NetworkScanner.py
3. Results are printed to terminal and saved to results.json

## Example Output
```json
{
  "192.168.1.1": {
    "status": "alive",
    "open_ports": [80, 443, 8080]
  },
  "192.168.1.254": {
    "status": "dead",
    "open_ports": []
  }
}
```

## Built With
- Python 3
- socket (built-in)
- csv (built-in)
- json (built-in)
