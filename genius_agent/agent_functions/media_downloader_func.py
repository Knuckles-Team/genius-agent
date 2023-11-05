from media_downloader import MediaDownloader


def exec_media_downloader(agent, url: str, directory: str, audio: bool = False):
    video_downloader_instance = MediaDownloader()
    video_downloader_instance.append_link(url)
    video_downloader_instance.set_save_path(directory)
    video_downloader_instance.set_audio(audio=audio)
    return agent.execute_function(func_call=video_downloader_instance.download_all())
