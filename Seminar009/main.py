import pytube
import os
from moviepy.editor import ImageClip, AudioFileClip, VideoFileClip, concatenate_videoclips

url = '0'
url = input('Введите ссылку на видео: ')
if url == 'Stok':
    url = 'https://www.youtube.com/watch?v=v6zl6VdvU8A'


yt = pytube.YouTube(url)
stream=yt.streams
video_480 = yt.streams.filter(res="720p").desc().first()
audio_best = yt.streams.filter(adaptive=False, only_audio=True, abr="160kbps").desc().first()

adress = str(os.path.abspath('main.py'))
for i in range(8):
    adress = adress[:-1]

video_name = yt.title.replace( '|', '').replace( '?', '').replace( '#', '').replace( ',', '')
video_480.download(adress)
audio_best.download(adress)
thisvideo = str(adress)+'\\'+ str(video_name)+".mp4"
thisFile = str(adress)+'\\'+ str(video_name)+".webm"
ext = '.'+ os.path.realpath(thisFile).split('.')[-1:][0]
mp3file = thisFile.replace(ext,'.mp3')
os.rename(thisFile ,mp3file)


    
audio_clip = AudioFileClip(f'{str(video_name)}.mp3')
image_clip = VideoFileClip(f'{str(video_name)}.mp4')
# final_clip = concatenate_videoclips([clip1,clip2])
video_clip = image_clip.set_audio(audio_clip)
video_clip.duration = audio_clip.duration
video_clip.write_videofile(f'{str(video_name)} .mp4')


os.remove(mp3file)
os.remove(thisvideo)