pc=0
dc=0
fc=0
state=""
progress=[]
trailer=[]
retriever=[]

excluded =[]
proceed =True
stage=""

students=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

def testresult():
    if pc==120 and dc==0 and fc==0:
        print("Progress")
        state="Progress"
        
    elif pc==100 and dc==20 and fc==0:
        print("Progress (module trailer)")
        state="Progress (module trailer)"
        
    elif pc==100 and dc==0 and fc==20:
        print("Progress (module trailer)")
        state="Progress (module trailer)"
        
    elif pc==80 and dc==40 and fc==0:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==80 and dc==20 and fc==20:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==80 and dc==0 and fc==40:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==60 and dc==60 and fc==0:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==60 and dc==40 and fc==20:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==60 and dc==20 and fc==40:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==60 and dc==0 and fc==60:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==40 and dc==80 and fc==0:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==40 and dc==60 and fc==20:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==40 and dc==40 and fc==40:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==40 and dc==20 and fc==60:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==40 and dc==0 and fc==80:
        print("Exclude")
        state="Exclude"
        
    elif pc==20 and dc==100 and fc==0:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==20 and dc==80 and fc==20:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==20 and dc==60 and fc==40:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==20 and dc==40 and fc==60:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==20 and dc==20 and fc==80:
        print("Exclude")
        state="Exclude"
        
    elif pc==20 and dc==0 and fc==100:
        print("Exclude")
        state="Exclude"
        
    elif pc==0 and dc==120 and fc==0:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==0 and dc==100 and fc==20:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==0 and dc==80 and fc==40:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==0 and dc==60 and fc==60:
        print("Do not Progress – module retriever")
        state="Do not Progress – module retriever"
        
    elif pc==0 and dc==40 and fc==80:
        print("Exclude")
        state="Exclude"
        
    elif pc==0 and dc==20 and fc==100:
        print("Exclude")
        state="Exclude"
        
    elif pc==0 and dc==0 and fc==120:
        print("Exclude")
        state="Exclude"
        
    if state == "Progress":
        progress.append("*")
    elif state == "Progress (module trailer)":
        trailer.append("*")
    elif state == "Do not Progress – module retriever":
        retriever.append("*")
    elif state == "Exclude":
        excluded.append("*")

print("-------------------------\nStaff Version with Histogram")

try:
    for i in students:
        pc=i[0]
        if pc%20 != 0 :
            print("Out of range")
                    
        dc=i[1]
        if dc%20 != 0 :
            print("Out of range")
                    
        fc=i[2]
        if fc%20 != 0 :
            print("Out of range")
                    

        if (pc+dc+fc)!=120:
            print("Total incorrect")
                    
        else:
            testresult()
                    
    print("\n---------------------------\n")
    print("Horizontal Histogram\n")
    print("Progress",len(progress),":",progress)
    print("Trailer",len(trailer),":",trailer)
    print("Retriever",len(retriever),":",retriever)
    print("Excluded",len(excluded),":",excluded)

    print("\n")
    print(len(progress)+len(trailer)+len(retriever)+len(excluded), "outcomes in total.\n---------------------------")
except:
    print("Integer required")

        


