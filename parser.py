from pytube import YouTube
from pytube.exceptions import PytubeError

def create_urls_lst(content: str):
    urls_lst = [url for url in content.split()]
    return urls_lst

def parse_video(url: str) -> dict:
    yt = YouTube(url)
    video_information = {
        "title": yt.title,
        "author": yt.author,
        "views": yt.views,
        "length": yt.length
    }

    return video_information

def create_sorted_videos_information_dict(urls: list[str], sort_by: str) -> dict|str:
    videos_information_lst = []
    for url in urls:
        try:
            video_information = parse_video(url)
        except PytubeError as e:
            print(f"Error parsing video at {url} - {e}")
            continue

        videos_information_lst.append(video_information)

    if len(videos_information_lst) > 0:

        sorted_videos_information_lst = sorted(videos_information_lst,
                                               key=lambda dct: dct[sort_by], reverse=True)

        videos_information_dict = {}
        for video in sorted_videos_information_lst:
            videos_information_dict[len(videos_information_dict) + 1] = video

        return videos_information_dict
    else:
        html = """
        <h1>Invalid Values!</h1>
        <form action="/" method="get">
            <button type="submit">Go back!</button>
        </form>
        """
        return html