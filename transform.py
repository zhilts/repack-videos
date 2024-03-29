import subprocess

FFMPEG_BIN = "ffmpeg"


def transform(file_in, file_out, h264):
    subprocess.run([
        FFMPEG_BIN,
        "-i", file_in,
        "-map_metadata", "0",
        "-y",
        "-vcodec", "libx264" if h264 else "libx265",
        "-acodec", "aac",
        # "-preset", "ultrafast",
        # "-crf", "24",
        file_out

    ])
