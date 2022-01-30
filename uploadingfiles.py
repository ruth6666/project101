import dropbox
class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken
    
    def upload_file(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)

def main():
    accessToken = 'RjubiHx6ExIAAAAAAAAAASsf7YKLBDcgZHFhWCmdBztYekeUUjdYyM8Z5W4MGN9e'
    transferData = TransferData(accessToken)
    fileFrom = input('Enter the source:')
    fileTo = input('Enter the path for uploading to dropbox:')

    transferData.upload_file(fileFrom,fileTo)
    print('FILE HAS BEEN MOVED.')

main()