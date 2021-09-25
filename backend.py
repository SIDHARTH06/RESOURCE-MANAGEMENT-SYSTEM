import pyrebase

firebaseConfig = { 'apiKey': "AIzaSyDHhm8S1tHYX8pPEUb2jo4j1a0rOz-4o5A",
    'authDomain': "resource-management-c024a.firebaseapp.com",
    'projectId': "resource-management-c024a",
    'databaseURL': "https://resource-management-c024a-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "resource-management-c024a.appspot.com",
    'messagingSenderId': "39523970740",
    'appId': "1:39523970740:web:08243ce39a16550278f1e1"
    }

firebase=pyrebase.initialize_app(firebaseConfig)

# db=firebase.database()
# auth=firebase.auth()
storage=firebase.storage()

# authentication
#login
# email=input("Enter your email")
# password=input("Enter your password")
# try:
#     auth.sign_in_with_email_and_password(email,password)
#     print("Login Successful!")
# except:
#     print("!!!Invalid username or password!!!")
#     print("Try again")

#sign up
# email=input("Enter your email")
# password=input("Enter your password")
# confirmpassword=input("Confirm password")
#
# if password==confirmpassword:
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         print("Success!")
#     except:
#         print("email already exists")

#storage

# #upload
# filename=input("Enter the name of the file you want to upload")
# cloudfilename=input("Enter the name of the file on the cloud")
# storage.child(cloudfilename).put(filename)
#
# print(storage.child(cloudfilename).get_url(None))

#download
cloudfilename=input("Enter the name of file you want to download")
storage.child(cloudfilename).download("","downloaded.txt")