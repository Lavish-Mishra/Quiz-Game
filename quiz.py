import json
import tkinter as tk
from tkinter import scrolledtext
import sys

#Function to Retrieve Questions
def readdata():
    ques=[]
    option=[]
    ans=[]
    file = open('quizdata.json')
    data =json.load(file)
    for i in data["data"]:
        ques.append(i["question"])
        option.append(i["option"])
        ans.append(i["answer"])
    file.close()
    return ques,option,ans,data

#Function to Check Answer
def check(topl,data,current,length,uanswer,score,root,but):
    def nextfun():
        topl.destroy()
        generateframe(data,current+1,length,score,root)
    but.destroy()
    if(uanswer==str(data["data"][current]["answer"])):
        score += 1
        label = tk.Label(topl,text="Correct", font=("Arial",20),fg="green")
        label.pack()
    else:
        label = tk.Label(topl,text=f"Incorrect! Correct: {data["data"][current]["answer"]}", font=("Arial",20),fg="red")
        label.pack()
    but = tk.Button(topl,text="Next", bg="#407ee3", width=8, fg="black", font=("Arial",20), command=nextfun)
    but.pack()

#Function to Enter new Questions
def writedata(que,op,an,root):
    _,_,_,data = readdata()
    dictionary = {"question":que,
                  "option":op,
                  "answer":an}
    
    data["data"].append(dictionary)
    insert = json.dumps(data, indent =4)
    with open("quizdata.json","w") as outfile:
        outfile.write(insert)
    mainFrame(root)



#Add Question Frame Generate
def add_questions(root):
    root.withdraw()
    frame = tk.Tk()
    frame.geometry("570x400")
    ques_label = tk.Label(frame,text="Question: ", font=("Arial",15))
    ques_label.grid(row=0, column=0, sticky="w", pady=20, padx=20)
    ques_entry = scrolledtext.ScrolledText(frame, font=("Arial",12), width=30, height=3, relief="groove")
    ques_entry.grid(row=0, column=1, sticky="w", pady=10)
    
    op1_label = tk.Label(frame,text="Option 1: ", font=("Arial",15))
    op1_label.grid(row=1, column=0, sticky="w", pady=10, padx=20)
    op1_entry = tk.Entry(frame, font=("Arial",10),width=25,relief="groove")
    op1_entry.grid(row=1, column=1, sticky="w", pady=10)
    
    op2_label = tk.Label(frame,text="Option 2: ", font=("Arial",15))
    op2_label.grid(row=2, column=0, sticky="w", pady=10, padx=20)
    op2_entry = tk.Entry(frame, font=("Arial",10),width=25,relief="groove")
    op2_entry.grid(row=2, column=1, sticky="w", pady=10)

    op3_label = tk.Label(frame,text="Option 3: ", font=("Arial",15))
    op3_label.grid(row=3, column=0, sticky="w", pady=10, padx=20)
    op3_entry = tk.Entry(frame, font=("Arial",10),width=25,relief="groove")
    op3_entry.grid(row=3, column=1, sticky="w", pady=10)

    op4_label = tk.Label(frame,text="Option 4: ", font=("Arial",15))
    op4_label.grid(row=4, column=0, sticky="w", pady=10, padx=20)
    op4_entry = tk.Entry(frame, font=("Arial",10),width=25,relief="groove")
    op4_entry.grid(row=4, column=1, sticky="w", pady=10)

    ans_label = tk.Label(frame,text="Correct Answer: ", font=("Arial",15))
    ans_label.grid(row=5, column=0, sticky="w", pady=10, padx=20)
    ans_entry = tk.Entry(frame, font=("Arial",10),width=25,relief="groove")
    ans_entry.grid(row=5, column=1, sticky="w", pady=10)

    #Getting data from Entry boxes
    def getdata(root,frame):
        frame.withdraw()
        question=ques_entry.get("1.0", tk.END)
        op1=op1_entry.get()
        op2=op2_entry.get()
        op3=op3_entry.get()
        op4=op4_entry.get()
        option=[op1,op2,op3,op4]
        answer=ans_entry.get()
        writedata(question,option,answer,root)
    
    submit_button = tk.Button(frame,text="Submit", bg="#407ee3", width=6, fg="black", font=("Arial",18),command=lambda:getdata(root,frame))
    submit_button.grid(row=6,column=1, sticky="w", pady=10, padx=20)
    
    frame.mainloop()

#Question Frames Generator
def generateframe(data,current,length,score,root):
    ques,_,_,data=readdata()
    length=len(ques)
    
    if current<length:
        root.withdraw() 
        topl = tk.Tk()
        topl.title("Quizathon")
        if(len(data["data"][current]["question"])<50):
            topl.geometry("600x430")
        else:
            size=len(data["data"][current]["question"])+600
            topl.geometry(f"{size}x400")
        topl.resizable(False,False)
        score_label = tk.Label(topl, text=f"Score: {score}", font=("Arial",20)).pack()
        label = tk.Label(topl, text = f"{current+1}. {data["data"][current]["question"]}", font=("Arial",15), justify="left")
        label.pack(pady=20,padx=10, anchor="w")
        val=tk.StringVar(topl," ")
        for i in range(0,4):
            rb1 = tk.Radiobutton(topl, text = data["data"][current]["option"][i],variable=val, value=data["data"][current]["option"][i], justify="left", font=("Arial",13)).pack(pady=5,padx=10, anchor="w")
        but=tk.Button(topl,text="Submit", bg="#407ee3", width=8, fg="black", font=("Arial",20), command=lambda: check(topl,data,current,length,val.get(),score,root,but))
        but.pack()
        topl.mainloop()
    else:
        endframe(score,length,root)


#End Frame
def endframe(score,length,root):
    frame = tk.Tk()
    frame.title("Quizathon")
    frame.geometry('500x300')
    frame.resizable(False,False)
    label = tk.Label(frame, text=f"Your Total Score is: {score} out of {length}", font=("Arial",25)).pack(pady=35)
    def execute(root,frame):
        frame.destroy()
        mainFrame(root)
    play_again = tk.Button(frame, text="Play Again", bg="#407ee3", fg="black", font=("Arial",20), command=lambda: execute(root,frame))
    play_again.pack(pady=15)

    exit_button = tk.Button(frame, text="Exit", bg="#407ee3", fg="black", font=("Arial",20), command=exit) 
    exit_button.pack(pady=20)
    frame.mainloop()

#Starting Frame
def mainFrame(root):
    if root!= None:
        root.destroy()
    root = tk.Tk()
    root.geometry('600x400')
    root.title("Quizathon")
    score=0
    title = tk.Label(root, text = "QUIZ GAME", font=("Arial",35))
    title.config(fg="red")
    title.pack(pady=35)

    data=None
    ques=0
    play_button = tk.Button(root, text="Play", width=7, bg="#C2BDBC", fg="black", font=("Arial",20), command=lambda: generateframe(data,0,ques,score,root))
    play_button.pack(pady=10)
    
    add_ques_button = tk.Button(root, text="Add More Questions", bg="#C2BDBC", fg="black", font=("Arial",20), command=lambda:add_questions(root))
    add_ques_button.pack(pady=15)

    exit_button = tk.Button(root, text="Exit", bg="#C2BDBC", fg="black", font=("Arial",20), command=exit) 
    exit_button.pack(pady=20)

    root.mainloop()

score=0
mainFrame(None)
