
URL = "https://api.github.com/repos/CSSEGISandData/COVID-19/contents/csse_covid_19_data/csse_covid_19_daily_reports"

url_list = []
response = requests.get(url)

print (response)
