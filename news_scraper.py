import requests
from bs4 import BeautifulSoup

# Step 1: URL of news website
url = "https://www.bbc.com/news"

# Step 2: Send request
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find headlines (h2 tags)
headlines = soup.find_all("h2")

# Step 5: Extract text and save
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, headline in enumerate(headlines):
        text = headline.get_text().strip()
        if text:  # avoid empty lines
            file.write(f"{i+1}. {text}\n")

print("✅ Headlines saved to headlines.txt")