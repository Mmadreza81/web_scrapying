import requests
# Define the initial URL and headers
url = 'https://api.divar.ir/v8/web-search/1/apartment-sell'
headers = {"Content-Type": "application/json"}

# Define the JSON data for the initial request
json_data = {
  "page": 1,
  "json_schema": {
    "category": {
      "value": "apartment-sell"
    },
    "sort": {
      "value": "sort_date"
    },
    "cities": [
      "1"
    ]
  }
}

try:
    list_of_tokens = []
    last_post_dates = [1704718426626198,1704718327420355,1704718263329981,1704718144787963,1704718085717545,
                       1704718008774087,1704717929534357,1704717841567013,1704717750090618,1704717637259022,
                       1704717522088127,1704717434193297,1704717347738207,1704717234856119,1704717152651155,
                       1704717045388787,1704716924885061,1704716804178351,1704716716520823,1704716628154314,
                       1704716560278522,1704716492123458,1704716383704777,1704716296280786,1704716226189604]

    # Loop through multiple last post dates
    for date in last_post_dates:
        json_data["last-post-date"] = date

        # Loop through multiple pages of the API response
        for page in range(1, 31):  # Assuming you want to collect tokens from 2 pages
            json_data["page"] = page  # Update the page number in the JSON data
            res = requests.post(url, json=json_data, headers=headers)
            data = res.json()

            for widget in data.get('web_widgets', {}).get("post_list", []):
                token = widget.get("data", {}).get("token")

                if token:
                    list_of_tokens.append(token)

except requests.exceptions.RequestException as e:
    print("Error:", e)

list_of_tokens = set(list_of_tokens)
list_of_tokens = list(list_of_tokens)
print(len(list_of_tokens))

txt_file = open('tokens.txt', 'w', encoding='utf8')
txt_file.write(",".join(list_of_tokens))
txt_file.close()
