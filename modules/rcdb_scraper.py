import time
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

BASE_URL = "https://rcdb.com"
REQUEST_DELAY = 0.01

HEADERS = {
    "User-Agent": "Mozilla/5.0 (educational research)"
}

PARKS = {
    # Cedar Fair (Legacy)
    "Cedar Point": {"url": "https://rcdb.com/4529.htm", "chain": "Cedar Fair"},
    "Kings Island": {"url": "https://rcdb.com/4540.htm", "chain": "Cedar Fair"},
    "Carowinds": {"url": "https://rcdb.com/4542.htm", "chain": "Cedar Fair"},
    "Canada's Wonderland": {"url": "https://rcdb.com/4539.htm", "chain": "Cedar Fair"},
    "Knott's Berry Farm": {"url": "https://rcdb.com/4546.htm", "chain": "Cedar Fair"},
    "California's Great America": {"url": "https://rcdb.com/4541.htm", "chain": "Cedar Fair"},
    "Kings Dominion": {"url": "https://rcdb.com/4544.htm", "chain": "Cedar Fair"},
    "Dorney Park": {"url": "https://rcdb.com/4588.htm", "chain": "Cedar Fair"},
    "Worlds of Fun": {"url": "https://rcdb.com/4533.htm", "chain": "Cedar Fair"},
    "Valleyfair": {"url": "https://rcdb.com/4552.htm", "chain": "Cedar Fair"},
    "Michigan's Adventure": {"url": "https://rcdb.com/4578.htm", "chain": "Cedar Fair"},

    # Six Flags 
    "Six Flags Magic Mountain": {"url": "https://rcdb.com/4532.htm", "chain": "Six Flags"},
    "Six Flags Great Adventure & Safari": {"url": "https://rcdb.com/4534.htm", "chain": "Six Flags"},
    "Six Flags Great America": {"url": "https://rcdb.com/4530.htm", "chain": "Six Flags"},
    "Six Flags Over Texas": {"url": "https://rcdb.com/4531.htm", "chain": "Six Flags"},
    "Six Flags Fiesta Texas": {"url": "https://rcdb.com/4538.htm", "chain": "Six Flags"},
    "Six Flags Over Georgia": {"url": "https://rcdb.com/4535.htm", "chain": "Six Flags"},
    "Six Flags New England": {"url": "https://rcdb.com/4565.htm", "chain": "Six Flags"},
    "Six Flags Discovery Kingdom": {"url": "https://rcdb.com/4711.htm", "chain": "Six Flags"},
    "Six Flags St. Louis": {"url": "https://rcdb.com/4536.htm", "chain": "Six Flags"},
    "Six Flags Darien Lake": {"url": "https://rcdb.com/4581.htm", "chain": "Six Flags"},
    "Six Flags Great Escape": {"url": "https://rcdb.com/4596.htm", "chain": "Six Flags"},
    "La Ronde": {"url": "https://rcdb.com/4567.htm", "chain": "Six Flags"},
    "Frontier City": {"url": "https://rcdb.com/4559.htm", "chain": "Six Flags"},
    "Six Flags Mexico": {"url": "https://rcdb.com/4629.htm", "chain": "Six Flags"},
    "Six Flags Qiddiya City": {"url": "https://rcdb.com/21275.htm", "chain": "Six Flags"},

    # Merlin Parks
    "Legoland California": {"url": "https://rcdb.com/4733.htm", "chain": "Legoland"},
    "Legoland Florida": {"url": "https://rcdb.com/5589.htm", "chain": "Legoland"},
    "Legoland New York": {"url": "https://rcdb.com/14429.htm", "chain": "Legoland"},
    "Legoland Billund": {"url": "https://rcdb.com/4903.htm", "chain": "Legoland"},
    "Legoland Deutschland" : {"url": "https://rcdb.com/5059.htm", "chain": "Legoland"},
    "Legoland Dubai": {"url": "https://rcdb.com/13462.htm", "chain": "Legoland"},
    "Legoland Japan": {"url": "https://rcdb.com/13644.htm", "chain": "Legoland"},
    "Legoland Malaysia": {"url": "https://rcdb.com/9575.htm", "chain": "Legoland"},
    "Legoland Korea": {"url": "https://rcdb.com/12557.htm", "chain": "Legoland"},
    "Legoland Shanghai": {"url": "https://rcdb.com/19273.htm", "chain": "Legoland"},
    "Legoland Windsor": {"url": "https://rcdb.com/4813.htm", "chain": "Legoland"},
    "Alton Towers": {"url": "https://rcdb.com/4796.htm", "chain": "Merlin"},
    "Chessington World of Adventures": {"url": "https://rcdb.com/4798.htm", "chain": "Merlin"},
    "Heide Park Resort": {"url": "https://rcdb.com/4874.htm", "chain": "Merlin"},
    "Gardaland": {"url": "https://rcdb.com/4866.htm", "chain": "Merlin"},
    "Thorpe Park": {"url": "https://rcdb.com/4814.htm", "chain": "Merlin"},

    # Disney
    "Magic Kingdom": {"url": "https://rcdb.com/4597.htm", "chain": "Disney"},
    "EPCOT": {"url": "https://rcdb.com/15503.htm", "chain": "Disney"},
    "Hollywood Studios": {"url": "https://rcdb.com/4735.htm", "chain": "Disney"},
    "Animal Kingdom": {"url": "https://rcdb.com/5109.htm", "chain": "Disney"},
    "Disneyland": {"url": "https://rcdb.com/4571.htm", "chain": "Disney"},
    "Disney California Adventure": {"url": "https://rcdb.com/4783.htm", "chain": "Disney"},
    "Disneyland Paris": {"url": "https://rcdb.com/4864.htm", "chain": "Disney"},
    "Disneyland Paris - Walt Disney Studios Park": {"url": "https://rcdb.com/5054.htm", "chain": "Disney"},
    "Tokyo Disneyland": {"url": "https://rcdb.com/4959.htm", "chain": "Disney"},
    "Tokyo DisneySea": {"url": "https://rcdb.com/5073.htm", "chain": "Disney"},
    "Shanghai Disneyland": {"url": "https://rcdb.com/6556.htm", "chain": "Disney"},
    "Hong Kong Disneyland": {"url": "https://rcdb.com/5279.htm", "chain": "Disney"},

    # Universal 
    "Universal Studios Florida": {"url": "https://rcdb.com/4736.htm", "chain": "Universal"},
    "Islands of Adventure": {"url": "https://rcdb.com/4734.htm", "chain": "Universal"},
    "Epic Universe": {"url": "https://rcdb.com/17569.htm", "chain": "Universal"},
    "Universal Studios Hollywood": {"url": "https://rcdb.com/5265.htm", "chain": "Universal"},
    "Universal Studios Singapore": {"url": "https://rcdb.com/4859.htm", "chain": "Universal"},
    "Universal Studios Japan": {"url": "https://rcdb.com/5492.htm", "chain": "Universal"},
    "Universal Studios Beijing": {"url": "https://rcdb.com/17287.htm", "chain": "Universal"},

    # United Parks
    "Busch Gardens Tampa": {"url": "https://rcdb.com/4543.htm", "chain": "United Parks"},
    "Busch Gardens Williamsburg": {"url": "https://rcdb.com/4548.htm", "chain": "United Parks"},
    "SeaWorld Orlando": {"url": "https://rcdb.com/4746.htm", "chain": "United Parks"},
    "SeaWorld San Antonio": {"url": "https://rcdb.com/4601.htm", "chain": "United Parks"},
    "SeaWorld San Diego": {"url": "https://rcdb.com/5320.htm", "chain": "United Parks"},

    # Herschend Family Entertainment
    "Adventureland": {"url": "https://rcdb.com/4576.htm", "chain": "Herschend"},
    "Dollywood": {"url": "https://rcdb.com/4593.htm", "chain": "Herschend"},
    "Kennywood": {"url": "https://rcdb.com/4553.htm", "chain": "Herschend"},
    "Kentucky Kingdom": {"url": "https://rcdb.com/4563.htm", "chain": "Herschend"},
    "Lake Compounce": {"url": "https://rcdb.com/4683.htm", "chain": "Herschend"},
    "Silver Dollar City": {"url": "https://rcdb.com/4579.htm", "chain": "Herschend"},

    # Parques Reunidos
    "Bobbejaanland": {"url": "https://rcdb.com/4846.htm", "chain": "Parques Reunidos"},
    "MoviePark Germany": {"url": "https://rcdb.com/4869.htm", "chain": "Parques Reunidos"},
    "Mirabilandia": {"url": "https://rcdb.com/4793.htm", "chain": "Parques Reunidos"},
    "Parque de Atracciones": {"url": "https://rcdb.com/4928.htm", "chain": "Parques Reunidos"},
    "Parque Warner Madrid": {"url": "https://rcdb.com/5028.htm", "chain": "Parques Reunidos"},
    "TusenFryd": {"url": "https://rcdb.com/4901.htm", "chain": "Parques Reunidos"},

    # Walibi Group
    "Walibi Belgium": {"url": "https://rcdb.com/4847.htm", "chain": "Walibi"},
    "Walibi Holland": {"url": "https://rcdb.com/4794.htm", "chain": "Walibi"},
    "Walibi Rhône-Alpes": {"url": "https://rcdb.com/4857.htm", "chain": "Walibi"},

    # Other 
    "Efteling": {"url": "https://rcdb.com/4839.htm", "chain": "Other"},
    "Nagashima Spa Land": {"url":"https://rcdb.com/4958.htm", "chain": "Other"},
    "Europa Park": {"url": "https://rcdb.com/4870.htm", "chain": "Other"},
    "Port Adventura": {"url": "https://rcdb.com/4792.htm", "chain": "Other"},
    "Ferrari Land": {"url": "https://rcdb.com/12016.htm", "chain": "Other"},
    "Phantasialand": {"url": "https://rcdb.com/4872.htm", "chain": "Other"},
    "Nickelodeon Universe": {"url": "https://rcdb.com/15593.htm", "chain": "Other"},
    "Fuji-Q Highland": {"url": "https://rcdb.com/4961.htm", "chain": "Other"},
    "Energylandia": {"url": "https://rcdb.com/12068.htm", "chain": "Other"},
    "Liseberg":{ "url": "https://rcdb.com/4909.htm", "chain": "Other"},
    "Hersheypark": {"url": "https://rcdb.com/4545.htm", "chain": "Other"},
    "Holiday World": {"url": "https://rcdb.com/4554.htm", "chain": "Other"},
    "Knoebels": {"url": "https://rcdb.com/4557.htm", "chain": "Other"},
    "Pleasure Beach Blackpool": {"url": "https://rcdb.com/4795.htm", "chain": "Other"},
    "Warner Bros. World Abu Dhabi": {"url": "https://rcdb.com/13899.htm", "chain": "Other"},
    "Linnanmäki": {"url": "https://rcdb.com/4917.htm", "chain": "Other"},
    "Ferrari World Abu Dhabi": {"url": "https://rcdb.com/6302.htm", "chain": "Other"},
    "Gröna Lund": {"url": "https://rcdb.com/4910.htm", "chain": "Other"},
    "Hansa Park": {"url": "https://rcdb.com/4873.htm", "chain": "Other"},
}


