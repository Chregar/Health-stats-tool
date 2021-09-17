from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter.messagebox as tmsg


PAGE_BREAK = "C:\\Users\\Ahmad Shreif\\PycharmProjects\\Health-stats-tool\\sourceii\\break2.PNG"

MAIN_FONT = ("Arial",24,"bold")
MAIN_FONT_COLOR = "#184A80"
SMALL_FONT_COLOR = "#050607"
SMALL_FONT = ("Arial",12,"bold")
SMALL_FONT_2 = ("Arial",12)
WHITE = "white"
SECONDARY_FONT = ("Arial",16,"bold")
FONT3 = ("Times New Roman",16)




root = Tk()
root.title('Calculator')
root.configure(background = 'white')

#app.configure(background='C:\\Usfront.png')

def term_of_use():
    tmsg.showinfo('Terms of Use ','IF YOU LIVE IN (OR IF YOUR PRINCIPAL PLACE OF BUSINESS IS IN) THE UNITED STATES, PLEASE READ THE BINDING ARBITRATION CLAUSE AND CLASS ACTION WAIVER IN SECTION 11. IT AFFECTS HOW DISPUTES ARE RESOLVED.')

def send_feedback():
    ans=tmsg.askquestion('Feedback Hub','Was your experience good with us ? ')
    if ans=='yes':
        tmsg.showinfo('Feedback','Please Rate us on AppStore')
    else:
        tmsg.showinfo('Feedback','We will contact you soon to know about your bad experience')

my_menu=Menu(root)
m1=Menu(my_menu,tearoff=0,fg='red')
m1.add_command(label='Terms of Use',command=term_of_use)
m1.add_command(label='Send Feedback',command=send_feedback)
root.config(menu=my_menu)
my_menu.add_cascade(label=' About ',menu=m1)
my_menu.add_command(label='Exit',command=quit)



def on_close():
    response=messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()

root.protocol('WM_DELETE_WINDOW',on_close)


labelText = StringVar()
labelText.set("       Learn How Many Calories You Burn Every Day ")
labelDir = Label(root, textvariable=labelText,
                         font=MAIN_FONT, bg='white', fg=MAIN_FONT_COLOR, height=4)
labelDir.grid(row=0, column=0)


labelText2  = Label(text = " Use the TDEE calculator to learn your Total Daily Energy Expenditure, a measure of how many calories you "
               "burn per day. ",font=SMALL_FONT, bg='white', fg=SMALL_FONT_COLOR)

labelText2.grid(row = 2,column = 0)
labelText2  = Label(text = " You will also be able to calculate and display your BMI, BMR, Macros & "
               "many other useful statistics!",font=SMALL_FONT_2, bg='white', fg=SMALL_FONT_COLOR)

labelText2.grid(row = 3,column = 0)

p_break_image = PhotoImage(file = PAGE_BREAK)
p_break = Label(image = p_break_image,bg = "#A2A5A1").grid(row = 7,column = 0,columnspan = 3,sticky = NSEW)



