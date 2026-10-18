
class product:
    def __init__(self,name,price,quantity,category):
        self.esm = name
        self.gheymat = price
        self.tedad = quantity
        self.dastebandi = category
        
    def __str__(self):
        return (f"{self.esm.upper().strip()}\n"          
                f"{float(self.gheymat)}\n"
                f"{int(self.tedad)}\n"
                f"{self.dastebandi.lower().strip()}")
        
        
    def update_price(self,new_price):
        try:
            if new_price < 0:                            
                raise ValueError
                         
            self.gheymat = new_price
        except (ValueError, TypeError):                  
            print("gheymat nemitavanad manfi bashad va bayad adad bashad")
            
    def add_stock(self,afzayesh_mojoodi):
        try:
            if afzayesh_mojoodi < 0:                     
                raise ValueError
            self.tedad = self.tedad + afzayesh_mojoodi
        except (ValueError, TypeError):
            print("bayad adad vared konid")
        
    def sell(self,foroosh):
        try:
            if foroosh > self.tedad:                     
                raise ValueError
            self.tedad = self.tedad - foroosh
        except TypeError:                                
            print("meghdar dorost vared konid")
        except ValueError:
            print("mojoodi kafi nist")
        
        
    def apply_discount(self,takhfif):
        try:
            if takhfif < 0 or takhfif > 100:             
                raise ValueError
            self.gheymat = self.gheymat - (self.gheymat * takhfif / 100)
        except (ValueError, TypeError):
            print("meghdar dorost vared konid")
        
    def total_value(self):
        total = self.gheymat * self.tedad
        return total    