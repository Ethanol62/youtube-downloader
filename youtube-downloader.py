from pytube import YouTube

link = input("Video link: ")
yt = YouTube(link)

print("Video found.")

video = yt.streams.get_highest_resolution()

print("Downloading...")
video.download()
print("Download completed.")

print("")
print("https://github.com/Ethanol62")
print("")

input("Press Enter to exit...")