# CanteenManagementApp


  #to open the stall info file
  
  use code:
      
      import pickle
      from Database import Stall
      from Database import item
      from Database import sort_data
      from Database import Search_item
      data_file = open("stall_info.out", mode="rb")
      db= pickle.load( data_file)
      data_file.close()
      sort_data(db)
      
   #db is now a list variable containing the list of stalls
   
   
   
   ##syntax for searching if stall is present: var= Search_item(db, Stall_namestring)
