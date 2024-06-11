#The purpose of this program is to be able to scrape top posts in different subreddits and upload the data into a csv file type.

'''
Client ID, client secret, user agent can be found in reddit profile. Under preferances -> apps -> create app.
For re-direct url, input: http://localhost:8080. 
'''

import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id = "", # input your client ID between quotes
                               client_secret = "", # input your client secret between quotes
                               user_agent = "") # input your user agent between quotes

subreddit = reddit_read_only.subreddit("Scams")

print("Display Name: ", subreddit.display_name) # displays name of subreddit

print("Title: ", subreddit.title) # displays title of subreddit

print("Description: ", subreddit.description) # displays description of the subreddit

subreddit = reddit_read_only.subreddit("Scams")

for post in subreddit.hot(limit = 10):
    print(post.title)
    print()

# Scraping the top posts of the current month
posts = subreddit.top(time_filter = "month")

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
                }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)
     
    # The score of a post
    posts_dict["Score"].append(post.score)
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)
print(top_posts)

top_posts.to_csv("Top Posts.csv", index=True) # exports data to a CSV file type

