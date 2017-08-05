import dropbox
from helpers import ClipBoard


class InterClip:

    def __init__(self, token):

        try:
            self.client = dropbox.Dropbox(token)
        except:
            ##user interface in place of print promt
            print("no internet acess")
        self.clipped_text = ClipBoard()


    def temporary_copy(self):

        content = self.clipped_text.pull_text()
        try:
            self.client.files_upload(content.encode(),
                                '/testing/cpy.txt',
                                mode=dropbox.files.WriteMode('overwrite', None))
        except:
            ##user interface in place of print promt
            print("no internet acess")


    def longterm_copy(self):

        content = self.clipped_text.pull_text()
        try:
            self.client.files_upload(content.encode(),
                                '/testing/multiple/cpy.txt',
                                autorename=True)
        except:
            ##user interface in place of print promt
            print("no internet acess")


    def temporary_paste(self):

        try:
            metadata,response = self.client.files_download('/testing/cpy.txt')
            self.clipped_text.push_text(response.text)
        except:
            ##user interface in place of print promt
            print("no internet acess")
