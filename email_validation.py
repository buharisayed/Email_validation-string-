email = input("Enter your Email : ") #workbuhari7736@gmail.com
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha():#first letter alphabet
        if ("@" in email) and (email.count("@")==1):#@ condition
            if (email[-4]==".") ^ (email[-3]=="."):#dot condition
                for i in email:
                    if i==i.isspace():#space
                        k=1
                    elif i.isalpha():
                        if i==i.upper():#uppercase
                            j=1
                    elif i.isdigit():#characters
                        continue
                    elif i=="_" or i=="."or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                    print("wrong email :space/case/digit")
                else:print("Email is correct")
            else:
                print("wrong email: dot ")
        else:
            print("wrong email: @")
    else:
        print("first letter should be alphabet")
else:
    print("wrong Email :length")
