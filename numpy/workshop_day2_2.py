print("\n\nCertificate Eligibility Checker\n\n")

question1=input("Have you attented all the classes or was there a day gap: \n\
                1. All Day.\n\
                2. Day Gap\n").strip().lower()

if question1=="all day" or question1=="1":
    question2=input("Have you submitted all the assignments on time: \n\
                    1. Yes\n\
                    2. No\n").strip().lower()
    if question2=="yes" or question2=="1":
        question3=input("Have you attended all the Live classes: \n\
                        1. Yes\n\
                        2. No\n").strip().lower()
        if question3=="yes" or question3=="1":
            question4=input("Was you camera on in those Live classes: \n")
            if question4=="yes" or question4=="1":
                question5=input("Have you scored atleast 70% in the final assessment: \n\
                                1. Yes\n\
                                2. No\n").strip().lower()
                if question5=="yes" or question5=="1":
                    print("\nCongratulations! You are eligible for the certificate.\n")
                else:
                    print("\nSorry! You are not eligible for the certificate.\n")
            else:
                print("\nSorry! You are not eligible for the certificate.\n")
        else:
            print("\nSorry! You are not eligible for the certificate.\n")
    else:
        print("\nSorry! You are not eligible for the certificate.\n")
        

else:
    print("\nSorry! You are not eligible for the certificate.\n")
