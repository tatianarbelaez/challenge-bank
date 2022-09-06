import requests
import pandas as pd

from pandas_profiling import ProfileReport

for day in range(1, 32):
    if day<10:
        day_string = '0'+str(day)
    else:
        day_string = str(day)

    print('day',day_string)
    result_json = requests.get('https://api.tvmaze.com/schedule/web?date=2020-12-'+day_string).json()
    df = pd.json_normalize(result_json)
    profile = ProfileReport(df, title="Pandas Profiling Report")
    profile.to_file("../profiling/report_december_"+day_string+".html")
