import instaloader
bot = instaloader.Instaloader()
Username = input("Enter username: ")
bot.load_session_from_file(Username)
profile = instaloader.Profile.from_username(bot.context, Username)

likes = set()
print("Fetching likes on profile".format(profile.username))
for post in profile.get_posts():
    print(post)
    likes = likes | set(post.get_likes())
print("Fetch followers".format(profile.username))
followers = set(profile.get_followers())
ghosts = followers-likes
print("storing ghosts")
with open("inactiveusers.txt", 'w') as f:
    for ghost in ghosts:
        print(ghost.username, file=f)

famous = input("Enter famous username: ")
profile2 = instaloader.Profile.from_username(bot.context, famous)
print(profile2.is_verified)
print(profile2.followers)
print(profile2.biography)



