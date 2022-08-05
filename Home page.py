from tkinter import*
from PIL import Image,ImageTk #pip install Pillow
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #import the speech recognition (pip install SpeechRecognition)
from translate import Translator #pip install translate
import PyPDF2 #pip install PyPDF2
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import os



home_page=Tk()
home_page.geometry('1280x1080')
home_page.title('HOME PAGE')
home_page.configure(bg='SkyBlue2')

engine=pyttsx3.init() #creation of the object 

#mandarin text to speech________________________________________________________________________________________________________

def mandarin():

    def speakout():
        text=text_area2.get(1.0,END)
        gender=gender_combobox2.get()
        speed= speed_combobox2.get()
        voices=engine.getProperty('voices')
        engine.setProperty("voice",voices[2].id)
#setting up the female and male voice   
        def setvoice():
            if(gender == 'Female'):
               engine.setProperty('voice',voices[2].id)
               engine.say(text)
               engine.runAndWait()
            else:
                engine.setProperty('voice',voices[2].id)
                engine.say(text)
                engine.runAndWait()
    
#setting the voice rate 
        if (text):
            if (speed =="Fast"):
                engine.setProperty('rate',250)
                setvoice()
            elif(speed == 'Normal'):
                 engine.setProperty('rate',150)
                 setvoice()
            else:
                engine.setProperty('rate',60)
                setvoice()

    

    def clear():
        text_area2.delete(1.0,END)
    
    textspeechpage2 =Toplevel(home_page)
    textspeechpage2.geometry('1280x1080')
    textspeechpage2.title('Text to Speech')
    textspeechpage2.configure(bg="SkyBlue2")


