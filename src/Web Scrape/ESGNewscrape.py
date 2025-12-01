import json
import os
from datetime import datetime

# ---------------------------------------------------------
# Master list of ESG websites (edit/extend this list anytime)
# ---------------------------------------------------------
SOURCES = [
    {
        "name": "KnowESG",
        "url": "https://www.knowesg.com",
        "region": "Global",
        "category": "ESG / Sustainability",
        "scrapability": "Easy",
        "notes": "Corporate ESG news, ratings insight, structured categories."
    },
    {
        "name": "ESG News",
        "url": "https://esgnews.com",
        "region": "Global",
        "category": "ESG / Climate / Sustainable Investing",
        "scrapability": "Easy",
        "notes": "High-frequency updates, good for time-series ESG monitoring."
    },
    {
        "name": "ESG Chronicle",
        "url": "https://esgchronicle.com",
        "region": "Global + Asia",
        "category": "ESG / Climate Policy / Energy Transition",
        "scrapability": "Easy",
        "notes": "Topic-wise sections – good for topic-level scrapers."
    },
    {
        "name": "ESG Times",
        "url": "https://www.esgtimes.in",
        "region": "India + Global",
        "category": "ESG / Corporate India / Sustainability",
        "scrapability": "Easy",
        "notes": "Good for emerging market ESG and India-specific tracking."
    },
    {
        "name": "Eco-Business",
        "url": "https://www.eco-business.com",
        "region": "Asia-Pacific",
        "category": "Sustainability / Climate / Policy",
        "scrapability": "Medium",
        "notes": "Deep regional sustainability coverage."
    },
    {
        "name": "Mongabay",
        "url": "https://www.mongabay.com",
        "region": "Global",
        "category": "Environment / Biodiversity / Conservation",
        "scrapability": "Easy",
        "notes": "Environmental news for ecological ESG context."
    },
    {
        "name": "Grist",
        "url": "https://grist.org",
        "region": "Global",
        "category": "Climate Justice / Environment",
        "scrapability": "Easy",
        "notes": "Long-form climate/environment journalism."
    },
    {
        "name": "TreeHugger",
        "url": "https://www.treehugger.com",
        "region": "Global",
        "category": "Sustainability / Green Living",
        "scrapability": "Easy",
        "notes": "Consumer sustainability & eco-lifestyle coverage."
    },
    {
        "name": "ESG News India",
        "url": "https://www.esgnewsindia.com",
        "region": "India",
        "category": "India ESG / Corporate Sustainability",
        "scrapability": "Easy",
        "notes": "India-focused ESG and CSR developments."
    },
]

# ---------------------------------------------------------
# Function: Load existing file or create a new one
# ---------------------------------------------------------
def load_existing_sources(filename="esg_sources.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {"updated_at": None, "sources": []}


# ---------------------------------------------------------
# Function: Update existing list with new sources
# ---------------------------------------------------------
def update_sources(existing, new_list):
    existing_map = {s["name"]: s for s in existing["sources"]}

    for src in new_list:
        existing_map[src["name"]] = src  # overwrite or add

    updated_list = list(existing_map.values())
    return updated_list


# ---------------------------------------------------------
# Main runner
# ---------------------------------------------------------
def main():
    filename = "esg_sources.json"

    # Load existing data
    data = load_existing_sources(filename)

    # Update entries
    updated = update_sources(data, SOURCES)

    # Save back to JSON
    final = {
        "updated_at": datetime.utcnow().isoformat() + "Z",
        "sources": updated
    }

    with open(filename, "w") as f:
        json.dump(final, f, indent=4)

    print(f"\n✔ ESG Source List Updated ({len(updated)} sources)")
    print(f"✔ File saved: {filename}\n")

    # Print summary
    for s in updated:
        print(f"- {s['name']}  →  {s['url']}  ({s['region']})")

if __name__ == "__main__":
    main()
