import instaloader

bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, 'username')
print(f"Followers: {profile.followers}")
