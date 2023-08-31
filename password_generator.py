import random, os, qrcode

char="123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"


len = int(input("enter your password length\n"))
password=''
for i in range(len):
    password += random.choice(char)     #password string will store random characters till loop last

print("Your generated passowrd is:",password)

ch=int(input("Want to make your password QR code:\n1. for yes\nrest. for no:\n"))

if(ch==1):
    password="Your Generated password is:"+password     #this message will going to store in qrcode image because qrcode.make() can't take 2 parameters
    img=qrcode.make(password)       #qrcode created
    path=os.getcwd()+"\qrcode.png"  #we get our current path with "\qrcode.png" name in it, if already .png file exist it will rewrite in it
    img.save(path)      #image saved at given path
    print("Your qrcode has been generated at",path)
else:
    print("no problem")


print("**************************************\n\nThank you for using our work\n\n**************************************")