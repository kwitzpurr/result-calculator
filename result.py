from tkinter import *
import sqlite3
root = Tk()


# Title
root.title('Student Result Management System')

# Window size
root.geometry('600x300')

# Create a databse connection
conn = sqlite3.connect("results.db")

#Create cursor
c = conn.cursor()

# Create table
'''c.execute("""create table marks(
  name text,
  class varchar,
  roll_no integer,
  eng real,
  dzo real,
  math real,
  science real,
  hcg real
  )""")'''

def add():
  conn = sqlite3.connect("results.db")
  c = conn.cursor()

  # Insert into table
  c.execute("INSERT INTO marks values(:name,:class,:roll_no,:eng, :dzo,:math,:science,:hcg)",
            {
              "name": name.get(),
              "class": std_class.get(),
              "roll_no": roll_no.get(),
              "eng": eng.get(),
              "dzo": dzo.get(),
              "math" : math.get(),
              "science": sci.get(),
              "hcg": hcg.get()})
  conn.commit()
  conn.close()

  

def calculate():
  conn = sqlite3.connect("results.db")
  c = conn.cursor()
  # to query the database
  c.execute("SELECT * FROM marks WHERE roll_no="+roll_no.get())
  records = c.fetchall()
  for record in records:
    eng = record[3]
    dzo = record[4]
    math = record[5]
    sci = record[6]
    hcg= record[7]
  tot = eng + dzo + math + sci +hcg
  avg = tot/5
    
  per.insert(0,avg)

  count = 0
  minor = [math, sci, hcg]

  # Condition to determine pass or fail
  if eng >= 40 and dzo >=40:
    for i in minor:
      if i < 40:
        count+=1
    if count == 0 or count == 1:
      r = "Pass"
      rem.insert(0,r)
    else:
      r = "Fail"
      rem.insert(0,r)     
    
  else:
    r = "Fail"
    rem.insert(0,r)
    
    
  conn.commit()
  conn.close()

# Function to view result
def view1():
  #Clear text boxes
  name.delete(0,END)
  std_class.delete(0,END)
  roll_no.delete(0,END)
  eng.delete(0,END)
  dzo.delete(0,END)
  math.delete(0,END)
  sci.delete(0,END)
  hcg.delete(0,END)
  per.delete(0,END)
  rem.delete(0,END)
  conn = sqlite3.connect("results.db")
  c = conn.cursor()
  # to query the database
  #roll = roll_no.get()
  c.execute("SELECT * FROM marks WHERE roll_no="+view.get())
  records = c.fetchall()
  for record in records:    
    name.insert(0,record[0])
    std_class.insert(0,record[1])
    roll_no.insert(0,record[2])
    eng.insert(0,record[3])
    dzo.insert(0,record[4])
    math.insert(0,record[5])
    sci.insert(0,record[6])
    hcg.insert(0,record[7])
  
  
  conn.commit()
  conn.close()
  
# declaring objects for entering data 
name = Entry(root) 
std_class = Entry(root) 
roll_no = Entry(root) 
eng = Entry(root) 
dzo = Entry(root) 
math = Entry(root) 
sci = Entry(root)
hcg = Entry(root)
per = Entry(root)
rem = Entry(root)

# Function to add records to database
# label for name 
Label(root, text="Name").grid(row=0, column=0) 

# label for class 
Label(root, text="Class").grid(row=0, column=2) 

# label for roll Number 
Label(root, text="Roll No").grid(row=1, column=0) 


# labels for serial numbers 
Label(root, text="Sl.No").grid(row=2, column=0,pady=20) 
Label(root, text="1").grid(row=3, column=0) 
Label(root, text="2").grid(row=4, column=0) 
Label(root, text="3").grid(row=5, column=0) 
Label(root, text="4").grid(row=6, column=0)
Label(root, text="5").grid(row=7, column=0)


# labels for subjects 
Label(root, text="Subject").grid(row=2, column=1) 
Label(root, text="English").grid(row=3, column=1) 
Label(root, text="Dzongkha").grid(row=4, column=1) 
Label(root, text="Maths").grid(row=5, column=1) 
Label(root, text="Science").grid(row=6, column=1)
Label(root, text="HCG").grid(row=7, column=1) 

	
# label for marks 
Label(root, text="Marks").grid(row=2, column=2) 
eng.grid(row=3, column=2) 
dzo.grid(row=4, column=2) 
math.grid(row=5, column=2) 
sci.grid(row=6, column=2)
hcg.grid(row=7, column=2)

#Button to calculate percentage and remarks
button2 = Button(root, text = "Calculate", bg="silver",command = calculate)
button2.grid(row=3,column=3,ipadx=20,columnspan=2)

# labels for percentage and remarks 
Label(root, text="Percentage").grid(row=5, column=3) 
Label(root, text="Remarks").grid(row=5, column=4)

# Entries for percentage and remarks
per = Entry(root,width=10)
rem = Entry(root,width=10)
per.grid(row=6,column=3,ipadx = 0.5)
rem.grid(row=6,column=4)

# Entries for name, class and roll number
name = Entry(root) 
std_class = Entry(root)
roll_no = Entry(root) 

# organizing name,class and roll no in the grid 
name.grid(row=0, column=1,padx=10,pady=10) 
std_class.grid(row=0, column=3) 
roll_no.grid(row=1, column=1) 


# button to add record into database
button1=Button(root, text="Save", bg="silver",command = add) 
button1.grid(row=8, column=1,ipadx=20,pady=10)


# View Result
Label(root,text="Search by Roll No").grid(row=8, column=2)

view = Entry(root, width = 15)
view.grid(row = 8, column =3,ipady=3)
button3 = Button(root,text= "Search", bg="silver",command= view1)
button3.grid(row=8, column=4,ipadx=20)

conn.commit()
conn.close()


	
root.mainloop() 

