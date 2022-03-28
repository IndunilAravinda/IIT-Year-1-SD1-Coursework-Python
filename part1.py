pc = int(input("Please enter your credit at pass : "))
dc = int(input("Please enter your credit at defer : "))
fc = int(input("Please enter your credit at fail : "))

if pc==120 and dc==0 and fc==0:
    print("Progress")
elif pc==100 and dc==20 and fc==0:
    print("Progress (module trailer)")
elif pc==100 and dc==0 and fc==20:
    print("Progress (module trailer)")
elif pc==80 and dc==40 and fc==0:
    print("Do not Progress – module retriever")
elif pc==80 and dc==20 and fc==20:
    print("Do not Progress – module retriever")
elif pc==80 and dc==0 and fc==40:
    print("Do not Progress – module retriever")
elif pc==60 and dc==60 and fc==0:
    print("Do not Progress – module retriever")
elif pc==60 and dc==40 and fc==20:
    print("Do not Progress – module retriever")
elif pc==60 and dc==20 and fc==40:
    print("Do not Progress – module retriever")
elif pc==60 and dc==0 and fc==60:
    print("Do not Progress – module retriever")
elif pc==40 and dc==80 and fc==0:
    print("Do not Progress – module retriever")
elif pc==40 and dc==60 and fc==20:
    print("Do not Progress – module retriever")
elif pc==40 and dc==40 and fc==40:
    print("Do not Progress – module retriever")
elif pc==40 and dc==20 and fc==60:
    print("Do not Progress – module retriever")
elif pc==40 and dc==0 and fc==80:
    print("Exclude")
elif pc==20 and dc==100 and fc==0:
    print("Do not Progress – module retriever")
elif pc==20 and dc==80 and fc==20:
    print("Do not Progress – module retriever")
elif pc==20 and dc==60 and fc==40:
    print("Do not Progress – module retriever")
elif pc==20 and dc==40 and fc==60:
    print("Do not Progress – module retriever")
elif pc==20 and dc==20 and fc==80:
    print("Exclude")
elif pc==20 and dc==0 and fc==100:
    print("Exclude")
elif pc==0 and dc==120 and fc==0:
    print("Do not Progress – module retriever")
elif pc==0 and dc==100 and fc==20:
    print("Do not Progress – module retriever")
elif pc==0 and dc==80 and fc==40:
    print("Do not Progress – module retriever")
elif pc==0 and dc==60 and fc==60:
    print("Do not Progress – module retriever")
elif pc==0 and dc==40 and fc==80:
    print("Exclude")
elif pc==0 and dc==20 and fc==100:
    print("Exclude")
elif pc==0 and dc==0 and fc==120:
    print("Exclude")
