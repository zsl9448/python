from zhuye import window,label
from openfilalog import open_file

def on_label_click(event):
    label.config(relief="sunken")
    window.after(100, lambda: label.config(relief="raised"))#标签浮动
    window.withdraw()#隐藏
    from fengmianaddzhengwen import look    
    from tuozhuai import tuozhuaiapp

label.bind("<Button-1>", on_label_click)   #左键单击 

window.mainloop()
    
    



    
