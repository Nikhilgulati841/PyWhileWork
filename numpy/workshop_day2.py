print("\n\t--Roadmap Provider Project--\n") 

while True:
    ask=input("Are you an Experienced or a Fresher: ")
    print("\n")
    while True:
        if ask=="Experienced" or ask.lower()=="experienced":
            ask2=input("You have three of the options as a career to choose as an Experience holder:\n\
                    1.Data Analytics\n\
                    2.Cloud Computing\n\
                    3.Front End\n")
            if ask2=="Data Analytics" or ask2.lower()=="data analytics" or ask2=="1":
                print("\nFor Data Analyst:-\nYou can start learning Python, R, SQL, Excel, Tableau, Power BI, Hadoop, Spark, etc.\n")
            elif ask2=="Cloud Computing" or ask2.lower()=="cloud computing" or ask2=="2":
                print("\nFor Cloud Computing:-\nYou can start learning AWS, Python for Automation Microsoft Azure, Google Cloud Platform, Docker, Kubernetes, Terraform, etc.\n")
            elif ask2=="Front End" or ask2.lower()=="front end" or ask2=="3":
                print("\nFor Front End:-\nYou can start learning HTML, CSS, JavaScript, React, Angular, Vue.js, Bootstrap, Learn Python and Django for Backend\n")
                
            else:
                print("\t!!Enter valid option!!\n\n")
                continue

        elif ask=="Fresher" or ask.lower()=="fresher":
            ask4=input("You have three of the options as a career to choose as a fresher:\n\
                    1.Web Development\n\
                    2.App Developement\n\
                    3.DS, ML, AI\n")
            if ask4=="Web Development" or ask4.lower()=="web development" or ask4=="1":
                print("\nLearn HTML, CSS, JS, Python Django\n")
                
            elif ask4=="App Developement" or ask4.lower()=="app developement" or ask4=="2":
                print("\nLearn Java, Kotlin for Android and Swift for iOS\n")
            
            elif ask4=="DS, ML, AI" or ask4.lower()=="ds, ml, ai" or ask4=="3":
                print("\nLearn Python, R, SQL, TensorFlow, Keras, PyTorch, etc.\n   ")
        
            else:
                print("\t!!Enter valid option!!\n\n")
                continue
        else:   
            print("\t!!Enter valid option!!\n\n")
            continue
        option=input("\n What do you want to do next:\n\
                    1.Choose another Career option.\n\
                    2.Go to the main menu.\n\
                    3.Exit.\n\
                    Enter your option (1/2/3): \n")
                    
        if option=="1":
            continue
        elif option=="2":
            break
        else:
            print("\n\t--Thank you for using the Roadmap Provider Project!--\n")
            exit()
    
            
        