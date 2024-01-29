import pyperclip
import os

files = []

def decode(fn):
    file = files[int(fn)]
    print("Decoding...")
    f = open(file, "r")
    encoded = "read('song', '"
    for line in f.read().split("\n"):
        encoded += line + "|"
    pyperclip.copy(encoded + "')")

id = 0
print("\n\n\n")
print("Finding osu files- input the id of the map you want to play.")
current_directory = os.getcwd()
for filename in os.listdir(current_directory):
   if filename.endswith(".osu"):
       files.append(filename)
       print(f"{id} :: " + filename)
       id += 1

print("\n\n\n")
decode(input())
print("Copied successfully to clipboard")

# DARKSHEEP    : cmu://765177/27972382/darksheep.ogg
# RUNENGON     : cmu://765177/28109488/runengon.mp3
# CRYSTALLIZED : cmu://765177/28109622/crystallized.ogg