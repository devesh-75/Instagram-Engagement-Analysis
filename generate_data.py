import csv
import random

rows = []

for i in range(1, 1001):
    post_id = i
    user_id = random.randint(100, 500)
    followers = random.randint(500, 20000)

    post_type = random.choice(["image", "reel", "video"])

    likes = random.randint(50, followers)
    comments = random.randint(5, likes // 10)
    shares = random.randint(1, likes // 5)
    saves = random.randint(1, likes // 3)
    views = random.randint(likes, likes * 10)

    watch_time = random.randint(5, 60)
    hashtags_count = random.randint(1, 10)
    caption_length = random.randint(20, 200)
    posted_hour = random.randint(0, 23)

    engagement_score = (likes + comments + shares) / followers
    engagement_label = 1 if engagement_score > 0.1 else 0

    rows.append([
        post_id, user_id, followers, post_type,
        likes, comments, shares, saves, views,
        watch_time, hashtags_count, caption_length,
        posted_hour, engagement_label
    ])

with open("data/dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "post_id","user_id","followers","post_type",
        "likes","comments","shares","saves","views",
        "watch_time","hashtags_count","caption_length",
        "posted_hour","engagement_label"
    ])
    writer.writerows(rows)

print("Dataset Generated Successfully!")