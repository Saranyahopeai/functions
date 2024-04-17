class assign():
   
    def Subfields():
        AI_list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")  
        for list in AI_list:
            print(list)

    Subfields()
    def OddEven():
        Num = int(input("Enter a number: "))
        if((Num%2)==0):
            print(Num," is Even number")
        else:
            print(Num," is Odd number")

    OddEven()
    def marriagelg():
        sex=input("Your Gender:")
        age=int(input("Your Age:"))

        if(sex=="Female"):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")

        elif(sex=="Male"):
            if(age>=21):
                print("Eligible")
            else:
                print("Not Eligible")    

    marriagelg()
    def percentage():
        # Subject marks
        S1 = 90
        S2 = 89
        S3 = 68
        S4 = 66
        S5 = 98

        #Marks scored
        total = S1 + S2 + S3 + S4 + S5

        # No of subjects
        totalsubjects = 5

        # percentage calculation
        percentage = (total / (totalsubjects * 100)) * 100

        print("Total :", total)
        print("Percentage :", percentage)

    percentage()    
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area of Triangle:",area)

        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter=height1+height2+breadth
        print("Perimeter of Triangle:",perimeter)

    triangle()
    

                