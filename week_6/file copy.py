#open source file
source= open("words.txt","r", encoding="utf-8")
#read the content and save it in a variable
content = source.read()
#open backup file
backup_file = open("backup.txt","w")
#copy the content of the variable created earlier to backup
backup_file.write(content)
#close both files
source.close()
backup_file.close()
#print the confirmation
print("Backup file complete")