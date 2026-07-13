import random
class Train:
    
    def __init__(self,train_no,fro,to):
        self.train_no = train_no
        self.fro = fro
        self.to = to
    def book(self,train_no,fro,to):
        print(f"Your ticket is booked from {fro} to {to} and train number is {train_no}")
        
    def getstatus(self,train_no,fro,to):
        
        print(f"Your train having train number {train_no} is running on time from {fro} to {to}e ")
    def fare(self,train_no,fro,to):
        print(f"Ticket charge is {random.randint(200,1500)} rupees")
        
c1 = Train(121,"Mhow","Rajpur") 
c1.book(121,"Mhow","Rajpur")
c1.getstatus(121,"Mhow","Rajpur")
c1.fare(121,"Mhow","Rajpur")      
