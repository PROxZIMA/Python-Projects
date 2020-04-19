from urllib.parse import urlencode
from urllib.request import urlopen
from re import findall

search_code = urlencode({'sql la la' : input('Search for the song: ')})
print(search_code)
search_url = urlopen('http://www.youtube.com/results?search_query' + search_code)
video_code = findall(r'href=\"\/watch\?v=(.{11})', search_url.read().decode())
for i in range(0, len(video_code), 2):
    print(f'[{i//2+1}] http://www.youtube.com/watch?v={video_code[i]}')