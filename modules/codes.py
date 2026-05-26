''''THE 'codes.py' module will print the list of any dimention  '''
def print_nested_list(mylist,level,indent=False):
    '''thr function 'def print_nested_list'will print thr nested list and takes one argument  '''
    for i in mylist:
       if  isinstance(i,list):
          print_nested_list(i,level+1)
       else:
         if indent:
          for i in range(level):
           print("\t",end="")
   
    
       print(i)   
        