import ffmpeg
from getinfo import gettime
import os

def Trim(filepath,start,end,outpath):
    """
    裁剪视频
    start，end支持%H:%M:%S或%s等格式
    """
    stream = ffmpeg.input(filepath,ss = start,to = end)
    stream = ffmpeg.output(stream,outpath)
    ffmpeg.run(stream)

def TrimPrefix(filepath,start,outpath):
    """
    裁剪视频/音频开头
    start支持%H:%M:%S或%s等格式
    """
    stream = ffmpeg.input(filepath,ss = start)
    stream = ffmpeg.output(stream,outpath)
    ffmpeg.run(stream)

def TrimSuffix(filepath,time,outpath):
    """
    裁剪视频/音频结尾
    time：裁掉结尾秒数，支持%s
    """
    time = gettime(filepath)-time
    stream = ffmpeg.input(filepath,to = time)
    stream = ffmpeg.output(stream,outpath)
    ffmpeg.run(stream)

def TrimByInterval(filepath,interval,outpath,filename="/",exfname =".mp4"):
    """
    将视频按照间隔时间interval裁剪成多段
    """
    if not os.path.isdir(outpath):
        os.mkdir(outpath)
    interval = float(interval)
    tot = gettime(filepath)
    start = 0
    end = interval
    i = 0
    flag = True
    while flag:
        if end >tot:
            end = tot
            flag = False
        outfile = outpath + filename + str(i)+exfname
        Trim(filepath,start,end,outfile)
        i+=1
        start = end
        end = end+interval
    print("trim over!")



if __name__ == "__main__":
    # Trim("../data/1.mp4",0,1,"2.mp4")
    # TrimPrefix("../data/1.mp4",2,"2.mp4")
    TrimByInterval("../data/1.mp4",1,"test")