# Script to print Dates Scrapped for posts.

import pandas as pd

date_file_name = ""

dates_done = pd.read_csv(date_file_name)
dates_done.drop_duplicates().to_csv(date_file_name, index=False)

dates_done = pd.read_csv(date_file_name)


print(dates_done)

print(pd.to_datetime(dates_done.iloc[0][0]))
