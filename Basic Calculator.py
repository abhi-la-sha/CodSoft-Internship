def calc():
    print("\t\t\t*******BASIC CALCULATOR*******")
    n1= int(input("Enter the 1st number:"))
    n2= int(input("Enter the 2nd number:"))
    print("********************************************")
    print("\nSelect the operation you want to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponential (**)")

    op=int(input("Enter the corresponding no."))

    if op==1:
       result=n1+n2
    elif op==2:
       result=n1-n2
    elif op==3:
       result=n1*n2
    elif op==4:
       result=n1/n2
    elif op==5:
       result=n1**n2
    else:
       print("Invalid input!")
    print("The result is:", result)

    nxt=input("Want to do another calculation? (Y/N):")
    if nxt.upper()=='Y':
        calc()
    elif nxt.upper()=='N':
        pass
    else:
        print("Invalid input!")

calc()
