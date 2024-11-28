from bs4 import BeautifulSoup
import json

# Open and read the HTML file
with open('list.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Create an empty list to store the extracted links and descriptions
link_description_pairs = []

# Find all divs in the HTML
for div in soup.find_all('div'):
    # Find all <a> tags with href attribute containing '/companies/'
    a_tags = div.find_all('a', href=lambda href: href and '/companies/' in href)
    # Find all <span> tags with a class containing 'Description'
    span_tags = div.find_all('span', class_=lambda cls: cls and 'Description' in cls)
    
    # If both <a> and <span> are found, extract the data
    for a_tag, span_tag in zip(a_tags, span_tags):
        link = a_tag['href']
        description = span_tag.text.strip()
        # Add the pair to the list
        link_description_pairs.append({'link': link, 'description': description})

# Write the list to a JSON file
with open('formatted.json', 'w', encoding='utf-8') as json_file:
    json.dump(link_description_pairs, json_file, indent=4, ensure_ascii=False)

print("Extraction complete. Data saved to formatted.json.")
