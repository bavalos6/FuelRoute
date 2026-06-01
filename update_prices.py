import requests
from bs4 import BeautifulSoup
import json
import datetime

def scrape_aaa_all_states():
    url = "https://gasprices.aaa.com/state-gas-price-averages/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # AAA lists state values in a clear table body layout
        table = soup.find('table')
        rows = table.find_all('tr') if table else []
        
        # Dict mapping state full names to 2-letter codes for your app logic
        state_map = {
            'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
            'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
            'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
            'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
            'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
            'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
            'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
            'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
            'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
            'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
        }
        
        data_output = {"regular": {}, "midgrade": {}, "premium": {}, "diesel": {}}
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                state_name = cols[0].get_text().strip()
                if state_name in state_map:
                    code = state_map[state_name]
                    # AAA column sequence: State | Regular | Midgrade | Premium | Diesel
                    data_output["regular"][code] = float(cols[1].get_text().replace('$','').strip())
                    data_output["midgrade"][code] = float(cols[2].get_text().replace('$','').strip())
                    data_output["premium"][code] = float(cols[3].get_text().replace('$','').strip())
                    data_output["diesel"][code] = float(cols[4].get_text().replace('$','').strip())
                    
        data_output["regular"]["DEFAULT"] = 3.50
        data_output["regular"]["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d")
        return data_output
        
    except Exception as e:
        print(f"Scraper error: {e}")
        return None

if __name__ == "__main__":
    all_data = scrape_aaa_all_states()
    if all_data and len(all_data["regular"]) > 0:
        with open('gas_prices.json', 'w') as f:
            json.dump(all_data, f, indent=2)
        print("Success! Generated a 50-state data tree mapping.")