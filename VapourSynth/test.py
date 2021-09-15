import vapoursynth as vs
from vapoursynth import core

# 视频路径
file_path = ""

# 读取视频
src = core.lsmas.LWLibavSource(file_path, threads=1)

# 输出视频
src.set_output()
