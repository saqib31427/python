try:
   with open("C:\Users\HP\python\modules\minot1.txt",'r') as data :
    for i in data :
     if ":" in i :
      try:
          speaker, ls= i.split(":")
          print(speaker,"said",ls)
      except ValueError:
       pass  
except IOError:
    print("the file is missing")