import yt_dlp

def find_vid(query: str, data: int) -> str | None:
    with yt_dlp.YoutubeDL({'quiet': True,
                          'no_warnings': True}) as ydl:
        find = ydl.extract_info(f"ytsearch1:{query}", download=False)
        if data == 0:
            return find["entries"][0]["webpage_url"]
        elif data == 1:
            return find["entries"][0]["title"]
        else:
            raise ValueError()