#top frame
    Top_frame2=Frame(textspeechpage2,bg='white',width=1280,height=120)
    Top_frame2.place(x=0,y=0) 

    Lgo2=PhotoImage(file="mic.png")
    Label(Top_frame2,image=Lgo2,bg="white").place(relx=0.85,rely=0.05)

    Label(Top_frame2,text="AUDIO TEXT CONVERTER",font="arial 20 bold", bg='white',fg='SkyBlue2').place(x=480,y=30)


    text_area2=Text(textspeechpage2,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
    text_area2.place(x=500,y=160,width=600,height=250)

    Label(textspeechpage2,text='VOICE',width=10,font='arial 15 bold',bg='powder Blue',fg='white').place(x=100,y=160)
    Label(textspeechpage2,text='SPEED',width=10,font='arial 15 bold',bg='powder Blue',fg='white').place(x=300,y=160)

   

    gender_combobox2=Combobox(textspeechpage2,values=['Female Only'],font='arial 14',state='r',width=10)
    gender_combobox2.place(x=100,y=200)
    gender_combobox2.set('Female Only')


    speed_combobox2=Combobox(textspeechpage2,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
    speed_combobox2.place(x=300,y=200)
    speed_combobox2.set('Normal')



    button2=Button(textspeechpage2,text='Read',width =10 ,bg='Slategray4',font='arial 14 bold ',command=speakout)
    button2.place(x=550,y=450)

  



    #clearbutton
    clear_button2=Button(textspeechpage2,text='clear',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=clear)
    clear_button2.place(x=950,y=450)

    #back button

    backbutton2=Button(textspeechpage2,text='Back',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=textspeechpage2.destroy)
    backbutton2.place(x=100,y=500)
    
#english text to speech————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————--
def english():
    
    def speakout():
        text=text_area.get(1.0,END)
        gender=gender_combobox.get()
        speed= speed_combobox.get()
        voices=engine.getProperty('voices')

        def setvoice():
            if(gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                engine.say(text)
                engine.runAndWait()
            else:
               engine.setProperty('voice',voices[1].id)
               engine.say(text)
               engine.runAndWait()
        if (text):
            if (speed =="Fast"):
                engine.setProperty('rate',350)
                setvoice()
            elif(speed == 'Normal'):
                 engine.setProperty('rate',150)
                 setvoice()
            else:
                engine.setProperty('rate',30)
                setvoice()

        
    def downloadnow():
        text=text_area.get(1.0,END)
        gender=gender_combobox.get()
        speed= speed_combobox.get()
        voices=engine.getProperty('voices')

        def setvoice():
            if(gender == 'Male'):
                engine.setProperty('voice',voices[0].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'english.mp3')
                engine.runAndWait()
                
            else:
                engine.setProperty('voice',voices[1].id)
                path=filedialog.askdirectory()
                os.chdir(path)
                engine.save_to_file(text,'english.mp3')
                engine.runAndWait()

        if (text):
            if (speed =="Fast"):
                engine.setProperty('rate',250)
                setvoice()
            elif(speed == 'Normal'):
                 engine.setProperty('rate',150)
                 setvoice()
            else:
                engine.setProperty('rate',60)
                setvoice()

    def clear():
        text_area.delete(1.0,END)
        
    textspeechpage =Toplevel(home_page)
    textspeechpage.geometry('1280x1080')
    textspeechpage.title('Text to Speech')
    textspeechpage.configure(bg="SkyBlue2")

    #icon
    image_icon=PhotoImage(file="speak.png")
    textspeechpage.iconphoto(False,image_icon)
#top frame
    Top_frame=Frame(textspeechpage,bg='white',width=1280,height=120)
    Top_frame.place(x=0,y=0)


    Label(Top_frame,text="AUDIO TEXT CONVERTER",font="arial 20 bold", bg='white',fg='SkyBlue2').place(x=480,y=30)
    
    text_area=Text(textspeechpage,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
    text_area.place(x=500,y=160,width=600,height=250)

    Label(textspeechpage,text='VOICE',width=10,font='arial 15 bold',bg='powder Blue',fg='white').place(x=100,y=160)
    Label(textspeechpage,text='SPEED',width=10,font='arial 15 bold',bg='powder Blue',fg='white').place(x=300,y=160)

    gender_combobox=Combobox(textspeechpage,values=['Male','Female'],font='arial 14',state='r',width=10)
    gender_combobox.place(x=100,y=200)
    gender_combobox.set('Male')

    speed_combobox=Combobox(textspeechpage,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
    speed_combobox.place(x=300,y=200)
    speed_combobox.set('Normal')

    button=Button(textspeechpage,text='Read',width =10 ,bg='Slategray4',fg='Black',font='arial 14 bold ',command=speakout)
    button.place(x=550,y=450)


    save=Button(textspeechpage,text='Download',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=downloadnow)
    save.place(x=750,y=450)

    #clearbutton
    clear_button=Button(textspeechpage,text='clear',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=clear)
    clear_button.place(x=950,y=450)

    #create a back button
    backbutton=Button(textspeechpage,text='Back',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=textspeechpage.destroy)
    backbutton.place(x=100,y=500)
#choose the language at the text to speech page 1——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————-——————————————————————
def textspeeechlanguagepage():
    textspeech1 =Toplevel(home_page)
    textspeech1.geometry('1280x1080')
    textspeech1.title('Text to Speech page 1')
    textspeech1.configure(bg="SkyBlue2")
    
    #create a white top frame
    whiteframe_1=Frame(textspeech1,bg='white',width=1280,height=120)
    whiteframe_1.place(x=0,y=0)

    #create frame that show the frame 
    language_frame=Frame(textspeech1,bg='white',width=600,height=400)
    language_frame.place(x=350,y=150)
    
    Label(language_frame,text=' Choose the Language that you want to convert to It !',bg='Red',relief=FLAT,fg='Black',font='arial 12 bold',).place(relx=0.15,rely=0.1)
    Button(language_frame,text='Mandarin',width =15,bg='Light Blue',fg='Black',font='arial 12 bold',command=mandarin).place(relx=0.35,rely=0.3)
    Button(language_frame,text='English',width =15,bg='Light Blue',fg='Black',font='arial 12 bold',command=english).place(relx=0.35,rely=0.60)
    #create a back button
    Button(textspeech1,text='Back',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=textspeech1.destroy).place(x=100,y=500)
  
#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————    
def mandarin_speechtext():
    def database_chtext():
        text_info=text1.get()
        #save into db
        if (text_info==""):
            MessageBox.showinfo("Empty", "Please Record Something")
            mandarin_page.destroy()
        else:
             con = mysql.connect(host="localhost",user="root", password="", database="python-tkinter")
             cursor = con.cursor()
             cursor.execute("insert into mandarin_text values('"+text_info +"')")
             cursor.execute("commit");

             MessageBox.showinfo("Insert Status", "Data Saved");
             mandarin_page.destroy()
             con.close();
    def clear_2():
        text1.delete(0,END)
    def recordmandarin():
        
         while True:
              r = sr.Recognizer()
              with sr.Microphone() as source: #using the microphone as the souurce
                   audio=r.listen(source) #listen the first speech and convert into audio data
                   try:    
                        text1 = r.recognize_google(audio,language="zh")
                   except:
                        pass
                   return text1
    mandarin_page = Toplevel(home_page)
    mandarin_page.title('Speech-to-Text Converter: Mandarin Language')
    mandarin_page.geometry("1280x1080")
    mandarin_page.configure(bg='skyblue2')

    Frame(mandarin_page,bg='white',width=1280,height=120).place(x=0,y=0)
    Label(mandarin_page, text='Speech-to-Text Converter ', font=("arial 20 bold"), bg='white',fg='Skyblue2').place(x=500)

    text1=StringVar()
    text1= Entry(mandarin_page, font=12, width=60)
    text1.place(x=300, y=450)

    # Create a photoimage object of the image in the path
    microphoneimage = Image.open("microphone.png")
    test = ImageTk.PhotoImage(microphoneimage)

    labelimage =Label(mandarin_page,image=test)
    labelimage.image = test

    # Position image
    labelimage.place(x=520, y=150)
   
    buttonforrecord= Button(mandarin_page, text='Record',font='arial 18 bold', bg='Red',fg='black', command=lambda: text1.insert(END, recordmandarin()))
    buttonforrecord.place(x=580,y=380)

    #back button
    backbutton=Button(mandarin_page, text='BACK',font='arial 18 bold', bg='blue',fg='white', command=mandarin_page.destroy)
    backbutton.place(x=100,y=450)
    #clear button
    Button(mandarin_page,text='clear',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=clear_2).place(x=560,y=560)
    #save text button
    Button(mandarin_page,text='Save',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=database_chtext).place(x=760,y=560)    
 

    
def malay_speechtext():
    def database_bmtext():
        text_info=text3.get()
        #save into db
        if (text_info==""):
            MessageBox.showinfo("Empty", "Please Record Something")
            malay_page.destroy()
        else:
             con = mysql.connect(host="localhost",user="root", password="", database="python-tkinter")
             cursor = con.cursor()
             cursor.execute("insert into bahasa_melayu_text values('"+text_info +"')")
             cursor.execute("commit");

             MessageBox.showinfo("Insert Status", "Data Saved");
             malay_page.destroy()
             con.close();

        
    def clear_3():
        text3.delete(0,END)
    def recordmalay():
        while True:
             r = sr.Recognizer()
             with sr.Microphone() as source:
                 audio=r.listen(source)
                 try:    
                      text3 = r.recognize_google(audio,language="ms-MY")
                 except:
                    pass
                 return text3
    malay_page=Toplevel(home_page)
    malay_page.title('Speech-to-Text Converter: Malay Language')
    malay_page.geometry("1280x1080")
    malay_page.configure(bg='skyblue2')

    Frame(malay_page,bg='white',width=1280,height=120).place(x=0,y=0)
    Label(malay_page, text='Speech-to-Text Converter ', font=("arial 20 bold"), bg='white',fg='Skyblue2').place(x=500)


    text3=StringVar()
    text3= Entry(malay_page, font=12, width=60)
    text3.place(x=300, y=450)

    # Create a photoimage object of the image in the path
    microphoneimage = Image.open("microphone.png")
    test3 = ImageTk.PhotoImage(microphoneimage)

    labelimage3 =Label(malay_page,image=test3)
    labelimage3.image = test3

    # Position image
    labelimage3.place(x=520, y=150)
   
    buttonforrecord3= Button(malay_page, text='Record',font='arial 18 bold', bg='Red',fg='black', command=lambda: text3.insert(END, recordmalay()))
    buttonforrecord3.place(x=580,y=380)

    #back button
    backbutton3=Button(malay_page, text='BACK',font='arial 18 bold', bg='blue',fg='white', command=malay_page.destroy)
    backbutton3.place(x=100,y=450)

    #clear button
    Button(malay_page,text='clear',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=clear_3).place(x=560,y=560)
    #save text button
    Button(malay_page,text='Save',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=database_bmtext).place(x=760,y=560)    



def english_speechtext():
    def database_englishtext():
        text_info=text2.get()
        #save into db
        if (text_info==""):
            MessageBox.showinfo("Empty", "Please Record Something")
            english_page.destroy()
        else:
             con = mysql.connect(host="localhost",user="root", password="", database="python-tkinter")
             cursor = con.cursor()
             cursor.execute("insert into english_text values('"+text_info +"')")
             cursor.execute("commit");

             MessageBox.showinfo("Insert Status", "Data Saved");
             english_page.destroy()
             con.close();
    def clear_4():
        text2.delete(0,END)
    def recordenglish():
        while True:
             r = sr.Recognizer()
             with sr.Microphone() as source:
                  audio=r.listen(source)
                  try:    
                        text2 = r.recognize_google(audio,language="en")
                  except:
                      pass
                  return text2
    english_page=Toplevel(home_page)
    english_page.title('Speech-to-Text Converter: English Language')
    english_page.geometry("1280x1080")
    english_page.configure(bg='skyblue2')

    Frame(english_page,bg='white',width=1280,height=120).place(x=0,y=0)
    Label(english_page, text='Speech-to-Text Converter ', font=("arial 20 bold"), bg='white',fg='Skyblue2').place(x=500)

    text2=StringVar()
    text2= Entry(english_page, font=12, width=60)
    text2.place(x=300, y=450)

    # Create a photoimage object of the image in the path
    microphoneimage = Image.open("microphone.png")
    test2 = ImageTk.PhotoImage(microphoneimage)

    labelimage2 =Label(english_page,image=test2)
    labelimage2.image = test2

    # Position image
    labelimage2.place(x=520, y=150)
   
    buttonforrecord2= Button(english_page, text='Record',font='arial 18 bold', bg='Red',fg='black', command=lambda: text2.insert(END, recordenglish()))
    buttonforrecord2.place(x=580,y=380)

    #back button
    backbutton2=Button(english_page, text='BACK',font='arial 18 bold', bg='blue',fg='white', command=english_page.destroy)
    backbutton2.place(x=100,y=450)

    #clear button
    Button(english_page,text='clear',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=clear_4).place(x=560,y=560)
    #save text button
    Button(english_page,text='Save',width =10,bg='Slategray4',fg='Black',font='arial 14 bold',command=database_englishtext).place(x=760,y=560)    
def speechtextlanguagepage():
    speechtextpage1=Toplevel(home_page)
    speechtextpage1.geometry('1280x1080')
    speechtextpage1.title('Speech to Text')
    speechtextpage1.configure(bg="SkyBlue2")

    topp=Frame(speechtextpage1,bg='white',width=1280,height=120) #create frame at the top
    topp.place(x=0,y=0)
    Label(speechtextpage1,text='Audio Text Converter',font="arial 20 bold", bg='white',fg='SkyBlue2').place(x=500,y=30)

    language_frame=Frame(speechtextpage1,bg='white',width=600,height=400)
    language_frame.place(x=350,y=150)
    
    Label(language_frame,text=' Choose the Language that you want to convert to It !',bg='Red',relief=FLAT,fg='Black',font='arial 12 bold',).place(relx=0.15,rely=0.1)
    Button(language_frame,text='Mandarin',width =15,bg='Light Blue',fg='Black',font='arial 12 bold',command=mandarin_speechtext).place(relx=0.35,rely=0.3)
    Button(language_frame,text='Bahasa Melayu',width =15,bg='Light Blue',fg='Black',font='arial 12 bold',command=malay_speechtext).place(relx=0.35,rely=0.45)
    Button(language_frame,text='English',width =15,bg='Light Blue',fg='Black',font='arial 12 bold',command=english_speechtext).place(relx=0.35,rely=0.60)
    #back button
    Button(speechtextpage1, text='BACK',font='arial 18 bold', bg='blue',fg='white', command=speechtextpage1.destroy).place(x=100,y=450)
 

    frame_top=Frame(speechtextpage1,bg='white',width=1280,height=120) #create frame at the top
    frame_top.place(x=0,y=0)
    Label1=Label(speechtextpage1,text='Audio Text Converter',font="arial 20 bold", bg='white',fg='SkyBlue2').place(x=500,y=30)


#____________________________________________________________________________________________________________________________________

def Translation():
   
#from_lang is auto detect with the input language
#to_lang=the output language 
    def translate():
           translation = Translator(from_lang= InputLanguage.get(),to_lang=OutputLanguage.get())
           Translation = translation.translate(inputVar.get())
           Output_Var.set(Translation)

        

    translation_1=Toplevel(home_page)
    translation_1.geometry('1280x1080')
    translation_1.title('Language Translation')
    translation_1.configure(bg='SkyBlue2')

    top_1=Frame(translation_1,bg='white',width=1280,height=120) #create frame at the top
    top_1.place(x=0,y=0)
    Label(translation_1,text='Audio Text Converter',font="arial 20 bold", bg='white',fg='SkyBlue2').place(x=500,y=30)

    #store in textbox
    InputLanguage = StringVar()
    OutputLanguage = StringVar()
    #tupple
    LanguageChoices = {'Spanish','English','Ms-Malay','Chinese','Japanese','Hindi'}
    InputLanguage.set('Choose')
    OutputLanguage.set('Choose')

    
    #create optional menu
    InputLanguageChoiceMenu =OptionMenu(translation_1,InputLanguage,*LanguageChoices)
    Label(translation_1,text="Choose  Language:").place(x=150,y=120)
    InputLanguageChoiceMenu.place(x=300,y=120)
    NewLanguageChoiceMenu = OptionMenu(translation_1,OutputLanguage,*LanguageChoices)
    Label(translation_1,text="Choose Language:").place(x=150,y=370)
    NewLanguageChoiceMenu.place(x=300,y=370)




    Label(translation_1,text="Input Text",bg='blue',fg='white').place(x=150,y=150)
    inputVar = StringVar()
    TextBox = Entry(translation_1,textvariable=inputVar).place(x=150,y=180,width=500,height=150)
 
    Label(translation_1,text="Output Text:",bg='blue',fg='white').place(x=150,y=430)
    Output_Var = StringVar()
    TextBox = Entry(translation_1,textvariable=Output_Var).place(x=150,y=450,width=500,height=150)
 
#Button for calling function
    Translate_button = Button(translation_1,text="Translate",width=12,command=translate, relief = GROOVE).place(x=520,y=350)
     #back button
    Button(translation_1, text='BACK',font='arial 12 bold', bg='blue',fg='white', command=translation_1.destroy).place(x=80,y=450)
 

    

def backtofirstpage():
    home_page.destroy()


#quiz---------------------------------------------------------------------------------------------------
def Quizz():
    def startQuiz():
        
        def database():
            username_info = username.get()
            Answer1_info = Answer1.get()
            Answer2_info = Answer2.get()
            Answer3_info = Answer3.get()
            Answer4_info = Answer4.get()
            Answer5_info = Answer5.get()

            #save into db
            if(username_info== "" or Answer1_info=="" or Answer2_info=="" or Answer3_info=="" or Answer4_info=="" or Answer5_info==""):
                MessageBox.showinfo("Insert status", "All fields are required")
                screen1.destroy()
                screen.destroy()
            else:
                con = mysql.connect(host="localhost",user="root", password="", database="python-tkinter")
                cursor = con.cursor()
                cursor.execute("insert into quiz values('"+ username_info +"','" + Answer1_info + "','"+ Answer2_info +"','"+ Answer3_info +"','"+ Answer4_info +"','"+ Answer5_info +"')")
                cursor.execute("commit");

                MessageBox.showinfo("Success !", "Quiz have been submit , please wait for the result");
                screen1.destroy()
                screen.destroy()
                con.close();
        global screen1
        screen1 = Toplevel(home_page)
        screen1.title ("quiz form")
        screen1.geometry("1280x1080")
        screen1.configure(bg='skyblue2')

        global username
        global username_entry

        username = StringVar()

         #prompt user to enter the username
        Label(screen1, text = "Quiz have Start now, you are allowed to answer the 5 quiz questions", bg = "White", width = "300", height = "2", font = ("Calibri", 17)).pack()
        

        Label(screen1, text = "Write down your Username", bg='skyblue2', font = ("Calibri", 20)).pack(side=TOP)
        username_entry = Entry(screen1, textvariable = username, width=30)
        username_entry.pack()

        global Answer1
        global Answer2
        global Answer3
        global Answer4
        global Answer5


        Answer1 = StringVar()
        Answer2 = StringVar()
        Answer3 = StringVar()
        Answer4 = StringVar()
        Answer5 = StringVar()

        
        #Questions for Quiz
        q1_label = Label(screen1, text="Q1. How many are spoken worldwide?", bg='skyblue2', font = ("Calibri", 12)).place(x=490,y=160)
        q1_entry = Entry(screen1, textvariable = Answer1, width=100)
        q1_entry.place(x=430,y=180)

        
        q2_label = Label(screen1, text="Q2. Which language has the second-most native speakers?", bg='skyblue2', font = ("Calibri", 12)).place(x=490,y=220)
        q2_entry = Entry(screen1, textvariable = Answer2, width=100)
        q2_entry.place(x=430,y=240)

        
        q3_label = Label(screen1, text="Q3. Which book has been translated into the most language?", bg='skyblue2', font = ("Calibri", 12)).place(x=490,y=280)
        q3_entry = Entry(screen1, textvariable = Answer3, width=100)
        q3_entry.place(x=430,y=300)

        
        q4_label = Label(screen1, text="Q4. The first printed book was written in which language?", bg='skyblue2', font = ("Calibri", 12)).place(x=490,y=340)
        q4_entry = Entry(screen1, textvariable = Answer4, width=100)
        q4_entry.place(x=430,y=360)

        
        q5_label = Label(screen1, text="Q5. What was the first language spoken in outer space?", bg='skyblue2',font = ("Calibri", 12)).place(x=490,y=400)
        q5_entry = Entry(screen1, textvariable = Answer5, width=100)
        q5_entry.place(x=430,y=420)

        
        Button(screen1, text = "Finish",bg='Red',fg='white', height = "2", width = "30",command=database).place(x=430,y=450)
        Button(screen1, text = "Back",bg='Blue',fg='white', height = "2", width = "30",command=screen1.destroy).place(x=700,y=450)



    global screen
    screen = Toplevel(home_page)
    screen.geometry("1280x1080")
    screen.title("Quiz Page")
    screen.configure(bg='skyblue2')
    
    Label(screen,text = "Click the button to Start the Quiz", bg = "White", width = "300", height = "2", font = ("Calibri", 17)).pack()
    
    
    Button(screen,text = "Start Quiz",bg='Blue', fg='white',height = "2", width = "30", font = ("Calibri", 15), command = startQuiz).pack()
    Button(screen, text = "Back",bg='Blue',fg='white', height = "2", width = "30", font = ("Calibri", 15),command=screen.destroy).pack()
    
    
#--------------------------------------------------------------------------------------------------------------------------
def pdftotext():
    def clearthetext():
          pdf_text.delete(1.0,END)
    def openfile():
        #code that only access for open pdf file 
         file_open=filedialog.askopenfilename(initialdir="C:/",title='open pdf file',filetypes=(('pdf files','*.pdf'),('all files','*.*')))
         #check to see if there is a file
         if file_open:
             #open the pdf file
             file_pdf=PyPDF2.PdfFileReader(file_open)
              #set the page to read 
             page=file_pdf.getPage(0)
              #extract the text from the pdf file#convert the pdf to text code
             page_text=page.extractText()
              #store the text into textbox
             pdf_text.insert(1.0,page_text)
              
    pdftotext_page=Toplevel(home_page)
    pdftotext_page.geometry('1280x1080')
    pdftotext_page.title('Pdf To Text Conversion')
    pdftotext_page.configure(bg='Skyblue')

    #place the textbox
    pdf_text=Text(pdftotext_page,height=35,width=100)
    pdf_text.place(y=30)

    #create menu
    the_menu=Menu(pdftotext_page)
    pdftotext_page.config(menu=the_menu)

    #add the dropdown menu
    open_menu=Menu(the_menu,tearoff=False)
#add the file option menu into add_casscade
#cascade is Creates a new hierarchical menu by associating a given menu to a parent menu
    the_menu.add_cascade(label='Menu',menu=open_menu)
#add the command into the menu
    open_menu.add_command(label='exit',command=pdftotext_page.destroy)



#clear button
    Button(pdftotext_page,text='Clear All',width=15,font='arial 15 bold',bg='Blue',fg='white',command=clearthetext).place(x=850,y=500)
    #open file button
    Button(pdftotext_page,text='Open File',width=15,font='arial 15 bold',bg='Blue',fg='white',command=openfile).place(x=850,y=400)



#label to open text speech page________________________________________________________________________________________________________
label1=Label(home_page,text='Text to Speech',width =15 ,font='arial 14 bold ',bg='powder Blue',fg='Black')
label1.place(x=150,y=200)

#label to open speech to text______________________________________________________________________________________________________-------
label2=Label(home_page,text='Speech to text',width=15 ,font='arial 15 bold',bg='powder Blue',fg='Black')
label2.place(x=500,y=200)

#label the language translator________________________________________________________________________________________________________
label3=Label(home_page,text='Translator',width=15 ,font='arial 15 bold',bg='powder Blue',fg='Black')
label3.place(x=800,y=200)


#label the quiz________________________________________________________________________________________________________
label4=Label(home_page,text='Quiz',width=15 ,font='arial 15 bold',bg='powder Blue',fg='Black')
label4.place(x=300,y=400)


#label the pdf to text ________________________________________________________________________________________________________
label5=Label(home_page,text='Pdf to text',width=15 ,font='arial 15 bold',bg='powder Blue',fg='Black')
label5.place(x=600,y=400)


#create an top frame________________________________________________________________________________________________________
White_space=Frame(home_page,bg='white',width=1280,height=100)
White_space.place(x=0,y=0)

#create name as AUDIO TEXT CONVERTER________________________________________________________________________________________________________
Label1=Label(White_space,text='Audio Text Converter',font="arial 20 bold", bg='white',fg='SkyBlue2').place(x=500,y=30)

#######create image and place them beside all the button-------------------------------------------------------------------------------------
#Create a photoimage object of the image in the path

#button to open textspeechlanguagepage__________________________________________________________________________________________________
photo1 = PhotoImage(file = "text to speech.png")
photoimage = photo1.subsample(2, 2)# Resize image to fit on button
Button(home_page, image = photoimage,command=textspeeechlanguagepage).place(x=170, y=250)# Position image on button

#button to open speechtextlanguage_page_____________________________________________________________________________________________________________
photo2 = PhotoImage(file = "speech to text.png")
phimage= photo2.subsample(2, 2)
Button(home_page, image = phimage,command=speechtextlanguagepage).place(x=510, y=250)

#button to open translation page__________________________________________________________________________________________________________________________
photo3 = PhotoImage(file = "language.png")
phimage2= photo3.subsample(2, 2)
Button(home_page, image = phimage2,command=Translation).place(x=850, y=250)

#button to open quiz ________________________________________________________________________________________________________
photo4 = PhotoImage(file = "quizz.png")
phimage3= photo4.subsample(2, 2)
Button(home_page, image = phimage3,command=Quizz).place(x=330, y=450)


#buttton to open pdf to text ________________________________________________________________________________________________________
photo5 = PhotoImage(file = "pdftotext.png")
phimage4= photo5.subsample(2, 2)
Button(home_page, image = phimage4,command=pdftotext).place(x=630, y=450)

#exit application button________________________________________________________________________________________________________
Button(home_page,text='Exit',width =15,bg='red',fg='Black',font='arial 12 bold',command=backtofirstpage).place(relx=0.8,rely=0.2)

home_page.mainloop()
