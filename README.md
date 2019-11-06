# CanteenManagementApp


  #to open the stall info file
  
  use code:
      
      import pickle
      data_file = open("stall_info.out", mode="rb")
      db= pickle.load( data_file)
      data_file.close()
      
   #db is now a list variable containing the list of stalls
