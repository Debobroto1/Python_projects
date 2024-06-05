from pytube import YouTube
from tqdm import tqdm
import requests


def Download(link):
    youtubeObject = YouTube(link)
    stream = youtubeObject.streams.get_highest_resolution()

    try:
        response = requests.head(stream.url, allow_redirects=True)
        file_size = int(response.headers.get('content-length', 0))

        with requests.get(stream.url, stream=True) as r, open(stream.default_filename, 'wb') as f, tqdm(
                total=file_size, unit='B', unit_scale=True, desc=stream.default_filename, ncols=100) as bar:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))

    except Exception as e:
        print(f"An error has occurred: {e}")
    else:
        print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
