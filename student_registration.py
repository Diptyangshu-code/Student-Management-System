import os

class check:
        def eligibility(s):
                print(" Select the caste of the student \n")
                print("1. ST (Schedule Tribe) \n")
                print("2. SC (Schedule Caste) \n")
                print("3. OBC (Other Backword Classes \n ")
                print("4. General \n")
                print("0. EXIT \n")
                c=int(input(" Enter your choice : "))

                if(c==1):
                        print("\n Enter marks of Higher Secondary \n")
                        y1=int(input(" English : "))
                        print("\n")
                        y2=int(input(" Mathematics : "))
                        print("\n")
                        y3=int(input(" Physics : "))
                        print("\n")
                        y4=int(input(" Chemistry : "))
                        print("\n")
                        y5=int(input(" Computer Science : "))
                        print("\n")
                        y6=int(input(" Biology : "))
                        print("\n")
                        y7=int(input(" Physical Education : "))
                        print("\n")
                        y8=int(input(" Alternative English : "))

                        a=list()

                        a.append(y1)
                        a.append(y2)
                        a.append(y3)
                        a.append(y4)
                        a.append(y5)
                        a.append(y6)
                        a.append(y7)
                        a.append(y8)

                        a.sort()

                        a.reverse()


                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                        
                        c7="45000"
                        

                        if(c6>=225):
                        
                                print("\n Student is eligible for admission \n")
                                print("Fees- Rs",c7)
                        
                        else:
                                
                                print(" Sorry !! Student is not eligible for Admission \n")
                                


                
                elif(c==2):
                
                        print("\n Enter marks of Higher Secondary \n")
                        y1=int(input(" English : "))
                        print("\n")
                        y2=int(input(" Mathematics : "))
                        print("\n")
                        y3=int(input(" Physics : "))
                        print("\n")
                        y4=int(input(" Chemistry : "))
                        print("\n")
                        y5=int(input(" Computer Science : "))
                        print("\n")
                        y6=int(input(" Biology : "))
                        print("\n")
                        y7=int(input(" Physical Education : "))
                        print("\n")
                        y8=int(input(" Alternative English : "))

                        a=list()

                        a.append(y1)
                        a.append(y2)
                        a.append(y3)
                        a.append(y4)
                        a.append(y5)
                        a.append(y6)
                        a.append(y7)
                        a.append(y8)

                        a.sort()

                        a.reverse()


                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                        c7="45000"

                        if(c6>=225):
                        
                                print("Student is eligible for admission \n")
                                print("Fees- Rs",c7)
                        
                        else:
                                
                                print(" Sorry !! Student is not eligible for Admission \n")
                                


                        

                elif(c==3):
                
                        print(" \nEnter marks of Higher Secondary \n")
                        y1=int(input(" English : "))
                        print("\n")
                        y2=int(input(" Mathematics : "))
                        print("\n")
                        y3=int(input(" Physics : "))
                        print("\n")
                        y4=int(input(" Chemistry : "))
                        print("\n")
                        y5=int(input(" Computer Science : "))
                        print("\n")
                        y6=int(input(" Biology : "))
                        print("\n")
                        y7=int(input(" Physical Education : "))
                        print("\n")
                        y8=int(input(" Alternative English : "))

                        a=list()

                        a.append(y1)
                        a.append(y2)
                        a.append(y3)
                        a.append(y4)
                        a.append(y5)
                        a.append(y6)
                        a.append(y7)
                        a.append(y8)

                        a.sort()

                        a.reverse()


                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                        c7="54000"

                        if(c6>=275):
                        
                                print("Student is eligible for admission \n")
                                print("Fees- Rs",c7)
                        
                        else:
                                
                                print(" Sorry !! Student is not eligible for Admission \n")
                                


                
                elif(c==4):
                
                        print("\n Enter marks of Higher Secondary \n")
                        y1=int(input(" English : "))
                        print("\n")
                        y2=int(input(" Mathematics : "))
                        print("\n")
                        y3=int(input(" Physics : "))
                        print("\n")
                        y4=int(input(" Chemistry : "))
                        print("\n")
                        y5=int(input(" Computer Science : "))
                        print("\n")
                        y6=int(input(" Biology : "))
                        print("\n")
                        y7=int(input(" Physical Education : "))
                        print("\n")
                        y8=int(input(" Alternative English : "))

                        a=list()

                        a.append(y1)
                        a.append(y2)
                        a.append(y3)
                        a.append(y4)
                        a.append(y5)
                        a.append(y6)
                        a.append(y7)
                        a.append(y8)

                        a.sort()

                        a.reverse()


                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                        c7="65000"

                        if(c6>=300):
                        
                                print("Student is eligible for admission \n")
                                print("Fees- Rs",c7)
                        
                        else:
                                
                                print(" Sorry !! Student is not eligible for Admission \n")

                elif(c==0):
                        exit(0)

                else:
                        print("\n !!! Enter correct option !!!\n")
                               
                                



