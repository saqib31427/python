def print_nested_list(mylist):
    '''thr function 'def print_nested_list'will print thr nested list and takes one argument  '''
    for i in mylist:
     if  isinstance(i,list):
        print_nested_list(i,level+1)
        for i in range(level):
         print("\t",end="")
    else:
      print(i)   