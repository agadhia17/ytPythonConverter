import sys
from pytube import YouTube 
import os

link = YouTube(input("Enter Youtube link:"))

def mp3convert(link):
    yd = link.streams.filter(only_audio=True).get_audio_only()
    destination="/Users/AbhishekGadhia/Desktop"

    #stream = yd.streams.get_by_itag(22)
    out_file=yd.download(output_path=destination)

    base, ext= os.path.splitext(out_file)
    new_file=base + '.mp3'
    os.rename(out_file, new_file)

    iso_file = new_file
    output_file = '"/Users/AbhishekGadhia/Downloads/output1.mp3"'
    command1 = "ls -l %s %s" % (iso_file, output_file)
    command2 = "ffmpeg -i %s %s" % (iso_file, output_file)
    os.system(command2)

    print(link.title + " has been successfully downloaded")
    return(link.title +"has successfully been downloaded")


def mp4convert(link):
    destination="/Users/AbhishekGadhia/Desktop"
    video=link.streams.filter(progressive=True)

    vid=list(enumerate(video))
    for i in vid:
        print(i)

    strm=int(input("choose resolution index: "))
    video[strm].download(output_path=destination)

    print(link.title + " has been successfully downloaded")
    return(link.title + " has been successfully downloaded")


choice= int(input("Would you like to download the audio(1) or video(2)?: "))
if choice==1:
    mp3convert(link)
elif choice==2:
    mp4convert(link)