from flask import Flask ,render_template,request
from main import audioGenerator,stichAnnouncement

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    success = False
    if request.method =="POST":
        Train_no = request.form["train_number"]
        Train_from = request.form["train_from"]
        Train_Via = request.form["train_via"]
        Train_To = request.form["train_to"]
        Platform_Number = request.form["platform_number"]
        Train_no = " ".join(Train_no)
        stichAnnouncement(audioGenerator([Train_no,Train_from,Train_Via,Train_To,Platform_Number]))
        success = True
    return render_template("home.html",success = success)


if __name__=="__main__":
    app.run(debug=True)