import os
import math
import statistics

if os.path.exists(r"C:\Users\Hadis\Desktop\project"):  
    print(True)
else:
    print(False)
    
    
zarf = os.listdir(r"C:\Users\Hadis\Desktop\project")
print(zarf) 

tedad = len(os.listdir(r"C:\Users\Hadis\Desktop\project"))
print(tedad)


s1 = os.path.getsize(r"C:\Users\Hadis\Desktop\project\data.csv")  
s2 = os.path.getsize(r"C:\Users\Hadis\Desktop\project\image.jpg") 
s3 = os.path.getsize(r"C:\Users\Hadis\Desktop\project\main.py")  
s4 = os.path.getsize(r"C:\Users\Hadis\Desktop\project\report.pdf")  
s5 = os.path.getsize(r"C:\Users\Hadis\Desktop\project\users.txt")  
print(s1,s2,s3,s4,s5)

jam = s1 + s2 + s3 + s4 + s5
print(jam)    

hajm =[s1,s2,s3,s4,s5]
miyangin = statistics.mean(hajm)
print(miyangin)

bozorgtarin = max(s1,s2,s3,s4,s5)
print(bozorgtarin)

kochiktarin = min(s1,s2,s3,s4,s5)
print(kochiktarin)

print(math.ceil(s1))
print(math.ceil(s2))
print(math.ceil(s3))
print(math.ceil(s4))
print(math.ceil(s5))


count = 0
for i in zarf:
    if ".py" in i:
        count = count + 1
print("tedad file hay .py:" ,count)
    
c = 0
for i in zarf:
    if ".txt" in i:
        c = c + 1
print(f"tedad file hay .txt:{c}")    
    
    
countt = 0
for i in zarf:
    if ".csv" in i:
        countt = countt + 1
print(f"tedad file hay .csv:{countt}")    
    