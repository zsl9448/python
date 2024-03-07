import tkinter as tk   
import openfilalog
#import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import docx
import docx_add_docx
#import os
class look():
    global window2
    global fengmian
    global zhengwen
    global hebing
    global FM_ZW_List
    global description
    FM_ZW_List=[]
    
    window2 = TkinterDnD.Tk()#第二个窗口
    window2.title("xxx")
    window2.geometry("200x200")
    fengmian = tk.Label(window2, text="封面(请将文件拖拽至此）",relief="sunken")#封面标签
    fengmian.pack() 
    zhengwen=tk.Label(window2, text="正文(请将文件拖拽至此）",relief="sunken")#正文标签
    zhengwen.pack()
    hebing=tk.Label(window2, text="开始合并",relief="sunken")#合并标签
    hebing.pack()
    description=tk.Label(window2, text="已添加%s个文件"%len(FM_ZW_List),relief="sunken")#正文标签
    description.pack(anchor="se")
    
    def fengmianclick(event):#封面标签操作
        fengmian.config(relief="sunken")
        window2.after(100, lambda: fengmian.config(relief="raised"))   
        openfilalog.open_file()
        pass
    def zhengwenclick(event):
        zhengwen.config(relief="sunken")
        window2.after(100, lambda: zhengwen.config(relief="raised")) 
        

        pass
    def hebingclick(event):
            hebing.config(relief="sunken")
            window2.after(100, lambda: hebing.config(relief="raised")) 
            print('sssss')
            print(type(FM_ZW_List))
            docx_add_docx.docx_add_docx(FM_ZW_List)
            FM_ZW_List.clear()
            print(len(FM_ZW_List))
            
            pass
    global file_path_return
    file_path_return=[]
    def on_drop_fengmian(event):
        file_path = event.data.replace('{','').replace('}','')
        FM_ZW_List.append(file_path)
        print(FM_ZW_List)
        fengmian.config(text=file_path)#对封面标签进行改名
        description.config(text="已添加%s个文件"%len(FM_ZW_List))
        return(file_path)
    def on_drop_zhengwen(event):
        file_path = event.data.replace('{','').replace('}','')
        FM_ZW_List.append(file_path)
        print(FM_ZW_List)
        zhengwen.config(text=file_path)#对封面标签进行改名    
        description.config(text="已添加%s个文件"%len(FM_ZW_List))       
        return(file_path)
    
        #print(file_path)   
        file_path_return.append(file_path)#共计打开多少个word文档 
        print(file_path_return)
    # 设置窗口接受文件拖拽+++++++++ 
    fengmian.drop_target_register(DND_FILES)#允许将文件拖拽至标签
    fengmian.bind("<Button-1>", fengmianclick)
    fengmian.dnd_bind('<<Drop>>', on_drop_fengmian)#绑定封面拖拽功能
    
    zhengwen.bind("<Button-1>", zhengwenclick)
    zhengwen.drop_target_register(DND_FILES)
    zhengwen.dnd_bind('<<Drop>>', on_drop_zhengwen)#绑定正文拖拽功能
    hebing.bind("<Button-1>", hebingclick)
    window2.mainloop()
    
    





