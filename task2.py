
class karbar:
    
    def __init__(self):
        self.shenase = []
        self.name = [] 
        self.age = []
        self.email = []
        
    
    def add_user(self,shenase,esm,sen,emaill):
        try:
            self.shenase.append(shenase)
            self.name.append(esm)
            self.age.append(sen)
            self.email.append(emaill)
            
        except Exception:
            print("meghdar nadorost")
        
    def find_user(self):
        for i in self.name:
            print(i)
            
            
            
    def delete_user(self, shenase):              
        try:
            index = self.shenase.index(shenase)  
            self.shenase.pop(index)              
            self.name.pop(index)                 
            self.age.pop(index)
            self.email.pop(index)
        except ValueError:
            print("vojood nadarad")              
            
            
    def update_user(self, shenase):              
        try:
            index = self.shenase.index(shenase)
            email_jadid = input("enter email: ")
            self.email[index] = email_jadid      
        except ValueError:
            print("vojood nadarad")
            
            
    def list_users(self):
        print(list(self.shenase))
        print(list(self.name))
        print(list(self.email))
        print(list(self.age))            
        
        
    def generate_report(self):
        print(self.name)
        print(len(self.shenase))
        