import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from fake_useragent import UserAgent
from typing import List, Dict, Optional
import logging
from urllib.parse import urlencode
import matplotlib.pyplot as plt
import seaborn as sns

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RightmoveScraper:
    BASE_URL = "https://www.rightmove.co.uk/property-for-sale/find.html"
    
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
    
    def _get_headers(self) -> Dict[str, str]:
        """Generate random headers for each request to avoid detection."""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
    
    def _make_request(self, url: str, params: Optional[Dict] = None) -> Optional[BeautifulSoup]:
        """Make a request to Rightmove with error handling and rate limiting."""
        try:
            # Add random delay between requests (1-3 seconds)
            time.sleep(random.uniform(1, 3))
            
            # If params is provided, use it to construct the URL
            if params is not None:
                response = self.session.get(
                    url,
                    params=params,
                    headers=self._get_headers(),
                    timeout=10
                )
            else:
                # Use the pre-constructed URL directly
                response = self.session.get(
                    url,
                    headers=self._get_headers(),
                    timeout=10
                )
            
            response.raise_for_status()
            
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error making request to {url}: {str(e)}")
            return None
    
    def search_properties(self, location: str) -> List[Dict]:
        """Search for properties with specified criteria."""
        properties = []
        page = 0
        
        while True:

            params = {
                'sortType': 1,
                'viewType': 'LIST',
                'channel': 'BUY',

                'index': page * 24,
                'radius' : 0.0,
                'transactionType': 'BUY',
                'displayLocationIdentifier': 'undefined',
                'tenureTypes': 'FREEHOLD'
            }
            
            # Construct the URL manually to prevent double encoding
            url = f"{self.BASE_URL}?{urlencode(params)}&locationIdentifier={location}"

            if(page == 0):
                logger.info(f"url: {url}")
            
            soup = self._make_request(url)  # Note: removed params argument
            if not soup:
                break
            # Find all property cards
            
            property_cards = soup.find_all('div', class_='PropertyCard_propertyCardContainerWrapper__mcK1Z propertyCard-details')
            if not property_cards:
                break
            
            for card in property_cards:
                try:
                    #Remove the featured property
                    featured_property = card.find('span', {'aria-label':'Featured Property'})
                    if featured_property != None:
                        continue

                    # Extract price
                    price_text = card.find('div', class_='PropertyPrice_price__VL65t').text.strip()
        
                    # Convert price to integer (remove £ and commas)
                    price = int(price_text.replace('£', '').replace(',', ''))
                    
                    # Extract number of bedrooms
                    beds_text= card.find('span', {'class': 'PropertyInformation_bedroomsCount___2b5R'}).text.strip()
                    
                    # Get the property link
                    house_link = card.find('a', {'class': 'PropertyPrice_priceLink__b24b5'})
                    property_url = f"https://www.rightmove.co.uk{house_link['href']}" if house_link else None

                    # Get property type
                    property_type_text= card.find('span', {'class': 'PropertyInformation_propertyType__u8e76'}).text.strip()

                    properties.append({
                        'price': price,
                        'beds': beds_text,
                        'property_type': property_type_text,
                        'url': property_url
                    })
                    
                except (ValueError, AttributeError) as e:
                    logger.warning(f"Error parsing property card: {str(e)}")
                    continue
                
            # Also check if we've found any properties on this page
            if len(property_cards) == 1:
                logger.info("No properties found on current page, stopping pagination")
                break
            
            page += 1
            logger.info(f"Page {page}, cards found: {len(property_cards)}")
        
        return properties