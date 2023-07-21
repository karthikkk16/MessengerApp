from abc import ABC,abstractmethod

class MessagingService(ABC):
    def sendMessage(self):
        pass

class SMSMessagingService(MessagingService):
    def __init__(self,mobile,message):
        self.mobile=mobile
        self.message=message

    def sendMessage(self):
        print("The Mobile Number is :",self.mobile)
        print("The message sent is :",self.message)

class EmailMessagingService(MessagingService):
    def __init__(self,email,subject,message):
        self.email=email
        self.subject=subject
        self.message=message

    def sendMessage(self):
        print("The email is sent to :",self.email,"this email")
        print("The subject of the mail is :",self.subject)
        print("The message in the mail is :",self.message)

class WhatsAppMessagingService(MessagingService):
    def __init__(self,mobile,ismobile,message):
        self.mobile=mobile
        self.ismobile=ismobile
        self.message=message
    def sendMessage(self):

        if self.ismobile:
            print("The WhatsApp number is :",self.mobile)
            print("It is valid user in whatsapp")
            print("The message is :",self.message)
        else:
            print(self.mobile,"This number is not a valid WhatsApp user")


while True:
    print("Enter 1 for SMS")
    print("Enter 2 for Email")
    print("Enter 3 for Whatsapp")
    choice=int(input("Enter the messaging options:"))

    if choice==1:
        mobile=input("Enter the mobile number : ")
        if mobile[0] in "6789" and len(mobile)==10:
            message=input("Enter the message : ")
            sms=SMSMessagingService(mobile,message)
            sms.sendMessage()

        else:
            print("Invalid Mobile Number")

    elif choice==2:
        email=input("Enter the Email : ")
        if email.split('.')[-1] in ['com','in'] and '@'in email:
            subject=input("Enter Subject: ")
            message=input("Enter Message: ")
            em=EmailMessagingService(email,subject,message)
            em.sendMessage()
        else:
            print("Invalid Email")

    elif choice==3:
        mobile=input("Enter the mobile : ")
        if mobile[0] in "6789" and len(mobile)==10:
            ismobile=input("Enter whether it is a whatsapp number or not (T/F): ")
            if(ismobile=='T'):
                ismobile=True
            elif(ismobile=='F'):
                ismobile=False
            message=input("Enter the message : ")
            whatsapp=WhatsAppMessagingService(mobile,ismobile,message)
            whatsapp.sendMessage()
        else:
            print("The number may not be belongs to INDIA")

    else:
        print("Invalid Choice")

