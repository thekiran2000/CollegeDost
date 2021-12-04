from django.shortcuts import render
import csv
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'demo/index.html')

def contact(request):
   
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    
    
    
    return render(request, 'demo/contacts.html')



def iit(request):
    return render(request, 'demo/iit.html')

def iit2(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        branch = request.POST.get('branch', '')
        caste = request.POST.get('caste', '')
        gender = request.POST.get('gender', '')
        rank = request.POST.get('rank', '')

        print(name,branch,caste,gender,rank)
        
    final=[]
    category={}
    with open('C:/Users/Lenovo/Django/Collegedost/collegedost/demo/Datasets/IIT.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        count=0
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
            
                line_count += 1
                if line_count==2718:
                    break
            
                if row[3]==caste and row[1]==branch and row[4]==gender:  
                    try:  
                        if int(rank)<int(row[6]) :
                               
                                category["institute"]=row[0]
                                category["opening"]=row[5]
                                category["closing"]=row[6]
                                final.append(category)
                                category={}

                                count+=1
                    except:
                        pass

        print(f'Processed total {line_count} for IIT and {count} result lines found.')


    return render(request, 'demo/iit.html',{'final':final,'name':name})




def nit(request):
    return render(request, 'demo/nit.html')

def nit2(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        branch = request.POST.get('branch', '')
        caste = request.POST.get('caste', '')
        gender = request.POST.get('gender', '')
        rank = request.POST.get('rank', '')
        quota = request.POST.get('quota', '')

        print(name,branch,caste,gender,rank)
        
    final=[]
    category={}
    with open('C:/Users/Lenovo/Django/Collegedost/collegedost/demo/Datasets/NIT.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        count=0
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
            
                line_count += 1
                if line_count==5659:
                    break
            
                if row[3]==caste and row[1]==branch and row[4]==gender and row[2]==quota:  
                    try:  
                        if int(rank)<int(row[6]) :
                               
                                category["institute"]=row[0]
                                category["opening"]=row[5]
                                category["closing"]=row[6]
                                final.append(category)
                                category={}

                                count+=1
                    except:
                        pass

        print(f'Processed total {line_count} for NIT and {count} result lines found.')


    return render(request, 'demo/nit.html',{'final':final,'name':name})



def iiit(request):
    return render(request, 'demo/iiit.html')

def iiit2(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        branch = request.POST.get('branch', '')
        caste = request.POST.get('caste', '')
        gender = request.POST.get('gender', '')
        rank = request.POST.get('rank', '')

        
        
    final=[]
    category={}
    with open('C:/Users/Lenovo/Django/Collegedost/collegedost/demo/Datasets/IIIT.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        count=0
        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
            
                line_count += 1
                if line_count==586:
                    break
            
                if row[3]==caste and row[1]==branch and row[4]==gender:  
                    try:  
                        if int(rank)<=int(row[6]) :
                               
                                category["institute"]=row[0]
                                category["opening"]=row[5]
                                category["closing"]=row[6]
                                final.append(category)
                                category={}

                                count+=1
                    except:
                        pass

        print(f'Processed total {line_count} for IIIT and {count} result lines found.')


    return render(request, 'demo/iiit.html',{'final':final,'name':name})



def jee(request):
    return render(request, 'demo/JEE.html')

def jee2(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        branch = request.POST.get('branch', '')
        rank = request.POST.get('rank', '')

        
        
    final=[]
    category={}
    with open('C:/Users/Lenovo/Django/Collegedost/collegedost/demo/Datasets/JEE.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        count=0
       

        
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
            
                line_count += 1
                if line_count==2482:
                    break
                
                if  row[5]==branch :  
                    try:
                        rate=""  
                        for ele in str(row[1]):
                            if ele=="(":
                                break
                            rate=rate+ele
                        print(row[1])    
                        print(rate)
                        print(rank)
                        if int(rank)<=int(rate) :
                               
                                category["institute"]=row[3]
                                category["opening"]=row[1]
                                category["choice"]=row[2]
                                final.append(category)
                                category={}

                                count+=1
                        rate=""
                    except:
                        pass

        print(f'Processed total {line_count} for State Colleges and {count} result lines found.')


    return render(request, 'demo/jee.html',{'final':final,'name':name})