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

#storage

#reading a file

cloudfilename=input("Enter the name of file you want to read")
url=storage.child(cloudfilename).get.url(None)
s=urllib.request.urlopen(url).read()
print(s)