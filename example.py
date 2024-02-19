from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=QegcGsE9tYE')
print(yt)

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

