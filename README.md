# Compliance_Automation_Script

This script is develop to reduce domain 11 ip matching task. 

PCI DSS mandates to perform VA and PT on all in-scope IPs so during audit it will be difficult to match each and every IP.
req11_pdf.py workes on pdf file. In order to use this script you have to crate folder and store all VA, PT report in that folder along with ip.txt file.

ip.txt is nothing but inscope ip from asset inventory. Once done run script in that directory. it will give you an output of missing ips. 

Same you can use req11_html.py if you have nessus, nexpose html report. 
