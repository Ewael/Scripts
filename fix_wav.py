# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import glob

dir_path = r'C:\Users\Ewael\Music\**\*.*'

def get_wav(dir_path):
    tracks_wav = []
    for track in glob.glob(dir_path, recursive=True):
        if track[-4:] == '.wav':
            tracks_wav.append(track)
    return tracks_wav
            
def get_unsupported(tracks_wav):
    unsupported_tracks = []
    for track in tracks_wav:
        with open(track, 'rb') as f:
            content = f.read(22)
            if content[-2:] == b'\xfe\xff':
                unsupported_tracks.append(track)
    return unsupported_tracks
                
def fix_unspported(unsupported_tracks):
    for track in unsupported_tracks:
        with open(track, 'rb') as f:
            content = list(f.read())
        content[20] = 0x01
        content[21] = 0x00
        with open(track, 'wb') as f:
            f.write(bytes(content))

wav = get_wav(dir_path)
uns = get_unsupported(wav)
#fix_unspported(uns)