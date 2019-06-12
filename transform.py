import subprocess

FFMPEG_BIN = "ffmpeg"


def transform(file_in, file_out):
    subprocess.run([
        FFMPEG_BIN,
        "-i", file_in,
        "-y",
        "-vcodec", "libx265",
        "-acodec", "mp2",
        # "-preset", "slower",
        # "-crf", "24",
        file_out

    ])
