import requests
import plotly.express as px
import webbrowser
from datetime import datetime

# Your GitHub Personal Access Token
TOKEN = 'your_personal_access_token'  # Replace with your actual token

# List of countries from different continents
countries = [
    "USA", "Canada", "Mexico",  # North America
    "Brazil", "Argentina", "Chile",  # South America
    "Germany", "UK", "France", "Spain", "Italy",  # Europe
    "India", "China", "Japan", "South Korea", "Indonesia",  # Asia
    "Ghana", "Nigeria", "Kenya", "South Africa", "Egypt",  # Africa
    "Australia", "New Zealand"  # Australia
]
org_counts = []

# Make API calls for each country and count organizations
for country in countries:
    url = f"https://api.github.com/search/users?q=type:org+location:{country}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}"  # Add your token here
    }
    r = requests.get(url, headers=headers)
    print(f"\nStatus code for {country}: {r.status_code}")

    # Log the response for debugging
    if r.status_code == 200:
        response_dict = r.json()
        org_count = response_dict.get('total_count', 0)
        org_counts.append(org_count)
        print(f"Organizations found in {country}: {org_count}")
    else:
        org_counts.append(0)  # Append 0 if the request failed
        print(f"Failed to retrieve data for {country}. Response: {r.text}")

# Calculate the average number of organizations
average_org_count = sum(org_counts) / len(org_counts) if org_counts else 0
print(f"\nAverage number of GitHub organizations across the countries: {average_org_count:.2f}")

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")
# Make visualization with the current date in the title
title = f"Number of GitHub Organizations by Country @ {current_date}"
labels = {'x': 'Country', 'y': 'Number of Organizations'}
fig = px.bar(x=countries, y=org_counts, title=title, labels=labels)

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Save as an HTML file
html_file_path = 'where_to_save_it_locally'
fig.write_html(html_file_path)

# Open the file in your browser
webbrowser.open(html_file_path)
