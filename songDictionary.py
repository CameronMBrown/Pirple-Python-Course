#Pirple Assignment 7 - Dictionaries and Sets

# convert the data from assignment 1 to a dictionary and print
# extra credit - write a function that allows the user can guess values and keys

Maria = { "name": "Dear Maria Count Me In", "artist": "All Time Low", "album": "So Wrong It's Right", "genre": "Pop Punk", "label": "Hopeless Records", "year": 2008, "playtime":"3:02", "seconds": 182, "hours": 0.051}

def printSong(song):
  for key in song:
    print(key, ": ", song[key]) 

def guessSong(key, val):
  if key in Maria:
    if Maria[key] == val:
      return True
  return False


printSong(Maria)
print(guessSong("name", "Dear Maria Count Me In"))
print(guessSong("artist", "Blink-182"))