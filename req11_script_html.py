import re
import os 
import threading 
'''
This Script is design and develop to reduce a work of finding and matching IP in requirement 11
how to run this script
1. copy the code file in a directory where all VA reports are kept.
2. make a txt file and copy all IPs from asset inventory to that directory and rename file as "ip.txt"
3. 
'''

print('\n')

print('< Developed by ControlCase R&D team >')
print(' -----------------------------------')
print('        \   ^__^')
print('         \  (oo)\_______')
print('            (__)\       )'+'/\\')
print('                ||----w |')
print('                ||     ||')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
#declaration of variable 
not_found=[]
path=[]
ips=[]
final_temp=[]
final_all_ips=[]
t=''
string =''
threads = []




listdir = os.listdir()
print('Please wait...While Programm is reading files..')
for current_file_path in listdir:
    if current_file_path != "req11_script_html.py" and current_file_path !='ip.txt':
        html = open(current_file_path,'r',encoding='utf-8')
        t +=str(html.readlines())
regobj=re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
#regobj=re.compile(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$')
#regobj = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
regobj2 =re.compile(r'\d\d\d\.+\S+')
a=regobj.findall(t)
kk=set(a)

#scope_file_path=input('enter scope file path\n')
scope_file_path='ip.txt'
txt_file = open(scope_file_path)
scope_ip = txt_file.readlines()
for i in scope_ip:
    temp = i.strip()
    count =0 
    for j in a:
        if temp.strip('\n')== j.strip('\n'):
            count = 1
    if count == 0:
        not_found.append(i)
        count = 0


if not_found==[]:
    print('**********************************************')
    print('WOW!!!All IPs are covered in VA scan')
else:
    print('**********************************************')
    print('below ips from asset inventory are missing in report:-\n')
    for l in not_found:
        print(l)

  
