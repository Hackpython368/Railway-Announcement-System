import os
from pydub import AudioSegment
import gtts


def audioGenerator(lst):
    file_lst = []
    for i in range(len(lst)):
        gtts.gTTS(text=lst[i],lang="hi").save(f"AudioFiles/GeneratedFiles/{i}.mp3")
        file_lst.append(f"AudioFiles/GeneratedFiles/{i}.mp3")
    return file_lst

def stichAnnouncement(lst):
    read_audio = []
    for i in lst:
        read_audio.append(AudioSegment.from_mp3(i))
    
    pre_audio = os.listdir(f"AudioFiles/Pre-audioFiles/")
    load_pre = []
    for i in pre_audio:
        load_pre.append(AudioSegment.from_mp3(f"AudioFiles/Pre-audioFiles/{i}"))

    final_audio = load_pre[0] + load_pre[1] + read_audio[0] + read_audio[1] + load_pre[2] + read_audio[2] + load_pre[3] + read_audio[4] + load_pre[4]
    final_audio._spawn(final_audio.raw_data,overrides={
        "frame_rate": int(final_audio.frame_rate * 0.8)
    })
    final_audio.export("o.mp3",format="mp3")



if __name__=="__main__":
    train_no = list(input("Enter Train Number : "))
    train_from = input("Enter Train From : ")
    train_via = input("Enter Train Via : ")
    train_to = input("Enter Train to :")
    platform_no = input("Enter Platform Number :")
    train_no = "".join(i+" " for i in train_no)
    lst = [train_no,train_from,train_via,train_to,platform_no]
    stichAnnouncement(audioGenerator(lst))

