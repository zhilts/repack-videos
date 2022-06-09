import subprocess

FFMPEG_BIN = "ffmpeg"


def transform(file_in, file_out):
    subprocess.run([
        FFMPEG_BIN,
        "-i", file_in,
        "-y",
        "-vcodec", "libx265",
        "-acodec", "aac",
        # "-preset", "ultrafast",
        # "-crf", "24",
        file_out

    ])
