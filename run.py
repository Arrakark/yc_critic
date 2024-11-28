import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load sentence-transformers model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Load skill.txt and formatted.json
with open('skill.txt', 'r') as skill_file:
    skills_text = skill_file.read().replace('\n', ', ')

with open('formatted.json', 'r') as json_file:
    formatted_data = json.load(json_file)

# Get the embedding vector for the skills text
skills_embedding = model.encode(skills_text)

# Calculate similarity for each description in formatted.json
for entry in formatted_data:
    entry['link'] = "https://www.ycombinator.com" + entry.get('link', '')
    description = entry.get('description', '')
    description_embedding = model.encode(description)
    similarity = cosine_similarity([skills_embedding], [description_embedding])[0][0]
    entry['similarity'] = float(similarity)

# Sort entries by similarity in descending order
formatted_data.sort(key=lambda x: x['similarity'], reverse=True)

# Save the result to output.json
with open('output.json', 'w') as output_file:
    json.dump(formatted_data, output_file, indent=4)

print("Output saved to output.json")
