import sqlalchemy
import os
from sqlalchemy import types, create_engine
import pandas as pd
import paramiko
from stat import S_ISDIR, S_ISREG


host, port = 'ftp-gfm.aronova.com', 22
username, password = 'TP24', 'Kp66CLL!h8'

transport = paramiko.Transport(host,port)

transport.connect(None, username, password)

sftp = paramiko.SFTPClient.from_transport(transport)

for entry in sftp.listdir_attr('gets'):
    #print(entry.filename+ " is file")
    sftp.get('/gets/'+entry.filename,'C:/Users/gashi/OneDrive - ARalytiKS L.L.C/Documents/PYTHONETL/'+ entry.filename)
    #print(entry.filename + '--- Download Completed!!')

#print("All files successfully downloaded!!")
#filepath = '/gets/InvoiceListReport_TP24_20220214.xlsx'
#localpath = 'C:/Users/gashi/OneDrive - ARalytiKS L.L.C/Documents/PYTHONETL/InvoiceListReport_TP24_20220214.xlsx'
#sftp.get(filepath,localpath)