def TDEE_Button():
    top_start = Toplevel()
    top_start.configure(background=WHITE)
    top_start.title('TDEE Calculator')

    radioGroup = LabelFrame(top_start, text="Select Gender", bg=WHITE, font=SECONDARY_FONT)
    radioGroup.grid(row=0, column=0)

    def get():
        global gender_choice
        gender_choice = gender.get()


    gender = IntVar()

    male = Radiobutton(radioGroup, text="Male", font=SMALL_FONT,
                       variable=gender, value=1, bg=WHITE,command = get).pack()
    female = Radiobutton(radioGroup, text="Female", font=SMALL_FONT,
                         variable=gender, value=0, bg=WHITE,command = get).pack()

    if gender.get() == "Male":
        pass
    if gender.get() == "Female":
        pass



    p_break_image = PhotoImage(file=PAGE_BREAK)
    p_break = Label(top_start,image=p_break_image, bg="#A2A5A1").grid(row=1, column=0, columnspan=3, sticky=NSEW)

    AgeGroup = LabelFrame(top_start, text="Age", bg=WHITE, font=SECONDARY_FONT)
    AgeGroup.grid(row=2, column=0)

    age_variable = StringVar()
    age_entry = Entry(AgeGroup, textvariable=age_variable, font=FONT3, bg=WHITE, width=30,
                         borderwidth=15)
    age_entry.grid(row=3, column=0, columnspan=3)
    new_text = 'years'
    age_variable.set(new_text)




    p_break_image2 = PhotoImage(file=PAGE_BREAK)
    p_break2 = Label(top_start,image=p_break_image2, bg="#A2A5A1").grid(row=4, column=0, columnspan=3, sticky=NSEW)

    WeightGroup = LabelFrame(top_start, text="Weight", bg=WHITE, font=SECONDARY_FONT)
    WeightGroup.grid(row=6, column=0)


    weight_variable = StringVar()
    weight_entry = Entry(WeightGroup, textvariable=weight_variable, font=FONT3, bg=WHITE, width=30,
                         borderwidth=15)
    weight_entry.grid(row=7, column=0, columnspan=3)
    new_text = 'kg'
    weight_variable.set(new_text)


    p_break_image3 = PhotoImage(file=PAGE_BREAK)
    p_break3 = Label(top_start,image=p_break_image3, bg="#A2A5A1").grid(row=8, column=0, columnspan=3, sticky=NSEW)

    HeightGroup = LabelFrame(top_start, text="Height", bg=WHITE, font=SECONDARY_FONT)
    HeightGroup.grid(row=9, column=0)

    height_variable = StringVar()
    height_entry = Entry(HeightGroup, textvariable=height_variable, font=FONT3, bg=WHITE, width=30,borderwidth=15)
    height_entry.grid(row=10, column=0, columnspan=3)
    new_text = 'cm'
    height_variable.set(new_text)


    p_break_image4 = PhotoImage(file=PAGE_BREAK)
    p_break4 = Label(top_start, image=p_break_image4, bg="#A2A5A1").grid(row=11, column=0, columnspan=3, sticky=NSEW)

    ActivityLevel = LabelFrame(top_start, text="Activity", font=SECONDARY_FONT, bg=WHITE, width=30)
    ActivityLevel.grid(row=12, column=0)

    def comboclick(event):
        myLabel = Label(ActivityLevel,text = ActivityLevel_box.get())
        level_of_activity = ActivityLevel_box.get()

    #clicked = StringVar()
    #clicked.set("2")

    options_activ = ["Sedentary (office job)",
                     "Light Exercise (1-2 days / week) ",
                     "Moderate Exercise (3-5 days / week)",
                     "Heavy Exercise (6-7 days / week)",
                     "Athlete (2x per day)"]
    ActivityLevel_box = ttk.Combobox(ActivityLevel,value = options_activ,width = 35,font = SMALL_FONT_2)
    ActivityLevel_box.current(0)
    ActivityLevel_box.bind("<<ComboboxSelected>>",comboclick)
    ActivityLevel_box.pack()

    def on_close2():
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
        if response:
            top_start.destroy()

    top_start.protocol('WM_DELETE_WINDOW', on_close)

    def proceed_button():
        top_tdee = Toplevel()
        top_tdee.configure(background=WHITE)
        top_tdee.title('TDEE Calculator')
        global number1
        global number2
        global number3

        def on_close3():
            response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
            if response:
                top_tdee.destroy()

        top_tdee.protocol('WM_DELETE_WINDOW', on_close)

        AnswerGroup = LabelFrame(top_tdee, text="Your Total Daily Energy Expenditure:", bg=WHITE, font=SECONDARY_FONT)
        AnswerGroup.grid(row=0, column=0)

        result_entry = Entry(AnswerGroup, font=SECONDARY_FONT, bg=WHITE, width=30, borderwidth=15)
        result_entry.grid(row=10, column=0, columnspan=3)

        #TDEE = BMR + TEF + EEE + NEAT
        #Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
        #Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)
        #TEF = BMR * 0.1
        #EEE and NEAT are a global range of values


        if ActivityLevel_box.get() == options_activ[0]: #Sedentary
            if gender_choice == 1: #male
                EEE = 250
                NEAT = 250
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))+
                                    ((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))*0.1)
                                    +121))
            if gender_choice == 0: #female
                EEE = 250
                NEAT = 250
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((447.593 + (9.247 * float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))+
                                    ((447.593 + (9.247* float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))*0.1)
                                    +121))
        if ActivityLevel_box.get() == options_activ[1]: #Light exercise
            if gender_choice == 1: #male
                EEE = 315
                NEAT = 315
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))+
                                    ((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))*0.1)
                                    +428))

            if gender_choice == 0: #female
                EEE = 315
                NEAT = 315
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((447.593 + (9.247 * float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))+
                                    ((447.593 + (9.247* float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))*0.1)
                                    +428))

        if ActivityLevel_box.get() == options_activ[2]: #Moderate exercise
            if gender_choice == 1: #male
                EEE = 440
                NEAT = 440
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))+
                                    ((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))*0.1)
                                    +735))


            if gender_choice == 0: #female
                EEE = 440
                NEAT = 440
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0,round((447.593 + (9.247 * float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))+
                                    ((447.593 + (9.247* float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))*0.1)
                                    +735))


        if ActivityLevel_box.get() == options_activ[3]: #Heavy exercise
            if gender_choice == 1: #male
                EEE = 640
                NEAT = 640
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))+
                                    ((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))*0.1)
                                    +1042))

            if gender_choice == 0: #female
                EEE = 640
                NEAT = 640
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((447.593 + (9.247 * float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))+
                                    ((447.593 + (9.247* float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))*0.1)
                                    +1042))


        if ActivityLevel_box.get() == options_activ[4]: #athlete
            if gender_choice == 1: #male
                EEE = 750
                NEAT = 750
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                result_entry.insert(0, round((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))+
                                    ((88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1)))*0.1)
                                    +1350))

            if gender_choice == 0: #female
                EEE = 750
                NEAT = 750
                number1 = age_entry.get()
                number2 = weight_entry.get()
                number3 = height_entry.get()
                global result
                result_entry.insert(0, round((447.593 + (9.247 * float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))+
                                    ((447.593 + (9.247* float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1)))*0.1)
                                    +1350))


        answer =  result_entry.get()
        labelText5 = StringVar()
        labelText5.set("Based on your stats, the best estimate for your maintenance calories is\n "
                       +answer+" calories per day based on the Mifflin-St \nJeor Formula,"
                       " which is widely known to be the most accurate."
                       )
        labelDir5 = Label(top_tdee, textvariable=labelText5,
                         font=SECONDARY_FONT, bg='white', fg=MAIN_FONT_COLOR, height=6)
        labelDir5.grid(row=2, column=0)

        #pagebreak
        p_break_image6 = PhotoImage(file=PAGE_BREAK)
        p_break6 = Label(top_tdee, image=p_break_image6, bg="#A2A5A1").grid(row=4, column=0, columnspan=3,
                                                                             sticky=NSEW)

        labelText6 = StringVar()
        labelText6.set("Click the button "
                       "below to see the difference if you were to have selected a different activity level."
                       )
        labelDir6 = Label(top_tdee, textvariable=labelText6,
                          font=SMALL_FONT_2, bg='white', fg=SMALL_FONT_COLOR, height=6)
        labelDir6.grid(row=3, column=0)


        def table_button_male(): # function for male button table
            top_table_male = Toplevel()

            class Table:

                def __init__(self, top_table_male):

                    # code for creating table
                    for i in range(total_rows):
                        for j in range(total_columns):
                            self.e = Entry(top_table_male, width=20, fg='black',
                                           font=SECONDARY_FONT)

                            self.e.grid(row=i, column=j)
                            self.e.insert(END, lst[i][j])


            #define all values
            # Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
            # Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)
            # take the data

            BMR_value = 88.362 + (13.387 * float(number2)) + (4.799 * float(number3)) - (5.677 * float(number1))
            value = BMR_value
            value_0 = BMR_value + (BMR_value*0.1) + 121
            value_1 = BMR_value + (BMR_value*0.1) + 428
            value_2 = BMR_value + (BMR_value*0.1) + 735
            value_3 = BMR_value + (BMR_value*0.1) + 1042
            value_4 = BMR_value + (BMR_value*0.1) + 1335

            lst = [('Basal Metabolic rate', round(BMR_value)),
                   ('Sedentary', round(value_0)),
                   ('Light Exercise', round(value_1)),
                   ('Moderate Exercise', round(value_2)),
                   ('Heavy exercise', round(value_3)),
                   ('Athlete', round(value_4))]

            total_rows = len(lst)
            total_columns = len(lst[0])

            t = Table(top_table_male)

        def table_button_female(): # function for female button table
            top_table_female = Toplevel()

            class Table:

                def __init__(self, top_table_female):

                    # code for creating table
                    for i in range(total_rows):
                        for j in range(total_columns):
                            self.e = Entry(top_table_female, width=20, fg='black',
                                           font=SECONDARY_FONT)

                            self.e.grid(row=i, column=j)
                            self.e.insert(END, lst[i][j])


            #define all values
            # Men: BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) – (5.677 x age in years)
            # Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) – (4.330 x age in years)
            # take the data

            BMR_value = 447.593 + (9.247 * float(number2)) + (3.098 * float(number3)) - (4.330 * float(number1))
            value = BMR_value
            value_0 = BMR_value + (BMR_value * 0.1) + 121
            value_1 = BMR_value + (BMR_value * 0.1) + 428
            value_2 = BMR_value + (BMR_value * 0.1) + 735
            value_3 = BMR_value + (BMR_value * 0.1) + 1042
            value_4 = BMR_value + (BMR_value * 0.1) + 1335

            lst = [('Basal Metabolic rate', round(BMR_value)),
                   ('Sedentary', round(value_0)),
                   ('Light Exercise', round(value_1)),
                   ('Moderate Exercise', round(value_2)),
                   ('Heavy exercise', round(value_3)),
                   ('Athlete', round(value_4))]

            total_rows = len(lst)
            total_columns = len(lst[0])

            t = Table(top_table_female)

        #Create a frame for the gender buttons
        Labelgroup_gender = LabelFrame(top_tdee,text = "Gender:",bg = WHITE,font = SECONDARY_FONT)
        Labelgroup_gender.grid(row = 5,column = 0,columnspan = 2)


        Table_button_me = Button(Labelgroup_gender, text="Click me if you are a\nMale!",
                              bg="CadetBlue", font=SECONDARY_FONT,
                                  command=table_button_male)
        Table_button_me.grid(row=1, column=0)
        Table_button_fe = Button(Labelgroup_gender, text="Click me if you are a\nFemale!",
                              bg="salmon", font=SECONDARY_FONT,
                              command=table_button_female)
        Table_button_fe.grid(row=1, column=2)

        p_break_image6 = PhotoImage(file=PAGE_BREAK)
        p_break6 = Label(top_tdee, image=p_break_image6, bg="#A2A5A1").grid(row=6, column=0, columnspan=3, sticky=NSEW)

        p_break_image7 = PhotoImage(file= "C:\\Users\\Ahmad Shreif\\PycharmProjects\\Health-stats-tool\\sourceii\\break3.PNG")
        p_break7 = Label(top_tdee, image=p_break_image7, bg="white").grid(row=7, column=0, columnspan=3, sticky=NSEW)

        def button_BMI_score():
            BMI_score = Toplevel()
            BMI_score.title('BMI Score')

            class Table:

                def __init__(self, BMI_score):

                    # code for creating table
                    for i in range(total_rows):
                        for j in range(total_columns):
                            self.e = Entry(BMI_score, width=20, fg='black',
                                           font=SECONDARY_FONT)

                            self.e.grid(row=i, column=j)
                            self.e.insert(END, lst[i][j])


            lst = [('Underweight', "18.5 or less"),
                   ('Normal Weight', "18.5 - 24.99"),
                   ('Overweight', "25 - 29.99"),
                   ('Obese', "30+")]

            total_rows = len(lst)
            total_columns = len(lst[0])

            t = Table(BMI_score)

        Labelgroup_BMI = LabelFrame(top_tdee, text="",borderwidth = 0, bg=WHITE, font=SECONDARY_FONT)
        Labelgroup_BMI.grid(row=8, column=0, columnspan=2)

        labelText7 = Label(Labelgroup_BMI,text=" Press the button below to check our verified BMI chart of underweight,"
                                " healthy, and obese values. ", font=SMALL_FONT_2, bg='white', fg=SMALL_FONT_COLOR)
        labelText7.grid(row=1, column=0)


        BMI_score_button = Button(Labelgroup_BMI, text="BMI Score", bg="dark orange", font=SECONDARY_FONT,
                                  command=button_BMI_score)
        BMI_score_button.grid(row=2, column=0)





    p_break_image5 = PhotoImage(file=PAGE_BREAK)
    p_break5 = Label(top_start, image=p_break_image5, bg="#A2A5A1").grid(row=14, column=0, columnspan=3, sticky=NSEW)

    Calculate_Button = Button(top_start,text = "Calculate!",bg = "DodgerBlue2",font = MAIN_FONT,command = proceed_button)
    Calculate_Button.grid(row = 15,column = 0)



