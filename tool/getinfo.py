import ffmpeg
import subprocess,json
import os


def getinfo(filepath):
    """
    获取文件帧大小
    """
    probe = ffmpeg.probe(filepath)  
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    print("width:%d,height:%d"%(width,height))
    return (width,height)

def gettime(filepath):
    """
    获取视频/音频时长
    """
    cmd = 'ffprobe -i %s -show_entries format=duration -v quiet -of csv="p=0"' % filepath
    output =os.popen(cmd,'r')
    output = output.read()
    print(output)
    return float(output[:-1])



if __name__ == "__main__":
    # getinfo("../data/1.mp4")
    gettime("../data/1.mp4")