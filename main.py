import os
from pydub import AudioSegment
import gtts

def arrangeList():
    pass


def audioGenerator(lst):
    for i in range(len(lst)):
        gtts.gTTS(text=lst[i],lang="hi").save(f"AudioFiles/GeneratedFiles/{i}.mp3")

def stichAnnouncement(lst):
    pass


if __name__=="__main__":
    train_no = list(input("Enter Train Number : "))
    train_from = input("Enter Train From : ")
    train_via = input("Enter Train Via : ")
    train_to = input("Enter Train to :")
    platform_no = input("Enter Platform Number :")
    train_no = "".join(i+" " for i in train_no)
    lst = [train_no,train_from,train_via,train_to,platform_no]
    audioGenerator(lst)

