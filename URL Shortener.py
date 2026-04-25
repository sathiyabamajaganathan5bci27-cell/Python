import pyshorteners

url = input("Enter URL: ")
s = pyshorteners.Shortener()
print("Short URL:", s.tinyurl.short(url))
