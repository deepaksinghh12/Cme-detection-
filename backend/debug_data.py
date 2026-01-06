import requests
import json
import sys
import time

def test_url(name, url):
    print(f"Testing {name}...")
    print(f"  URL: {url}")
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        elapsed = time.time() - start
        
        print(f"  Status: {response.status_code}")
        print(f"  Time: {elapsed:.2f}s")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"  ✅ JSON Valid. Items: {len(data)}")
                if len(data) > 0:
                    print(f"  Sample: {str(data[0])[:100]}...")
            except json.JSONDecodeError as e:
                print(f"  ❌ JSON Error: {e}")
                print(f"  Raw Content (first 100): {response.text[:100]}")
        else:
            print(f"  ❌ Failed status code")

    except Exception as e:
        print(f"  ❌ Connection Error: {e}")
    print("-" * 50)

if __name__ == "__main__":
    print("🚀 STARTING NOAA CONNECTIVITY TEST\n")
    
    test_url("NOAA Mag (7-day)", "https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json")
    test_url("NOAA Plasma (7-day)", "https://services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json")
    test_url("NOAA Alerts", "https://services.swpc.noaa.gov/products/alerts.json")
    test_url("NOAA DST Index", "https://services.swpc.noaa.gov/products/kyoto-dst.json")
    
    print("\nTests Complete.")