class student:
        def registration(s):
                

                

                        a=input(" Enter student's First Name : ")
                        print("\n")

                        b=input(" Enter student's Last Name : ")
                        print("\n")

                        c=input(" Enter student's Address : ")
                        print("\n")

                        d=input(" Enter student's  Contact-Number : ")
                        print("\n")

                        e=input(" Have the student paid the bill ? y/n ")

                        if(e=='y'):
                                pay="paid full"
                                pay1= "00.00"
                        elif(e=='n'):
                                pay="unpaid"

                                s=int(input(" Enter the amount student paid ? "))
                                w=c8-s
                                q=str(w)
                                
                                pay1=q
                                
                                
                                

                        abc=open(a+".txt","x")
                        abc=open(a+".txt","w")
                        abc.write("-----------------------------------------------------------******----CENTRAL INSTITUTE OF TECHNOLOGY, KOKRAJHAR----******--------------------------------------------------------------------------------")
                        abc.write("\n")
                        abc.write("----------------------------------------------------------(A Centrally Funded Institute under ministry of HRD, Govt.of India)-------------------------------------------------------------------------------")
                        abc.write("\n")
                        abc.write("---------------------------------------------------------------------Kokrajhar, BTAD, Assam, India, PIN-783370---------------------------------------------------------------------------------------------------")
                        abc.write("\n")
                        abc.write("\n")
                        abc.write("\n")
                        abc.write("----------------------------------------------------------------------******----Student's Registration-----*****--------------------------------------------------------------------")
                        abc.write("\n")
                        abc.write("\n")


                        abc.write("First Name : "+a)
                        abc.write("\n")
                        abc.write("Last Name : "+b)
                        abc.write("\n")
                        abc.write("Address : "+c)
                        abc.write("\n")
                        abc.write("Contact-Number : "+d)
                        abc.write("\n")
                        abc.write(" Branch : "+branch)
                        abc.write("\n")
                        abc.write("Elective : "+e1)
                        abc.write("\n")
                        abc.write("Payment Status- Rs : "+pay)
                        abc.write("\n")
                        abc.write("Due Amount - Rs : "+pay1)
                        abc.write("\n\n")
                        abc.write("\n")
                        abc.write("\n")
                        abc.write("-------------------------------------------------------------------------------------THANK YOU--------------------------------------------------------------------------------------------------------------------------------")
                        

                        abc.close()

                        billing=open(a+"_bill.txt","x")
                        billing=open(a+"_bill.txt","w")
                        billing.write("---------------------------------------------------********--CENTRAL INSTITUTE OF TECHNOLOGY, KOKRAJHAR--********---------------------------------------------------------------------------------------")
                        billing.write("\n")
                        billing.write("-------------------------------------------------(A Centrally Funded Institute under ministry of HRD, Govt.of India)----------------------------------------------------------------------------")
                        billing.write("\n")
                        billing.write("------------------------------------------------------------Kokrajhar, BTAD, Assam, India, PIN-783370------------------------------------------------------------------------------------------")
                        billing.write("\n")
                        billing.write("\n")
                        billing.write("\n")
                        billing.write("-----------------------------------------------------------------****---Student's Billing---****-----------------------------------------------------------------------------------------")
                        billing.write("\n")
                        billing.write("\n")


                        billing.write("First Name : "+a)
                        billing.write("\n")
                        billing.write("Last Name : "+b)
                        billing.write("\n")
                        billing.write("Address : "+c)
                        billing.write("\n")
                        billing.write("Contact-Number : "+d)
                        billing.write("\n")
                        billing.write("Branch : "+branch)
                        billing.write("\n")
                        billing.write("Elective : "+e1)
                        billing.write("\n")
                        billing.write("Total Amount : "+c7)
                        billing.write("\n")
                        billing.write(" Payment Status - Rs : "+pay)
                        billing.write("\n")
                        billing.write("Due Amount - Rs : "+pay1)
                        billing.write("\n")
                        billing.write("\n")
                        billing.write("\n")
                        billing.write("\n")
                        billing.write("-------------------------------------------------------------------------------THANK YOU------------------------------------------------------------------------------------------")                        
                        billing.close()
                        billing=open(a+"_bill.txt","r")
                        print(billing.read())

                        

                        
                

        def search(s):

                s1=input("Type student's name to search : ")
                if(os.path.exists(s1+".txt")):
                        
                        print(s1, " is a registered student ")
                        print("\n")
                        print(" Do you want to view the details of ",s1," ? y/n")
                        s2=input()
                        print("\n")
                        if(s2=='y'):
                                
                                abc=open(s1+".txt","r")

                                print(abc.read())
                                
                        else:
                                
                                print(" Thank You ")
                                
                        

                else:
                        
                        print(" No student is registered by ",s1)
                        

                        print("\n Thank You \n")


        def search_bill(s):

                s1=input("Type student's name to search : ")
                if(os.path.exists(s1+"_bill.txt")):
                        
                        print(s1, " is a registered student ")
                        print("\n")
                        print(" Do you want to view the bill of ",s1," ? y/n")
                        s2=input()
                        print("\n")
                        if(s2=='y'):
                                
                                billing=open(s1+"_bill.txt","r")

                                print(billing.read())
                                
                        else:
                                
                                print(" Thank You ")
                                
                        

                else:
                        
                        print(" No student is registered by ",s1)
                        

                        print("\n Thank You \n")
                                




