# Rightmove Property Price Scraper

This Python script scrapes Rightmove.co.uk to find the median price of 3-bedroom properties in a specified location.

## Features

- Scrapes all available properties matching the criteria
- Handles pagination automatically
- Implements rate limiting to avoid being blocked
- Saves results to a CSV file
- Calculates median price
- Uses random user agents to avoid detection

## Requirements

- Python 3.7+
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Find your desired location code from Rightmove:
   - Go to Rightmove.co.uk
   - Search for your desired location
   - Look at the URL, it will contain a location identifier (e.g., "REGION^87490" for London)

2. Run the script:
```bash
python rightmove_scraper.py
```

3. The script will:
   - Search for all 3-bedroom properties in the specified location
   - Calculate the median price
   - Save the results to `property_prices.csv`
   - Display progress in the console

## Output

The script generates two types of output:
1. Console output showing progress and the final median price
2. A CSV file (`property_prices.csv`) containing all found properties with their prices

## Customization

To modify the search criteria, edit the `main()` function in `rightmove_scraper.py`:
- Change the `location` variable to your desired location code
- Modify `min_beds` and `max_beds` parameters in `search_properties()` if you want different bedroom counts

## Notes

- The script includes random delays between requests to avoid overwhelming the server
- It uses rotating user agents to avoid detection
- Results are saved to CSV for further analysis
- The script handles errors gracefully and includes logging

## Disclaimer

This script is for educational purposes only. Make sure to review and comply with Rightmove's terms of service and robots.txt before using this scraper. 