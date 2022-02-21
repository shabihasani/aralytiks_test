from fileinput import filename
import sqlalchemy
import os
from sqlalchemy import types, create_engine
import pandas as pd
import paramiko
from stat import S_ISDIR, S_ISREG
from datetime import date


host, port = 'ftp-gfm.aronova.com', 22
username, password = 'TP24', 'Kp66CLL!h8'

transport = paramiko.Transport(host,port)

transport.connect(None, username, password)

sftp = paramiko.SFTPClient.from_transport(transport)

#with open('TP_DIM_DEBITOR_Col.txt','r') as f:
#   columns = [line.strip() for line in f]
for entry in sftp.listdir_attr('gets'):
   if os.path.exists('C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder/'+ entry.filename):
       print(entry.filename+ ' Already exists!')
   elif entry.filename.__contains__(date.today().strftime('%Y%m%d')): 
        print(entry.filename+ " is downloading...")
        sftp.get('/gets/'+entry.filename,'C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder/'+ entry.filename)
        print(entry.filename + '  Download Completed!!')
      


'''for files in os.listdir('C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder/'):
  if os.path.exists(r'C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder'+files.upper().split('.',1)[0]+'.csv'):
      print('File already converted to .csv')
  else:
    read_file = pd.read_excel(r'C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder'+ files)
    read_file.to_csv (r'C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder'+files.upper().split('.',1)[0]+'.csv')


for file in os.listdir('C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder/'):
    read = pd.read_csv('C:/Users/Aralytiks/OneDrive - ARalytiKS L.L.C/Desktop/New folder/' + file, sep=None, engine="python", encoding='latin1')
#read.columns = columns
    print(read)

#query = text(f"""" INSERT INTO TP_DIM_ VALUES{ ',' })
#read = pd.read_csv('C:/Users/Gashi/OneDrive - ARalytiKS L.L.C/Documents/PYTHONETL/' + files, sep=None, engine="python", encoding='latin1')
 #   read.columns = columns
 #   print (read)
    #print (tabela.columns)
#    tabela.to_sql(files.partition('.') [0].upper(), con=conn, if_exists='append', index=False)
#print("All files successfully downloaded!!")
#filepath = '/gets/InvoiceListReport_TP24_20220214.xlsx'
#localpath = 'C:/Users/gashi/OneDrive - ARalytiKS L.L.C/Documents/PYTHONETL/InvoiceListReport_TP24_20220214.xlsx'
#sftp.get(filepath,localpath)'''