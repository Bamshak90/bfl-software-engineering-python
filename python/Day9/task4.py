# using the playlsit blow to format the list
#
# 1. change song b to song D 
# 2. Add song e to the end of the list 
# 3. Add intro to the start of the list


playlist = ["song A", "song B", "song C"]

playlist[1] = "song D"
print(playlist)
playlist.append("song E")
print(playlist)
playlist.insert(0,"intro")
print(playlist)