print("\n")
print("\n")
print("-----------------------------------------------------------------CENTRAL INSTITUTE OF TECHNOLOGY, KOKRAJHAR----------------------------------------------------------------------------------------------")
print("----------------------------------------------------(A Centrally Funded Institute under ministry of HRD, Govt. of India)---------------------------------------------------------------------------------")
print("-----------------------------------------------------------------Kokrajhar, BTAD, Assam, India, PIN-783370------------------------------------------------------------------------------------------------")
print("\n")
print("\n")
print("------------------------------------------------------------------Welcome to Student's Registration System--------------------------------------------------------------------------------------------")
print("\n")
print("\n")
obj1=student()
obj2=check()

f=0



while(1):
        print(" Select Your Option from below : \n")
        print(" 1. Registration \n")
        print(" 2. Search Student Info \n")
        print(" 3.Eligibility \n")
        print(" 4. Search bill of students \n")
        print(" 0. EXIT \n ")

        s3=int(input(" Enter your choice : "))

        print("\n")
        if(s3==1):
                while(1):
                

                        print(" Which Department Student want to take admission in ? ")
                        print("\n")
                        print(" 1. Computer Science Engineering ")
                        print(" 2. Electrical Engineering ")
                        print(" 3. Mechanical Engineering ")
                        print(" 4. BACK TO PREVIOUS OPTIONS ")
                        print(" 0. EXIT \n")
                        print("\n")
                        s4=int(input(" Enter your choice : "))

                        if(s4==1):
                                print("Enter total number of seats allocation for B.Tech of Computer Science : ")
                                seats=int(input())
                                for i in range(0,seats):
                                        if(f<=seats):
                                                print(" Select the caste of the student \n ")
                                                print("1. ST (Schedule Tribe) \n ")
                                                print("2. SC (Schedule Caste) \n ")
                                                print("3. OBC (Other Backword Classes) \n ")
                                                print("4. General(Unreserved) \n ")
                                                print("5. BACK TO PREVIOUS OPTIONS \n")
                                                print("0. EXIT \n")
                                                c=int(input())
                                                if(c==1):
                                
                                                        print("\n Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        
                                                        if(c6>=225):
                                        
                                                                print("\nStudent is eligible for admission \n")
                                                                c7="45000"
                                                                c8=45000
                                                                print("Select Elective from below : ")
                                                                print("1.Cyber Security Majors \n")
                                                                print("2.Internet of things (IOT) \n ")
                                                                print("3. Robotics \n")
                                                                print("4. BACK TO PREVIOUS OPTIONS \n")
                                                                print("0. EXIT \n")
                                                                e=int(input(" Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Cyber Security Majors"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Internet of things (IOT)"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Robotics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print("\n !!! Enter correct input !!! \n")
                                                                        break
                                                                
                                                        
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                


                                
                                                elif(c==2):
                                
                                                        print(" \nEnter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]




                                                        c7="45000"
                                                        c8=45000

                                                        if(c6>=225):
                                        
                                                                print("\nStudent is eligible for admission \n")
                                                                c7="45000"
                                                                c8=45000
                                                                print("Select Elective from below : ")
                                                                print("1. Cyber Security Majors \n")
                                                                print("2. Internet of things (IOT) \n ")
                                                                print("3. Robotics \n")
                                                                print("4. BACK TO PREVIOUS OPTIONS \n")
                                                                print("0. EXIT \n")
                                                                e=int(input(" Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Cyber Security Majors"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Internet of things (IOT)"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Robotics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")

                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print("\n !!! Enter correct option !!!\n ")
                                                                        break
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                


                                        

                                                elif(c==3):
                                
                                                                print("\n Enter marks of Higher Secondary \n")
                                                                y1=int(input(" English : "))
                                                                print("\n")
                                                                y2=int(input(" Mathematics : "))
                                                                print("\n")
                                                                y3=int(input(" Physics : "))
                                                                print("\n")
                                                                y4=int(input(" Chemistry : "))
                                                                print("\n")
                                                                y5=int(input(" Computer Science : "))
                                                                print("\n")
                                                                y6=int(input(" Biology : "))
                                                                print("\n")
                                                                y7=int(input(" Physical Education : "))
                                                                print("\n")
                                                                y8=int(input(" Alternative English : "))

                                                                a=list()

                                                                a.append(y1)
                                                                a.append(y2)
                                                                a.append(y3)
                                                                a.append(y4)
                                                                a.append(y5)
                                                                a.append(y6)
                                                                a.append(y7)
                                                                a.append(y8)

                                                                a.sort()

                                                                a.reverse()


                                                                c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                                c7="54000"

                                                                if(c6>=275):
                                                
                                                                        print("Student is eligible for admission \n")
                                                                        c7="54000"
                                                                        c8=54000
                                                                        print("Select Elective from below : ")
                                                                        print("1. Cyber Security Majors \n")
                                                                        print("2. Internet of things (IOT) \n ")
                                                                        print("3. Robotics \n")
                                                                        print("4. BACK TO PREVIOUS OPTIONS \n")
                                                                        print("0. EXIT \n")
                                                                        e=int(input(" Enter your choice : "))
                                                                        if(e==1):
                                                                                branch=" Computer Science Engineering "
                                                                                e1="Cyber Security Majors"
                                                                        
                                                                                obj1.registration()
                                                                                f+=1
                                                                                print(f," seats are filled up out of ",seats)
                                                                                print("\n")
                                                                        
                                                                        elif(e==2):
                                                                                branch=" Computer Science Engineering "
                                                                                e1="Internet of things (IOT)"
                                                                       
                                                                                obj1.registration()
                                                                                f+=1
                                                                                print(f," seats are filled up out of ",seats)
                                                                                print("\n")
                                                                        
                                                                        elif(e==3):
                                                                                branch=" Computer Science Engineering "
                                                                                e1="Robotics"
                                                                        
                                                                                obj1.registration()
                                                                                f+=1
                                                                                print(f," seats are filled up out of ",seats)
                                                                                print("\n")

                                                                        elif(e==4):
                                                                                break
                                                                        elif(e==0):
                                                                                exit(0)

                                                                        else:
                                                                                print(" \n !!! Enter correct option !!!\n ")
                                                                                break
                                                                
                                                
                                                                else:
                                                        
                                                                        print(" Sorry !! Student is not eligible for Admission \n")
                                                                        break
                                                                


                                
                                                elif(c==4):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        
                                                        c7="65000"

                                                        if(c6>=300):
                                        
                                                                print("\nStudent is eligible for admission \n")
                                                                c7="65000"
                                                                c8=65000
                                                                print("Select Elective from below : ")
                                                                print("1.Cyber Security Majors \n")
                                                                print("2.Internet of things (IOT) \n ")
                                                                print("3. Robotics \n")
                                                                print("4. BACK TO PREVIOUS OPTIONS \n")
                                                                print("0. EXIT \n")
                                                                e=int(input("Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Cyber Security Majors"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Internet of things (IOT)"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Computer Science Engineering "
                                                                        e1="Robotics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)

                                                                else:
                                                                        print("\n !!! Enter correct option !!!\n")
                                                                        break
                                                                
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                elif(c==5):
                                                        break


                                                elif(c==0):
                                                        exit(0)
                                                else:
                                                        print(" \n!!! Enter correct option !!! \n")
                                                        break


                        elif(s4==2):
                                print("Enter total number of seats allocation for B.Tech of Electrical Engineering : ")
                                seats=int(input())
                                for i in range(0,seats):
                                        if(f<=seats):
                                                print(" Select the caste of the student \n ")
                                                print("1. ST (Schedule Tribe) \n ")
                                                print("2. SC (Schedule Caste) \n ")
                                                print("3. OBC (Other Backword Classes) \n ")
                                                print("4. General(Unreserved) \n ")
                                                print("5.BACK TO PREVIOUS OPTIONS \n")
                                                print("0. EXIT \n")
                                                c=int(input(" Enter your choice : "))
                                                if(c==1):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]



                                                        
                                                        if(c6>=225):
                                        
                                                                print("\nStudent is eligible for admission \n")
                                                                c7="45000"
                                                                c8=45000
                                                                print("Select Elective from below : ")
                                                                print("1.Environmental Studies \n")
                                                                print("2.Computer Programming \n ")
                                                                print("3.Design Thinking \n")
                                                                print("4. BACK TO PREVIOUS OPTIONS \n")
                                                                print("0. EXIT \n")
                                                                e=int(input("Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Electrical Engineering "
                                                                        
                                                                        e1="Environmental Studies"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Computer Programming"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Design Thinking"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")

                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print(" \n!!! Enter correct option  !!!\n")
                                                                        break
                                                        
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                


                                
                                                elif(c==2):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        c7="45000"
                                                        c8=45000

                                                        if(c6>=225):
                                        
                                                                print("Student is eligible for admission \n")
                                                                c7="45000"
                                                                c8=45000
                                                                print("Select Elective from below : ")
                                                                print("1.Environmental Studies \n")
                                                                print("2.Computer Programming \n ")
                                                                print("3.Design Thinking \n")
                                                                print("4.BACK TO PREVIOUS OPTIONS \n ")
                                                                print("0. EXIT \n")
                                                                e=int(input(" Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Environmental Studies"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                elif(e==2):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Computer Programming"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                elif(e==3):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Design Thinking"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)

                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print("\n !!! Enter correct option !!! \n")
                                                                        break
                                                        
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                


                                        

                                                elif(c==3):
                                
                                                                print("\n Enter marks of Higher Secondary \n")
                                                                y1=int(input(" English : "))
                                                                print("\n")
                                                                y2=int(input(" Mathematics : "))
                                                                print("\n")
                                                                y3=int(input(" Physics : "))
                                                                print("\n")
                                                                y4=int(input(" Chemistry : "))
                                                                print("\n")
                                                                y5=int(input(" Computer Science : "))
                                                                print("\n")
                                                                y6=int(input(" Biology : "))
                                                                print("\n")
                                                                y7=int(input(" Physical Education : "))
                                                                print("\n")
                                                                y8=int(input(" Alternative English : "))

                                                                a=list()

                                                                a.append(y1)
                                                                a.append(y2)
                                                                a.append(y3)
                                                                a.append(y4)
                                                                a.append(y5)
                                                                a.append(y6)
                                                                a.append(y7)
                                                                a.append(y8)

                                                                a.sort()

                                                                a.reverse()


                                                                c6=a[0]+a[1]+a[2]+a[3]+a[4]



                                                                
                                                                c7="54000"

                                                                if(c6>=275):
                                        
                                                                        print("\nStudent is eligible for admission \n")
                                                                        c7="54000"
                                                                        c8=54000
                                                                        print("Select Elective from below : ")
                                                                        print("1.Environmental Studies \n")
                                                                        print("2.Computer Programming \n ")
                                                                        print("3.Design Thinking \n")
                                                                        print("4.BACK TO PREVIOUS OPTIONS \n")
                                                                        print("0. EXIT \n")
                                                                        e=int(input("Enter your choice : "))
                                                                        if(e==1):
                                                                                branch=" Electrical Engineering "
                                                                                e1="Environmental Studies"
                                                                
                                                                                obj1.registration()
                                                                                f+=1
                                                                                print(f," seats are filled up out of ",seats)
                                                                                print("\n")
                                                                
                                                                        elif(e==2):
                                                                                branch=" Electrical Engineering "
                                                                                e1="Computer Programming"
                                                               
                                                                                obj1.registration()
                                                                                f+=1
                                                                                print(f," seats are filled up out of ",seats)
                                                                                print("\n")
                                                                
                                                                        elif(e==3):
                                                                                branch=" Electrical Engineering "
                                                                                e1="Design Thinking"
                                                                
                                                                                obj1.registration()
                                                                                f+=1
                                                                                print(f," seats are filled up out of ",seats)
                                                                                print("\n")

                                                                        elif(e==4):
                                                                                break
                                                                        elif(e==0):
                                                                                exit(0)
                                                                        else:
                                                                              print("\n !!! Enter correct choice !!!\n")
                                                                              break
                                                                                
                                                        
                                        
                                                                else:
                                                
                                                                        print(" Sorry !! Student is not eligible for Admission \n")
                                                                        break
                                                        


                                
                                                elif(c==4):
                                
                                                        print(" \nEnter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        c7="65000"

                                                        if(c6>=300):
                                        
                                                                print("\n Student is eligible for admission \n")
                                                                c7="65000"
                                                                c8=65000
                                                                print("Select Elective from below : ")
                                                                print("1.Environmental Studies \n")
                                                                print("2.Computer Programming \n ")
                                                                print("3.Design Thinking \n")
                                                                print("4. BACK TO PREVIOUS OPTIONS \n")
                                                                print("0. EXIT \n")
                                                                e=int(input(" Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Environmental Studies"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                elif(e==2):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Computer Programming"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                elif(e==3):
                                                                        branch=" Electrical Engineering "
                                                                        e1="Design Thinking"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                elif(e==4):
                                                                        break

                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print("\n !!! Enter correct option!!! \n ")
                                                                        break
                                                                
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break


                                                elif(c==5):
                                                        break
                                                elif(c==0):
                                                        exit(0)
                                                else:
                                                        print(" \n!!! Enter correct option !!!\n")
                                                        break



                        elif(s4==3):
                                print("Enter total number of seats allocation for B.Tech of Mechanical Engineering : ")
                                seats=int(input(" Enter number of seats : "))
                                
                                
                                for i in range(0,seats):
                                        if(f<=seats):
                                                print(" Select the caste of the student \n ")
                                                print("1. ST (Schedule Tribe) \n ")
                                                print("2. SC (Schedule Caste) \n ")
                                                print("3. OBC (Other Backword Classes) \n ")
                                                print("4. General(Unreserved) \n ")
                                                print("5.BACK TO PREVIOUS OPTIONS \n ")
                                                print("0. EXIT \n")
                                                c=int(input(" Enter your choice : "))
                                                if(c==1):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]



                                                        
                                                        if(c6>=225):
                                        
                                                                print("\nStudent is eligible for admission \n")
                                                                c7="45000"
                                                                c8=45000
                                                                print("Select Elective from below : ")
                                                                print("1.Robotics \n")
                                                                print("2.Intermediate Fluid Mechanics \n ")
                                                                print("3.Computer Aided Design and Manufacturing \n")
                                                                print("4.BACK TO PREVIOUS OPTIONS\n")
                                                                print("0. EXIT \n")
                                                                e=int(input(" Enter your choice "))
                                                                if(e==1):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Robotics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Intermediate Fluid Mechanics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Computer Aided Design and Manufacturing "
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==0):
                                                                        exit(0)
                                                                elif(e==4):
                                                                        break
                                                                else:
                                                                        print("\n !!! Enter correct option !!!\n ")
                                                                        break
                                                        
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                


                                
                                                elif(c==2):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        c7="45000"
                                                        c8=45000

                                                        if(c6>=225):
                                        
                                                                print("Student is eligible for admission \n")
                                                                c7="45000"
                                                                c8=45000
                                                                print("Select Elective from below : ")
                                                                print("1.Robotics \n")
                                                                print("2.Intermediate Fluid Mechanics \n ")
                                                                print("3.Computer Aided Design and Manufacturing \n")
                                                                print("4.BACK TO PREVIOUS OPTIONS\n")
                                                                print("0. EXIT \n")
                                                                e=int(input(" Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Robotics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Intermediate Fluid Mechanics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Computer Aided Design and Manufacturing"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print("\n !!! Enter correct option !!! \n")
                                                                        break
                                                        
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                


                                        

                                                elif(c==3):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        c7="54000"

                                                        if(c6>=275):
                                        
                                                                print("Student is eligible for admission \n")
                                                                c7="54000"
                                                                c8=54000
                                                                print("Select Elective from below : ")
                                                                print("1.Robotics \n")
                                                                print("2.Intermediate Fluid Mechanics \n ")
                                                                print("3.Computer Aided Design and Manufacturing \n")
                                                                print("4.BACK TO PREVIOUS OPTIONS\n")
                                                                print("0. EXIT \n")
                                                                e=int(input("Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Robotics"
                                                                
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                
                                                                elif(e==2):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Intermediate Fluid Mechanics"
                                                               
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                
                                                                elif(e==3):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Computer Aided Design and Manufacturing"
                                                                
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")

                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print(" \n !!! Enter correct option !!! \n ")
                                                        
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break
                                                        


                                
                                                elif(c==4):
                                
                                                        print(" Enter marks of Higher Secondary \n")
                                                        y1=int(input(" English : "))
                                                        print("\n")
                                                        y2=int(input(" Mathematics : "))
                                                        print("\n")
                                                        y3=int(input(" Physics : "))
                                                        print("\n")
                                                        y4=int(input(" Chemistry : "))
                                                        print("\n")
                                                        y5=int(input(" Computer Science : "))
                                                        print("\n")
                                                        y6=int(input(" Biology : "))
                                                        print("\n")
                                                        y7=int(input(" Physical Education : "))
                                                        print("\n")
                                                        y8=int(input(" Alternative English : "))

                                                        a=list()

                                                        a.append(y1)
                                                        a.append(y2)
                                                        a.append(y3)
                                                        a.append(y4)
                                                        a.append(y5)
                                                        a.append(y6)
                                                        a.append(y7)
                                                        a.append(y8)

                                                        a.sort()

                                                        a.reverse()


                                                        c6=a[0]+a[1]+a[2]+a[3]+a[4]


                                                        c7="65000"

                                                        if(c6>=300):
                                        
                                                                print("Student is eligible for admission \n")
                                                                c7="65000"
                                                                c8=65000
                                                                print("Select Elective from below : ")
                                                               
                                                                print("1.Robotics \n")
                                                                print("2.Intermediate Fluid Mechanics \n ")
                                                                print("3.Computer Aided Design and Manufacturing \n")
                                                                print("4.BACK TO PREVIOUS OPTIONS\n")
                                                                print("0. EXIT \n")
                                                                
                                                                e=int(input(" Enter your choice : "))
                                                                if(e==1):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Robotics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==2):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Intermediate Fluid Mechanics"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")
                                                                elif(e==3):
                                                                        branch=" Mechanical Engineering "
                                                                        e1="Computer Aided Design and Manufacturing"
                                                                        obj1.registration()
                                                                        f+=1
                                                                        print(f," seats are filled up out of ",seats)
                                                                        print("\n")

                                                                elif(e==4):
                                                                        break
                                                                elif(e==0):
                                                                        exit(0)
                                                                else:
                                                                        print(" \n!!! Enter correct option !!! \n")
                                                                        break
                                                                
                                        
                                                        else:
                                                
                                                                print(" Sorry !! Student is not eligible for Admission \n")
                                                                break

                                                elif(c==5):
                                                        break
                                                elif(c==0):
                                                        exit(0)
                                                else:
                                                        print("\n !!! Enter correct option !!!\n ")
                                                        break
                                        else:
                                                
                                                print(" !!Sorry no  Seats are available !!")

                        elif(s4==4):
                                break
                        elif(s4==0):
                                exit(0)
                        else:
                                print(" \n !!! Enter correct option !!!\n")
                                break
                                
                                


                

                        
                
                               

        elif(s3==2):

                obj1.search()


        elif(s3==3):
                obj2.eligibility()

        elif(s3==4):
                obj1.search_bill()

        elif(s3==0):
                break

print("\n")
print("\n")
print("------------------------------------------------------------------------THANK YOU----------------------------------------------------------------------------")
print("\n")
print("-------------------------------------------------Copyright © 2019 CIT,KOKRAJHAR INDIA, Inc. All rights reserved----------------------------------------------------------")
print("\n")
print("\n")
print("\n")
print("\n")
                
                
                


                                


