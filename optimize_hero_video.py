from pathlib import Path
import subprocess
import imageio_ffmpeg

src = Path('assets/videos/hero-bg.mp4')
dst_temp = Path('assets/videos/hero-bg-optimized.mp4')
dst_final = Path('assets/videos/hero-bg.mp4')

if not src.exists():
    raise FileNotFoundError(f'Source video not found: {src}')

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

# Re-encode with faststart and compression
cmd = [
    ffmpeg,
    '-i', str(src),
    '-vcodec', 'libx264',
    '-preset', 'fast',
    '-crf', '22',
    '-acodec', 'aac',
    '-b:a', '128k',
    '-movflags', '+faststart',
    '-pix_fmt', 'yuv420p',
    '-y',
    str(dst_temp),
]
print('Running:', ' '.join(cmd))
subprocess.run(cmd, check=True)
print('Created optimized:', dst_temp, 'size:', dst_temp.stat().st_size)

# Replace original with optimized
import shutil
shutil.move(str(dst_temp), str(dst_final))
print('Replaced original with optimized version')
print('Final size:', dst_final.stat().st_size)
