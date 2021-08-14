import os
import dropbox
from dropbox.files import writeMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = Dropbox.dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for filename in files:

                local_path=os.path.join(root,filename)

                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)

                with open (local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=writeMode('overwrite'))


def main():
    access_token='sl.A2jtBPQD4CsT5rfqJ0N5I5TxA2BqpinEVVfywESSgr0pPt2PRvlYMW94ElgW7axr-gHqkynG4JG3zhMaxVUBW_2_IWVZLrdXhBl_HekFB49OfpCHUuUbe0yx4k19ZEBTaSfonpM'
    TransferData=TransferData(access_token)

    file_from=str(input('Enter the folder path to transfer :- '))
    file_to=input("Enter the full path to upload to dropbox :- ")

    transferData.upload_file(file_from,file_to)
    print("file has been successfully moved")

main()

