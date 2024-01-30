from os import system
system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/http')
system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/urllib3')
system("rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
system('pkg uninstall python -y;pkg install python -y;pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
system('clear')
print("MAYBE FIXED RUN TOOLS AGAIN")
