import os
import platform

def system_beep():
    system = platform.system()
    if system == "Windows":
        import winsound
        winsound.Beep(1000, 1000)
    elif system == "Darwin":  # macOS
        os.system('say "警报"')
        # 或者播放系统声音
        os.system('afplay /System/Library/Sounds/Ping.aiff')
    elif system == "Linux":
        # 需要安装sox: sudo apt-get install sox
        os.system('play -nq -t alsa synth 1 sine 1000')
    else:
        print("\a")  # 终端响铃

# 使用
system_beep()