import csvopen as sf
import smtplib 
import sys


mail = smtplib.SMTP('smtp.gmail.com', 587) 
mail.starttls()

sender_mail=input("Enter Senders E--mail ID -:    ")
password= input("Password -:    ")

try:
    mail.login(sender_mail, password)
    message = input("Email Body -:    ")
except:
    print("something went wrong !!! , check your internet connection")
    sys.exit()
    

def send_mail(p): 
  
    #animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
       
    count=1
    
    for i in p:  
        receivers_mail= i[1]
        mail.sendmail(sender_mail,receivers_mail,message)
        sys.stdout.write("\r" + "sent... "+str(count))
        sys.stdout.flush()
        count+=1
        
    sys.stdout.write("\r" + "All sent Successfully")
    mail.quit()
    
    
def update(e):
    var=True
    while var:
        k=int(input("Enter the Serial Number to Update ---> "))
        e[k-1][0]=input("New name ---> ")
        e[k-1][1]=input("New E-mail Id ---> ")
        print()
        print("-"*10)
        print("Record Updated Successfully")
        print("-"*10)
        print()
        printlist(e)
        var2=input("Any more changes required? YES/NO---> ")
        if(var2.lower()=="no"):
            var=False  
    
              
              
              
def printlist(p):
    print()
    print("*"*30)
    print("***** Email List provided *****")
    print("*"*30)
    print()
 
    
    for i in range(len(p)):
        print("------------------------------------")
        print("Serial number --> {}".format(i+1))
        print("Recipient name --> "+ p[i][0])
        print("Recipient Email Address --> " +p[i][1])
        print("------------------------------------")

        
        
def csvgmail():   
    file=open("gmails.csv")
    lst5=[]
    for x in file:
        cv=x.split()
        lst5.append(cv)
    print(lst5)
    send_mail(lst5)
    
# creates SMTP session 


print()
print()
lst=[]
print("list of E-mail's   ------------>  1")
print("Excel sheet        ------------>  2")
print()

option1= int(input("Choose one of them ---> "))
print("-"*20)
if (option1==1):
    var1=True
    while var1:
        lst2=[]
        a=input("Enter Name of recipient  -: ")
        b=input("Enter E-mail ID of recipient  -: ")
        lst2.append(a)
        lst2.append(b)
        lst.append(lst2)
        print()
        var2=input("TYPE ('STOP') IF YOU ARE DONE WITH EMAIL LIST ELSE CLICK ENTER ")
        if(var2.lower()=="stop"):
            var1=False  
        print()
    
    printlist(lst)
    print()
    
    j= input("Do you want to make any changes? YES OR NO --->  ")
    if j.lower()=="yes":
        update(lst)
    
    
        
        

    
elif(option1==2):
    p=0
    print("please select the Excel file ")
    lst=sf.selectfile()
    printlist(lst)
    j= input("Do you want to make any changes? YES OR NO --->  ")
    if j.lower()=="yes":
        update(lst)
    
    
   
    
else:
    print("invalid option selected")



print()
print()
print("-------FINAL LIST TO BE SENT----------")
printlist(lst)
send_mail(lst)
              
# Authentication 



  
# message to be sent 


#bansalpushkar6@gmail.com
#kavya9140@gmail.com
#bbbshyaw@123k
#9927686088
