# The purpose of this program is to be able to scrape top posts in different subreddits and upload the data into a csv file type.
# subreddits.py is the config file with all subreddits to scrape.

"""
Client ID, client secret, user agent can be found in reddit profile. Under preferances -> apps -> create app.
For re-direct url, input: http://localhost:8080. 
"""

import praw
import pandas as pd
from subreddits import subreddits_to_scrape

reddit_read_only = praw.Reddit(client_id = "", # input your client ID between quotes
                               client_secret = "", # input your client secret between quotes
                               user_agent = "") # input your user agent between quotes

# Dictionary to hold scraped data
posts_dict = {"Subreddit": [], "Title": [], "Post Text": [],
              "ID": [], "Score": [], "Total Comments": [], "Post URL": []}

# Loop through each subreddit
for subreddit_name in subreddits_to_scrape:
    try:
        subreddit = reddit_read_only.subreddit(subreddit_name)

        print(f"Display Name: {subreddit.display_name}")  # displays name of subreddit
        print(f"Title: {subreddit.title}")  # displays title of subreddit
        print(f"Description: {subreddit.description}")  # displays description of the subreddit

        # Scraping the new posts
        posts = subreddit.new(limit=10)  # adjust limit as needed

        # Populate dictionary with data
        for post in posts:
            posts_dict["Subreddit"].append(subreddit_name)
            posts_dict["Title"].append(post.title) # Title of each post
            posts_dict["Post Text"].append(post.selftext) # Text inside a post
            posts_dict["ID"].append(post.id) # Unique ID of each post
            posts_dict["Score"].append(post.score) # The score of a post
            posts_dict["Total Comments"].append(post.num_comments) # Total number of comments inside the post
            posts_dict["Post URL"].append(post.url) # URL of each post

    except praw.exceptions.PRAWException as e:
        print(f"An error occurred while processing subreddit {subreddit_name}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing subreddit {subreddit_name}: {e}")

# Create a DataFrame from the dictionary
top_posts = pd.DataFrame(posts_dict)

# Display the DataFrame
print(top_posts)

# Export data to a CSV file
top_posts.to_csv("New_Posts.csv", index=True)

"""
subreddits_to_scrape = [
    "Scams",
    "fraud",
    "amazon",
    "OnlineFraud"
    # Add more subreddits as needed
]
This is the config file (called subreddits.py that is imported into this file. Can keep adding as many subreddits as needed.)
"""
