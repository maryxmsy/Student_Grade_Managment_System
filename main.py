import json 

print("=" * 40)
print("STUDENT GRADE MANAGER SYSTEM")
print("=" * 40)
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
def valid_marks(subject):
	while True:
		marks=int(input(f"{subject} Marks:"))
		if 0 <= marks <= 100:
			return marks
		else:
			print("Marks must be between 0 and 100.")
			


def calculate_grade(student):
	total=(
	student["ai"]+
	student["python"]+
	student["maths"]+
	student["dbms"]+
	student["os"]
	)
	average=total/5
	if average >=90:
		grade="+A"
	elif average >=80:
		grade="A"
	elif average >=70:
		grade="B"
	elif average >=60:
		grade="C"
	elif average >=50:
		grade="D"
	else:
		grade="F"
	return total, average, grade
		
	



while True:
	print("\n.Main Menu")
	print("1. Add Student")
	print("2. View Students")
	print("3. Search Student")
	print("4. Update Student")
	print("5. Delete Student")
	print("6. Calculate Grades")
	print("7. Exit")
	
	choice=input("\nEnter your choice: ")
	if choice=="7":
		print("Thank you for using the program!")
		break
	elif choice=="1":
		name=input("Enter Student Name:")
		roll=input("Enter Roll Number :")
		duplicate=False
		for student in students:
			if student["roll"]==roll:
				duplicate=True
				break
		if duplicate:
			print("\nRoll Number already exists!")
			continue 
		ai=valid_marks("AI")
		python_marks=valid_marks("Python")
		maths=valid_marks("Mathematics")
		dbms=valid_marks("DBMS")
		os=valid_marks("OS")
		
		student={
		"name": name,
		"roll": roll,
		"ai": ai,
		"python": python_marks,
		"maths": maths,
		"dbms": dbms,
		"os": os
		}
		students.append(student)
		save_data( )
		print("\nStudent Added Successfully!")
	elif choice == "2":
		if len(students) == 0:
			print("\nNo Students Found.")
		else:
			print("\n----------Student Record----------")
			for student in students:
				print(f"\nName : {student['name']}")
				print(f"Roll: {student['roll']}")
				print(f"AI : {student['ai']}")
				print(f"Python:{student['python']}")
				print(f"Mathematics:{student['maths']}")

				print(f"DBMS:{student['dbms']}")
				print(f"OS:{student['os']}")
				print("-"*30)
				
		
		
	elif choice == "3":
		roll=input("Enter Roll Number to Search:")
		found=False
		for student in students:
			if student["roll"]==roll:
				print("\nStudent Name Found!")
				print(f"Name:{student['name']}")
				print(f"Roll:{student['roll']}")
				print(f"AI:{student['ai']}")
				print(f"Python:{student['python']}")
				print(f"Mathematics:{student['maths']}")
				print(f"DBMS:{student['dbms']}")
				print(f"OS:{student['os']}")
				found=True
				break
		if found == False:
			print("Student Not Found.")
	
	elif choice == "4":
	   roll = input("Enter Roll Number to Update: ")
	   found = False
	   for student in students:
	           	if student["roll"] == roll:
	           		found=True
	           		print("\nWhat do you want to update?")
	           		print("1. Name")
	           		print("2. Roll Number")
	           		print("3. AI Marks")
	           		print("4. Python Marks")
	           		print("5. Mathematics Marks")
	           		print("6. DBMS Marks")
	           		print("7. OS Marks")
	           		option=input("Enter your choice:")
	           		if option == "1":
	           			student["name"]=input("Enter New Name:")
	           		elif option == "2":
	           			student["roll"]=input("Enter New Roll Number:")
	           		elif option == "3":
	           			student["ai"]=int(input("Enter New AI Marks:"))
	           		elif option == "4":
	           			student["python"]=int(input("Enter New Python Marks:"))
	           		elif option == "5":
	           			student["maths"]=int(input("Enter New Mathematics Marks:"))
	           		elif option == "6":
	           			student["dbms"]=int(input("Entet New DBMS Marks:"))
	           		elif option == "7":
	           			student["os"]=int(input("Enter New OS Marks:"))
	           		
	           			
	           		
	           		
	           		save_data( )
	           		print("\nStudent Updated Successfully!")
	           		
	   if found == False:
	      	print("Student Not Found.")
	
	       
		    	
		   		
		   		
						
						
	       
		   
	       
		   
		   	
			
					
        
					
						
						
	elif choice == "5":
		roll=input("Enter Roll Number to Delete:")
		found=False
		for student in students:
			if student["roll"]==roll:
				confirm=input("Are you sure? (Y/N):")
				if confirm.upper( )=="Y":
					students.remove(student)
					save_data( )
					print("Student deleted successfully.")
				else:
					print("Deletion Cancelled.")
				
				
				save_data( )
				
				
				
						
	elif choice == "6":
	  if len(students)==0:
	  	print("\nNo Student Found.")
	  else:
	  	for student in students:
	  		total, average, grade=calculate_grade(student)
	  		print("\n------------------------------------")
	  		print(f"Name:{student['name']}")
	  		print(f"Roll:{student['roll']}")
	  		print(f"Total:{total}")
	  		print(f"Average:{average:.2f}")
	  		print(f"Grade:{grade}")
	  
   