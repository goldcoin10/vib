import yt_dlp

def find_vid(query: str):
    with yt_dlp.YoutubeDL({'quiet': True,
                          'no_warnings': True}) as ydl:
        find = ydl.extract_info(f"ytsearch1:{query}", download=False)
        return_me = [find["entries"][0]["webpage_url"], find["entries"][0]["title"]] 
        return return_me
