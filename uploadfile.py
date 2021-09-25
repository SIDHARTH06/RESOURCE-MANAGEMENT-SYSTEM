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

#upload
filename=input("Enter the name of the file you want to upload")
cloudfilename=input("Enter the name of the file on the cloud")
storage.child(cloudfilename).put(filename)

print(storage.child(cloudfilename).get_url(None))