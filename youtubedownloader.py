import pytube  # this is where i imported the pytube module which is necessary for this script

print(
    "Enter the YouTube video URL")  # This is where we tell the user to input the url in which then pytube grabs the download
a = input()

b = pytube.YouTube(a)  # This is where pytube comes in and pulls info from the video
videos = b.get_videos()

s = 1
for v in videos:
    print(f"{str(s)}. {str(v)}")  # Here is where pytube shows the user what it can download and what file format
    s += 1

print(
    "Type the number of which quality/format you would like: ")  # this is where the user inputs what kind of quality and file format he wants to download
c = int(input())
d = videos[c - 1]

print("Enter the video file path: ")  # This is where the user inputs where they want to save the video
path = input()
d.download(path)  # the download process is initiated

print("The video",
      b.filename + " has been downloaded")  # If the download has successfully finished it will display this
