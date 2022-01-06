import os
import dropbox


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.A_muq5eKzztFDdO6HBNWPaMvn_YtA2rro-IZFa9rTuhK3VnWQOO5Y5RvxuLB4CxM7c2QTNZaA8fEV5o2qJI7vGQNOw2T1M_E_VgyqoQU5cXA5M-WquyEvgPHJnBmQ5q9hrgUTE4'
    transferData = TransferData(accessToken)
    fileFrom = str(input("Enter the folder path which you want to transfer:- "))
    fileTo = input("Enter the path to upload to dropbox:- ")
    transferData.uploadFile(fileFrom, fileTo)
    print("File has been transferred to your desired place")

main()