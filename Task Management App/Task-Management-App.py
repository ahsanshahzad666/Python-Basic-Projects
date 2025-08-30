def Tasks ():
    Tasks_list = []    #empty list
    print("________Welcome to Task Management App_______")
    
    

    total_tasks = int(input("How Many Tasks you want to do today? = "))
    for i in range(1, total_tasks+1):
       Task_name = input(f"Enter Task {i} Name  = ")
       Tasks_list.append(Task_name)
    
    print(f"Today Total Tasks {Tasks_list}")
    

# Tasks()

    while True:
       action = input("Want Any Changes? YES/NO = ").lower()
  
       if action == "yes":
          print("Okay, let's make changes!")
          operations = input("\n 1 - Add \n 2 - Update \n 3 - delete \n 4 - View \n 5 - Exist \n Waiting for your actions... =  ")
          
          if operations == "1":
              New_task = input("Add New Task = ")
              Tasks_list.append(New_task)
              print(f"Task {New_task} is added successfully")
              
                           
          if operations == "2":
              old_task = input("Which Task you want to update = ")
              if old_task in Tasks_list:
                 update_task = input("Enter Update Task")
                 task_index =  Tasks_list.index(old_task)
                 old_task[task_index] = update_task
                 print(f"Task {update_task} is updated successfully")
              
              
          if operations == "3":
              delete_task = input("Which Task you want to delete = ")
              if delete_task in Tasks_list:
                 task_index =  Tasks_list.index(delete_task)
                 del Tasks_list[task_index]
                 print(f"Task {delete_task} is deleted successfully")
                 
                 
          if operations == "4":
                  print(f"Today Total Tasks {Tasks_list}")
                  
           
          if operations == "5":
               print(f" Your Final Today Tasks {Tasks_list}")
               break         
          
          else:
              print("Invalid operation")
            
         

       elif action == "no":
           print("No changes, continue as is...")
           break
  
  
       else:
          print("Invalid input, please type YES or NO.")
       



Tasks()
    



    