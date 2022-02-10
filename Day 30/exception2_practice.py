facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 21, "Comments": 2, "Shares": 1},
    {"Likes": 21, "Comments": 8, "Shares": 3},
    {"Shares": 2, "Comments": 4},
    {"Shares": 21, "Comments": 1},
    {"Likes": 19, "Comments": 3},
]

total_like = 0

for post in facebook_posts:
        total_like = total_like + post["Likes"]


print(total_like)

























# facebook_posts = [
#     {"Likes": 21, "Comments": 2},
#     {"Likes": 21, "Comments": 2, "Shares": 1},
#     {"Likes": 21, "Comments": 8, "Shares": 3},
#     {"Shares": 2, "Comments": 4},
#     {"Shares": 21, "Comments": 1},
#     {"Likes": 19, "Comments": 3},
# ]

# total_like = 0

# for post in facebook_posts:
#     try:
#         total_like = total_like + post["Likes"]
#     except KeyError:
#         pass

# print(total_like)