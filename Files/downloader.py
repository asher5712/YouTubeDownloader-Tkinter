from pytube import YouTube
from pytube.contrib.playlist import Playlist


def single(url, form='mp4', res='720p', separate_audio_video_file=False, path_to_store=None):
    if path_to_store is None:
        path_to_store = 'C:/Users/Lenovo/Downloads/Videos/YouTube/'
    instance = YouTube(url)
    if separate_audio_video_file:
        instance.streams.filter(file_extension=form, res=res, adaptive=True).first().download(path_to_store)
    else:
        instance.streams.filter(file_extension=form, res=res, progressive=True).first().download(path_to_store)
        print(f"Video '{instance.title}' downloaded!")
    return f"Video '{instance.title}' downloaded!"


def playlist(playlist_url, form='mp4', res='720p', separate_audio_video_file=False, path_to_store=None):
    vid_lst = []
    if path_to_store is None:
        path_to_store = 'C:/Users/Lenovo/Downloads/Videos/YouTube/'
    instance = Playlist(playlist_url)
    url_lst = instance.video_urls
    for url in url_lst:
        vid_lst.append(single(url, form, res, separate_audio_video_file, path_to_store))
        print(vid_lst[-1])
    return vid_lst


def download_data(url, url_type, form='mp4', res='720p', separate_audio_video_file=False, path_to_store=None):
    f_lst = []
    validation = (form != 'mp4' or res != '720p' or separate_audio_video_file is not True)
    if url_type.lower() == 'playlist':
        if validation:
            f_lst = playlist(url, form, res, separate_audio_video_file, path_to_store)
        else:
            f_lst = playlist(url, path_to_store=path_to_store)
    elif url_type.lower() == 'single':
        if validation:
            f_lst.append(single(url, form, res, separate_audio_video_file, path_to_store))
        else:
            f_lst.append(single(url, path_to_store=path_to_store))
    return f_lst


def call_downloader():
    while True:
        urltype = input("What type of data you want to enter? [1. Single, 2. Playlist]")
        isValid = (urltype.lower() == 'single' or
                   urltype.lower() == '1' or
                   urltype.lower() == 'playlist' or
                   urltype.lower() == '2')
        if isValid:
            if urltype.lower() == '1':
                urltype = 'single'
            elif urltype.lower() == '2':
                urltype = 'playlist'
            break
        else:
            print("Must be either string ['Single' or 'Playlist'] or number [1,2]")
    url = input("Enter the url here:")
    path = input("Specify complete path for storing video ['D:/Videos' or 'skip']:")
    if path == 'skip':
        path = None
    choice = input("Wanna specify formatting? [For skipping type 'skip']")
    if choice.lower() == 'skip':
        download_data(url=url, url_type=urltype, path_to_store=path)
    else:
        ext = input("Enter file extension [mp4, mkv, flv]:")
        resol = input("Enter video resolution [360p, 480p, 720p]:")
        isSingleFile = bool(input("Combined/Single audio video file? [True, False]:"))
        download_data(url=url,
                      url_type=urltype,
                      form=ext,
                      res=resol,
                      separate_audio_video_file=not isSingleFile,
                      path_to_store=path)
