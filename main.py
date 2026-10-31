print("SWYNEX PYTHON AUTOMATION TOOL")
print("-----------------------------")

files = ["photo.jpg", "assignment.pdf", "notes.txt", "song.mp3", "video.mp4"]

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file, "-> Images")
    elif file.endswith(".pdf") or file.endswith(".txt"):
        print(file, "-> Documents")
    elif file.endswith(".mp3"):
        print(file, "-> Audio")
    elif file.endswith(".mp4"):
        print(file, "-> Videos")

print("-----------------------------")
print("Automation completed successfully!")