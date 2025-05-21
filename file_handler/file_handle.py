import os


class file:
      def __init__(self,file_Name,file_directory,file_content):
          self.file_Name = file_Name
          self.file_directory = file_directory
          self.path=self.file_directory+"\\"+self.file_Name
          self.content=file_content
      def delete_file(self):
          if os.path.exists(self.path):
              os.remove(self.path)
              print("File Deleted")
          else:
              print("File Not Found")
      def write_file(self):
          if os.path.exists(self.path):
              with open(self.path, 'w') as f:
                  f.write(self.content)
                  f.close()
                  print("File Written")
          else:
              print("File Not Found")
      def create_file(self):
          if os.path.exists(self.path):
              print('File Already Exists')
          else:
              with open(self.path, 'w') as f:
                  print("File Created")
      def open_file(self):
          if os.path.exists(self.path):
              with open(self.path, 'r') as f:
                  content=f.read()
                  print(content)
                  f.close()
          else:
              print("File Not Found")
if __name__ == "__main__":
     dir=input("Enter Directory Name: ")
     file_Name=input("Enter File Name: ")
     content=input("Enter File Content: ")
     file=file(file_Name,dir,content)
     # file.open_file()
     # file.delete_file()
     # file.write_file()
     # file.create_file()