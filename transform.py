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
        "-movflags", "+faststart",
        file_out
    ])
    subprocess.run([
        "exiftool",
        "-tagsfromfile",
        file_in,
        "-all:all",
        "-overwrite_original",
        file_out
    ])
