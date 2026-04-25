from pytube import YouTube

url = 'VIDEO_URL_HERE'
yt = YouTube(url)
yt.streams.get_highest_resolution().download()
print("Download Success!")