def get_soup(url: str) -> Optional[BeautifulSoup]:
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"Fetch failed: {url} ({e})")
        return None


def get_coaster_urls(park_url: str) -> List[str]:
    soup = get_soup(park_url)
    if not soup:
        return []

    coaster_urls = []

    for table in soup.find_all("table"):
        headers = table.find_all("th")
        if not headers:
            continue

        header_text = "".join(h.get_text(strip=True) for h in headers)

        if "Name" not in header_text or "Opened" not in header_text:
            continue

        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) < 2:
                continue

            link = cells[1].find("a", href=True)
            if link and re.fullmatch(r"/\d+\.htm", link["href"]):
                coaster_urls.append(BASE_URL + link["href"])

        break

    return list(set(coaster_urls))


def scrape_coaster_data(url: str, park: str, chain: str) -> Optional[Dict]:
    soup = get_soup(url)
    if not soup:
        return None

    name = soup.find("h1").get_text(strip=True)
    text = soup.get_text(" ", strip=True)

    def grab(pattern):
        m = re.search(pattern, text)
        return m.group(1) if m else None

    return {
        "Chain": chain,
        "Park": park,
        "Name": name,
        "Height": grab(r"Height[:\s]*(\d+\.?\d*\s*(?:ft|m))"),
        "Speed": grab(r"Speed[:\s]*(\d+\.?\d*\s*(?:mph|km/h))"),
        "Length": grab(r"Length[:\s]*(\d+\.?\d*\s*(?:ft|m))"),
        "Inversions": grab(r"Inversions?[:\s]*(\d+)"),
        "URL": url,
    }


def scrape_all_parks(delay: float = REQUEST_DELAY) -> pd.DataFrame:
    rows = []

    for i, (park, info) in enumerate(PARKS.items(), 1):
        print(f"\n[{i}/{len(PARKS)}] {park}")

        urls = get_coaster_urls(info["url"])
        print(f"  Found {len(urls)} coasters")

        for j, url in enumerate(urls, 1):
            data = scrape_coaster_data(url, park, info["chain"])

            if data:
                print(f"    [{j}] {data['Name']}")
                rows.append(data)

            time.sleep(delay)

    return pd.DataFrame(rows)