def BMI_button():
    return
def macros_button():
    return


Frame_buttons = LabelFrame(root, text="Choose the desired option", bg=WHITE, font=SECONDARY_FONT)
Frame_buttons.grid(row=8, column=0)


login_btn_mac = PhotoImage(file = "C:\\Users\\Ahmad Shreif\\PycharmProjects\\Health-stats-tool\\sourceii\\macros.PNG")
img_label_mac = Label(image = login_btn_mac)
Macros_Button = Button(Frame_buttons,image = login_btn_mac, highlightthickness = 0, bd = 0, bg = 'gray38'
                       ,command = macros_button)
Macros_Button.grid(row =0,column = 0)

login_btn_bmi = PhotoImage(file = "C:\\Users\\Ahmad Shreif\\PycharmProjects\\Health-stats-tool\\sourceii\\bmi.PNG")
img_label_bmi = Label(image = login_btn_bmi)
BMI_button = Button(Frame_buttons,image = login_btn_bmi, highlightthickness = 0, bd = 0, bg = 'gray38',
                    command = BMI_button)
BMI_button.grid(row =0,column = 1)

login_btn_tdee = PhotoImage(file = "C:\\Users\\Ahmad Shreif\\PycharmProjects\\Health-stats-tool\\sourceii\\tdee.PNG")
img_label_tdee = Label(image = login_btn_tdee)
TDEE_button = Button(Frame_buttons,image = login_btn_tdee, highlightthickness = 0, bd = 0, bg = 'gray38',
                     command =TDEE_Button)
TDEE_button.grid(row =0,column = 2)




root.mainloop()