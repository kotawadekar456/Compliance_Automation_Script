import PyPDF2
import re
import os 
import threading
import glob
'''
This Script is design and develop to reduce a work of finding and matching IP in requirement 11
how to run this script
1. copy the code file in a directory where all VA reports are kept.
2. make a txt file and copy all IPs from asset inventory to that directory and rename file as "ip.txt"
3. 
'''


print('')
print('')
print(' -----------------------------------')
print('< Developed by ControlCase R&D team and This is COW >')
print(' -----------------------------------')
print('        \   ^__^')
print('         \  (oo)\_______')
print('            (__)\       )'+'/\\')
print('                ||----w |')
print('                ||     ||')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print('\n')

#print('\t**********************************************')
#declaration of variable

not_found=[]
path=[]
ips=[]
final_temp=[]
final_all_ips=[]
t=''
string =''
threads = []
total_ip = 0
missing_ip_count=0
ip_count=0

listdir = glob.glob("*.pdf")
print('*************** Please wait ***************')
for current_file_path in listdir:
    pdfobj = open(current_file_path,'rb')
    pdfreader = PyPDF2.PdfFileReader(pdfobj)
    enc_value = pdfreader.isEncrypted
    if enc_value == " True":
        print(current_file_path+" is encrypted with unknown algorithm")
    total_page= pdfreader.numPages
    for z in range(0,total_page):
        pageobj = pdfreader.getPage(z)
        t +=str(pageobj.extractText())

regobj=re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
#regobj=re.compile(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})$')
#regobj = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
#regobj2 =re.compile(r'\d\d\d\.+\S+')
a=regobj.findall(t)
kk=set(a)


#scope_file_path=input('enter scope file path\n')
scope_file_path='ip.txt'
txt_file = open(scope_file_path)
scope_ip = txt_file.readlines()
for i in scope_ip:
    temp = i.strip()
    count =0
    total_ip=total_ip+1
    for j in a:
        if temp.strip('\n')== j.strip('\n'):
            count = 1
    if count == 0:
        not_found.append(i)
        count = 0


if not_found==[]:
#    print('**********************************************')
    print('\n')
    print('All In-Scope assets are covered.')
else:
#    print('**********************************************')
    print('\n')
    print('** Missing Asset **')
    print('\n')
    for l in not_found:
        missing_ip_count=missing_ip_count+1
        ip_count=ip_count+1

        
    if total_ip==missing_ip_count:
        print('Unable to read PDF.PDF might be encoded with unknown format')
    else:
        for x in not_found:
            print(x)

#print('')
#if total_ip== missing_ip_count:
#    print('Script might not able to read PDF.')
#    print('PDF is encoded with unknown standard')


print()
print('------------------------------------')
print('Final Summary report')
print('------------------------------------')
print('Total number of asset  :-  '+str(total_ip))
print()
print('Total number of missing asset :- '+str(missing_ip_count))
print('')
print('Total number of covered asset :- '+str(total_ip-missing_ip_count))
print('------------------------------------')

  
