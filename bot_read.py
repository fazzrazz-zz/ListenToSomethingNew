#!/usr/bin/python
import praw
import webbrowser
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("listentothis")

list = []
master = "http://www.youtube.com/watch_videos?video_ids="
for submission in subreddit.top('week', limit= 7):#Change limit to change the
                                                  # amount of videos in playlist
    sub = str(submission.url)
    url = sub[-11:len(sub)]
    master = master + url + ","

webbrowser.open(master)
