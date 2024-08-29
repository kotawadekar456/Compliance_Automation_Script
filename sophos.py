#!/usr/bin/python

import paramiko
import optparse
import re



parser = optparse.OptionParser('Usage: ./altchains.py -i <scope file> -u <username> -p <password>')
parser.add_option('-i', dest='sfile', type='string', help='Specify scope file')
parser.add_option('-u', dest='uname', type='string', help='Specify Username')
parser.add_option('-p', dest='pword', type='string', help='Specify Password')
(options, args) = parser.parse_args()
file = options.sfile
name = options.uname
word = options.pword

if file == None or name == None or word == None:
	#print(parser.usage
	exit(0)


def ssl_test(host, user, passw):
	print('*********************************************')
	print('AV scan report for '+host)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
	ssh.connect(host, username=user, password=passw)

	stdin_auditd, stdout_auditd, stderr_auditd = ssh.exec_command('/opt/sophos-av/bin/savdstatus | grep -F "is running"')
	temp1_in,version,temp1_err = ssh.exec_command('savscan -VV |grep "Product version"')
	temp2_in,dat,temp2_err = ssh.exec_command('savscan -VV | grep "Virus data version"')
	temp3_in,log,temp3_err = ssh.exec_command('/opt/sophos-av/bin/savlog | head')
	temp4_in,update,temp4_err = ssh.exec_command('/opt/sophos-av/bin/./savconfig  -v | grep UpdatePeriodMinutes')
	temp5_in,avscan,temp5_err = ssh.exec_command('/opt/sophos-av/bin/./savconfig  -v | grep NamedScans')
	a = stdout_auditd.channel.recv_exit_status()
	#b = stdout_rsyslogd.channel.recv_exit_status()
        
	if a == 0:
		print("Running in active mode :- Pass")
	else:
		print("Running in active mode :- Failed")

	print(str(version.read()).strip())
	#print('---------------------------------------------')
	print(str(dat.read()).strip('\n'))
	log_check(log.read())
	#print('---------------------------------------------')
	print('*********************************************')
	ssh.close()


#space for log function-----------
def log_check(rev_log):
        reg_obj=re.compile(r'\d\d \D\D\D \d\d\d\d')
        full_date=reg_obj.findall(str(rev_log))
        first_date=str(full_date[0])
        print('Oldest Log date founds       : '+str(first_date))
        reg_month=re.compile(r' \D\D\D')
        month_temp=reg_month.findall(first_date)
        month=str(month_temp[0].strip())
        


        
        ob=re.compile(r'\d\d\d\d')
        test = ob.findall(first_date)
        final_year=int(test[0])
        
        
        


#-------------------------------------




f = open(file)
for line in f:
	host = line.strip()
	ssl_test(host, name, word)


	
