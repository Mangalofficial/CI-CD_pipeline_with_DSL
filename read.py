open_file=open('/jenkins/workspace/JOB2_task4/port.py','r')
read=open_file.read()
for a in read:
  if a.isnumeric() == True: 
      print(a,end='')
