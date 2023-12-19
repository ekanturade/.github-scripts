import requests

url = "https://cdn.digialm.com/EForms/configuredHtml/1258/83923/Index.html"

response = requests.get(url)
with open("source_code.html", "w", encoding="utf-8") as file:
    file.write(response.text)
