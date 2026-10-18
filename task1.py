class student:
    
    def __init__(self,esm,nomre):
        self.name= esm
        self.grade = nomre
        self.adad = []      
        self.tedad = 0      
        


    def add_grade(self):
        try:
            if 0 <= self.grade <= 20:
                self.adad.append(self.grade)        
                self.tedad = len(self.adad)         
                with open(r'C:\Users\Hadis\Desktop\grades.txt','a') as file:   
                    file.write(f"{self.name},{self.grade}\n")   
                print(self.adad)
            else:
                raise ValueError
                
        except ValueError:
        
            print('adad vared konid')
            
        except FileNotFoundError:
            
            print('file mojood nist')
        
        except Exception:
            
            print('khatay gheire ghabel pishbini etefagh oftad')
        
        
        
    def read_grades(self):
        try:
            with open(r'C:\Users\Hadis\Desktop\grades.txt','r') as file:   
                text=file.read()
                print(text)
        except FileNotFoundError:
            print("file mojood nist")
        except Exception:
            print("khatay gheire ghabele pishbini")
        
            
        
    def calculate_average(self):
        try:
            total = sum(self.adad)      
            miyangin = total / self.tedad
            return miyangin 
        except ZeroDivisionError:
            print("tedad nemitavanad sefr bashad")
            
    def find_top_student(self):
        if not self.adad:           
            return None
        bishtarin = max(self.adad)  
        return bishtarin