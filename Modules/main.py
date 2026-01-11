import os
from pydub import AudioSegment
import gtts


def audioGenerator(lst):
    text = f"कृपया ध्यान दीजिए: गाड़ी संख्या {lst[0]}, {lst[1]} से चलकर {lst[2]} के रास्ते {lst[3]} जाने वाली, प्लेटफार्म संख्या {lst[4]} पर आ रही है।"
    gtts.gTTS(text=text,lang="hi",slow=True).save(f"AudioFiles/GeneratedFiles/announcement.mp3")

def stichAnnouncement():

    final_audio = AudioSegment.from_mp3("AudioFiles/Pre-GeneratedFiles/pre.mp3") + AudioSegment.from_mp3("AudioFiles/GeneratedFiles/announcement.mp3")
    final_audio.export("static/final_announcement.mp3",format="mp3")



if __name__=="__main__":
    train_no = list(input("Enter Train Number : "))
    train_from = input("Enter Train From : ")
    train_via = input("Enter Train Via : ")
    train_to = input("Enter Train to :")
    platform_no = input("Enter Platform Number :")
    train_no = "".join(i+" " for i in train_no)
    lst = [train_no,train_from,train_via,train_to,platform_no]
    audioGenerator(lst)
    stichAnnouncement()

