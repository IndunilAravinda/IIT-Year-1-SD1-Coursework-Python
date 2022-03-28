pc=0
dc=0
fc=0
state=""
progress=[]
trailer=[]
retriever=[]
allresults=["Progress","Trailer","Retriever","Excluded"]
excluded =[]
proceed =True
stage=""

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

while(proceed):
    while(True):
        try:
            pc = int(input("\nPlease enter your credit at pass : "))
            if pc%20 != 0 :
                print("Out of range")
                continue
            dc = int(input("Please enter your credit at defer : "))
            if dc%20 != 0 :
                print("Out of range")
                continue
            fc = int(input("Please enter your credit at fail : "))
            if fc%20 != 0 :
                print("Out of range")
                continue

            if (pc+dc+fc)!=120:
                print("Total incorrect")
                continue
            else:
                testresult()
                print(state)
                
                break
        except:
            print("Integer required")
            continue
    
    print("Would you like to enter another set of data?")
    stage=input("Enter 'y' for yes or 'q' to quit and view results: ")

    if stage=="y" or stage=="Y":
        proceed=True
    elif stage=="q" or stage=="Q":
        print("\n---------------------------\n")
        print("Horizontal Histogram\n")
        print("Progress",len(progress),":",progress)
        print("Trailer",len(trailer),":",trailer)
        print("Retriever",len(retriever),":",retriever)
        print("Excluded",len(excluded),":",excluded)

        print("\n")
        print(len(progress)+len(trailer)+len(retriever)+len(excluded), "outcomes in total.\n---------------------------")

        print("-------------------------\n")
        print("Vertical Histogram\n")

        vertidata=[["Progress",progress],["Trailer",trailer],["Retriever",retriever],["Excluded",excluded]]
        
        for i in vertidata:
            print(i[0])
            for x in i[1]:
                print(x)
    
        proceed=False

