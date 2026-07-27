from pathlib import Path
import shutil
import subprocess
import imageio_ffmpeg

src = Path('assets/videos/IMG_5442 1.MOV')
dst = Path('assets/videos/hero-bg.mp4')

if not src.exists():
    raise FileNotFoundError(f'Source video not found: {src}')

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
cmd = [
    ffmpeg,
    '-i', str(src),
    '-vcodec', 'libx264',
    '-acodec', 'aac',
    '-movflags', '+faststart',
    '-pix_fmt', 'yuv420p',
    '-y',
    str(dst),
]
print('Running:', ' '.join(cmd))
subprocess.run(cmd, check=True)
print('Created:', dst, 'size:', dst.stat().st_size)
