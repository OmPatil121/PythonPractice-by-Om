def add_contact(name, number):
    with open("contact.txt","a") as f:
     text = f.writelines(f"{name} => {number}\n")
   
def show_contact():
    with open("contact.txt") as k:
     content = k.read()
     return content 

def search_name(name):
   with open("contact.txt") as s:
      search_bar = s.readlines()
      
      for line in search_bar:
        
        if name in line:
           return line  
      return  "Contact not found" 
  
final_input = int(input('''What u want to do - 
1. Add a contact (Press 1)
2. Show all contact (Press 2)
3. Search contact (Press 3) \n ===> '''))

if final_input == 1:
    user_input_name = input("To add number write pupils name:  ")
    user_input_number = int(input("To add number write pupils contact number:  "))
    print("Contact successfully added")
    add_contact(user_input_name,user_input_number)

elif final_input ==2:
      print(show_contact())

else:
   search_input= input("Write name of pupil you want contact of: ").lower()
   print(search_name(search_input))
   




 
