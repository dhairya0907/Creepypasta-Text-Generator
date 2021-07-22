import praw
import pandas as pd
import datetime as dt
import os
import time
import requests
import smtplib
import ssl
import pytz
from os import path
from tqdm import tqdm
from datetime import date
from psaw import PushshiftAPI
from datetime import datetime
from firebase_admin import credentials, initialize_app, storage

IST = pytz.timezone('') # Enter your timezone.
start_time = str(dt.datetime.now(IST).strftime("%H:%M:%S"))
start_dt = dt.datetime.strptime(start_time, '%H:%M:%S')

# Enter your Reddit client_id and client_secret and user_agent.

r = praw.Reddit(client_id='',
                client_secret='',
                user_agent='')
api = PushshiftAPI(r)

 # Enter path to Credentials json file and storageBucket link.

cred = credentials.Certificate('')
initialize_app(cred, {'storageBucket': ''})

limit = 100 # How much post you want to fetch at once
loop = 10000 # How many times you want to fetch
file_size = 0.0 # Current size of file
file_name = 1 # File name sub number
max_file_size = 90.00 # Max file size before you want to divide file and upload it to firebase
subreddit = "" # Enter name of subreddit you want to scrap
username = '' # Enter username of pythonanywhere account
token = '' # Enter token form pythonanywhere account
console_id = 0
console_frame_url = ''
port = 465  # For SSL
smtp_server = 'smtp.gmail.com'
sender_email = ''  # Enter your email address
receiver_email = ''  # Enter receiver email address
password = '' # Enter your email address password
context = ssl.create_default_context()
posts = []
today = date.today()
year = today.year
month = today.month
day = today.day

# For coustom start date

# year = 2017
# month = 3
# day = 28

response = requests.get('https://www.pythonanywhere.com/api/v0/user/{username}/consoles/'.format(username=username),headers={'Authorization': 'Token {token}'.format(token=token)})
if response.status_code == 200:
    console_id = response.json()[0]['id']
    console_frame_url = str(response.json()[0]['console_frame_url'])



message = """\
   Reddit Scrapper
Subject: Your Task Details

Your Task is started.\n\nStrating Date : """+str(today)+"""\n\nLoop range : """+str(loop)+"""\n\nLimit : """+str(limit)+"""\n\nStarting Time : """+start_time+"""\n\nCheck Your Live Progess Here : https://www.pythonanywhere.com/""" + console_frame_url + """\n\nTask is in Progess..."""
with smtplib.SMTP_SSL(smtp_server, port,context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,message)



for i in tqdm(range(loop)):

    if year != 2011 or month != 8 or day != 3:
        if i % 35 == 0 and i != 0:
            print("\n\n\n1  Minutes Wait Time Starts. \n\n\n")
            for k in tqdm(range(59)):
                time.sleep(1)
            print("\n\n\n1  Minutes Wait Time Ends. \n\n\n")

        if path.exists(subreddit+'_dataset_CSV.csv'):
            file_stats = os.stat(subreddit+'_dataset_CSV.csv')
            file_size = '{:.2f}'.format(file_stats.st_size / (1024 * 1024))

        if float(file_size) < max_file_size:

            posts = []
            dates = []

            start_epoch = int(dt.datetime(year, month, day).timestamp())
            post = list(api.search_submissions(before=start_epoch,
                        subreddit = subreddit, limit=limit))

            for id in range(len(post)):
                parsed_date = datetime.utcfromtimestamp(post[id].created_utc)
                year = parsed_date.year
                month = parsed_date.month
                day = parsed_date.day
                posts.append([
                    post[id].title,
                    post[id].score,
                    post[id].id,
                    post[id].subreddit,
                    post[id].url,
                    post[id].num_comments,
                    post[id].selftext,
                    parsed_date.date().strftime('%d-%m-%y'),
                    ])
                dates.append(parsed_date.date().strftime('%d-%m-%y'))

            posts = pd.DataFrame(posts, columns=[
                'title',
                'score',
                'id',
                'subreddit',
                'url',
                'num_comments',
                'body',
                'created',
                ])
            dates = pd.DataFrame(dates, columns=['Date'])

            if path.exists(subreddit+'_dataset_CSV.csv'):
                posts.to_csv(subreddit+'_dataset_CSV.csv', index=False, mode='a',
                             header=False)
            else:
                posts.to_csv(subreddit+'_dataset_CSV.csv', index=False)

            if path.exists(subreddit+'_dates_done_CSV.csv'):
                dates.to_csv(subreddit+'_dates_done_CSV.csv', index=False, mode='a',
                             header=False)
            else:
                dates.to_csv(subreddit+'_dates_done_CSV.csv', index=False)



            file_stats = os.stat(subreddit+'_dataset_CSV.csv')
            file_size = '{:.2f}'.format(file_stats.st_size / (1024 * 1024))

        else:
            os.rename(subreddit+'_dataset_CSV.csv', subreddit+'_dataset_Raw_Csv_' + str(file_name) + '.csv')
            # Put your local file path

            fileName = subreddit+'_dataset_Raw_Csv_' + str(file_name) + '.csv'
            bucket = storage.bucket()
            blob = bucket.blob(fileName)
            blob.upload_from_filename(fileName)

            # Opt : if you want to make public access from the URL

            blob.make_public()

            os.remove(subreddit+'_dataset_Raw_Csv_' + str(file_name) + '.csv')
            file_name = file_name + 1
            file_size = 0
    else:
        break

if path.exists(subreddit+'_dates_done_CSV.csv'):
    fileName = subreddit+'_dates_done_CSV.csv'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL

    blob.make_public()

    os.remove(subreddit+'_dates_done_CSV.csv')

if path.exists(subreddit+'_dataset_CSV.csv'):
    os.rename(subreddit+'_dataset_CSV.csv', subreddit+'_dataset_Raw_Csv_' + str(file_name) + '.csv')
    # Put your local file path

    fileName =subreddit+'_dataset_Raw_Csv_' + str(file_name) + '.csv'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL

    blob.make_public()

    os.remove(subreddit+'_dataset_Raw_Csv_' + str(file_name) + '.csv')
    file_name = file_name + 1
    file_size = 0

end_time = str(dt.datetime.now(IST).strftime("%H:%M:%S"))
end_dt = dt.datetime.strptime(end_time, '%H:%M:%S')
total_time = (end_dt - start_dt)

message = """\
      Reddit Scrapper
Subject: Your Task Is Finished

Check Firebase, for Raw Files.\n\nEnd Time : """+end_time+"""\n\nTotal Time : """+str(total_time)+"""\n\nCheck Your Finished Progess Here : https://www.pythonanywhere.com/""" + console_frame_url + """\n\nTask is Completed."""
with smtplib.SMTP_SSL(smtp_server, port,context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email,message)

