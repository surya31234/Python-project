global inp
global index
global mean
record = []                        # for storing Student data in multidimension
import statistics                  # For calculation S.D
def new_student():                 # Function to add new student data to record array
  if len(record) > 20 :                                         # max number of students is 20
   print("Student data limit exceeded!!")
   return
  data = []                                            # Default array to store student data (later appended to record array)
  reg_no = input("Enter Registration number:")
  name = input("Enter Student Name:")
  marks = input("Enter Marks Obtained:")
  data.append(reg_no)
  data.append(name)
  data.append(int(marks))
  record.append(data)                                         # Appending data to record array
  print("--------------------------")
  print("Student Data Inserted successfully")
  print("--------------------------")
  return

def display_student():                                                    # Function to display the students based on given index
  index = input("Enter index(From 0) to display student data:")
  if int(index) > (len(record))+1:                                 # Validating record array length
    print("Student data not found!!")
    display_student()
  else:
    print("----------------------")
    print("Registration no: " + str(record[int(index)][0]))           # Fetching the data of student from record array
    print("Name: " + str(record[int(index)][1]))  
    print("Marks Obtained: " + str(record[int(index)][2])) 
    print("----------------------")
  
def update_student():                                               # function to update student data
  upd_index = input("Enter index(From 0) to update data :")
  if int(upd_index) > (len(record))+1:
    print("Student data not found!!")
    update_student()                                                   # Recursion if index exceeds length of record array
  else:
    new_reg = input("Enter new Registration number:")
    new_name = input("Enter new name:") 
    new_marks = input("Enter new marks:")
    record[int(upd_index)][0] = new_reg                              # Overwriting existing value
    record[int(upd_index)][1] = new_name
    record[int(upd_index)][2] = new_marks
    print("----------------------")
    print("Student Data updated successfully")
    print("----------------------")

def delete_student():                                                      # Function to delete student data
  del_index = input("Enter index(From 0) to Delete student record:")
  del record[int(del_index)]                                                # del method to remove element
  print("----------------------")
  print("Student Data Deleted successfully")
  print("----------------------")

def mean_deviation():                                   # Function to calculate mean deviation
  mean = 0 
  for i in range(len(record)):
    total = record[i][2]
    mean += float(total)
  print("------------------------")  
  print("Mean is " + str(mean/len(record)))               # average/no.of students
  print("------------------------")
  return mean

def std_deviation():                              # Function to calculate Standard deviation
  std_dev_data = []
  for i in range(len(record)):
    data = record[i][2]
    std_dev_data.append(data) 
  print("-------------------------------------")   
  print("Standard Deviation of marks data is % s " % (statistics.stdev(std_dev_data)))                 # Library function to compute S.D 
  print("-------------------------------------")   
  
while True:                                                    # Displaying the option menu infinitely
  print("Enter 1 to create new Student Record")
  
  if len(record) >= 1:                                          # Validating the option whether student data exists or not
   print("Enter 2 to Update a student record")
  
  if len(record) >= 1:
   print("Enter 3 to Delete a student record")

  if len(record) >= 1: 
   print("Enter 4 to Display Student records")

  if len(record) >= 1:
   print("Enter 5 to calculate mean deviation of class marks")

  if len(record) >= 2:
   print("Enter 6 to calculate mean deviation of class marks") 
  
  inp = input("Enter your choice")                                       # Getting user input

  if int(inp) == 1:
    new_student()                              # calling new_student() function
 
  elif int(inp)==2 and len(record) >= 1 :
    update_student()                           # Calling update_student() function
    
  elif int(inp)==3 and len(record) >= 1:
    delete_student()                           # Calling delete_student() function
    
  elif int(inp)==4 and len(record) >= 1:
    display_student()                          # Calling display_student() function

  elif int(inp)==5 and len(record) >= 1:
    mean_deviation()                            # Calling mean_deviation() function

  elif int(inp)==6 and len(record) >= 2:
    std_deviation()                            # Calling std_student() function
    
  else:
    print("Invalid Choice, Try again!")
