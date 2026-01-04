import json
import urllib.parse

# CAVE: json must be generated using Google Takeout (exporting "starred places")
input_filename = 'input.json'
output_filename = 'output_formatted.json'

with open(input_filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

for feature in data['features']:
    props = feature['properties']
    
    # CASE A: Items that have a 'location' object
    if 'location' in props:
        if 'name' in props['location']:
            props['name'] = props['location']['name']
        
        address = props['location'].get('address')
        if address:
            props['address'] = address

    # CASE B: "Ghost" items with no location object (often 0,0 coordinates)
    elif 'google_maps_url' in props:
        url = props['google_maps_url']
        try:
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query)
            if 'q' in params:
                props['name'] = params['q'][0]
            else:
                props['name'] = "Saved Place"
        except:
            props['name'] = "Saved Place"

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Done! Processed {len(data['features'])} items.")