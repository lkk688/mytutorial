from pytube import YouTube #https://github.com/nficano/pytube
yt = YouTube('https://www.youtube.com/watch?v=fSnPFiFb-1c')
#yt.streams
print(yt.streams.filter(subtype='mp4', progressive=True))
yt.streams.get_by_itag(22).download()