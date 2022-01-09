import tkinter
from tkinter import *
def main():
    root=Tk()
    root.geometry('250x250')

    root.title('Calculater')

    def button_click(value):
        if input_lable.get()=="ERROR":
            input_lable.delete(0,END)
        if value==10:
            value="."
            if "." in input_lable.get():
                value=""

        if store_val.get() != "":
            last_sign = str(store_val.get())[-1]
            try:
                last_sign=float(last_sign)
                store_val.delete(0, END)
                first = ''
            except:
                pass


        input_lable.insert(END, value)


    def button_sub(sign_val):
        global Sign
        Sign=sign_val
        if sign_val==1:
            sign="+"
        elif sign_val==2:
            sign="-"
        elif sign_val==3:
            sign="*"
        elif sign_val==4:
            sign="/"
        if store_val.get() == "":
            value = input_lable.get() + sign
            # print(value)
        else:
            sv=store_val.get()
            if '+' in sv or '-' in sv or '*' in sv or '/' in sv:
                last_sign = str(sv)[-1]
                replace=str(sv).replace(last_sign,sign)
                store_val.delete(0,END)
                store_val.insert(0,replace)
                value=''
            else:
                value = sv +sign
                store_val.delete(0, END)
        store_val.insert(0, value)
        input_lable.delete(0, END)
    def button_mul():
        pass
    def button_div():
        pass

    def button_clear():
        first=""
        input_lable.delete(0,END)
        store_val.delete(0,END)
    def button_result():
        try:
            global first
            second=input_lable.get()
            last_sign=str(store_val.get())[-1]
            first=str(store_val.get()).replace(last_sign,"")
            input_lable.delete(0,END)
            store_val.delete(0,END)
            if second=="":
                store_val.insert(0,first)
            else:
                if Sign==1:
                    store_val.insert(0,float(first) +float(second))
                elif Sign==2:
                    store_val.insert(0,float(first) -float(second))
                elif Sign==3:
                    store_val.insert(0,float(first) * float(second))
                elif Sign==4:
                    store_val.insert(0,float(first) / float(second))
        except ZeroDivisionError:
            input_lable.delete(0,END)
            input_lable.insert(0,"ERROR")
        except Exception as e:
            print(e)
            print(store_val.get())



    store_val=Entry(root,bg='#ff4',font=('italic',10,'bold'),justify='center')
    store_val.grid(row=0,columnspan=4,sticky=W+E,ipadx=20)
    input_lable=Entry(root,bg='#ff4',font=('italic',10,'bold'),justify='center')
    input_lable.grid(row=1,columnspan=4,sticky=W+E,pady=10)

    button_9=Button(root,text=9,padx=10,pady=5,command=lambda:button_click(9))
    button_9.grid(row=4,column=2)
    button_8=Button(root,text=8,padx=10,pady=5,command=lambda:button_click(8))
    button_8.grid(row=4,column=1)
    button_7=Button(root,text=7,padx=10,pady=5,command=lambda:button_click(7))
    button_7.grid(row=4,column=0)
    button_6=Button(root,text=6,padx=10,pady=5,command=lambda:button_click(6))
    button_6.grid(row=5,column=2)
    button_5=Button(root,text=5,padx=10,pady=5,command=lambda:button_click(5))
    button_5.grid(row=5,column=1)
    button_4=Button(root,text=4,padx=10,pady=5,command=lambda:button_click(4))
    button_4.grid(row=5,column=0)
    button_3=Button(root,text=3,padx=10,pady=5,command=lambda:button_click(3))
    button_3.grid(row=6,column=2)
    button_2=Button(root,text=2,padx=10,pady=5,command=lambda:button_click(2))
    button_2.grid(row=6,column=1)
    button_1=Button(root,text=1,padx=10,pady=5,command=lambda:button_click(1))
    button_1.grid(row=6,column=0)

    button_0=Button(root,text=0,padx=10,pady=5,command=lambda:button_click(0))
    button_0.grid(row=7,column=0)
    button_p=Button(root,text=".",padx=10,pady=5,command=lambda:button_click(10))
    button_p.grid(row=7,column=1)
    button_C=Button(root,text="CLEAR",padx=2,pady=5,command=button_clear)
    button_C.grid(row=7,column=2)

    button_op = Button(root, text="+", padx=10, pady=5, command=lambda :button_sub(1))
    button_op.grid(row=7, column=3)
    button_s = Button(root, text="-", padx=10, pady=5, command=lambda :button_sub(2))
    button_s.grid(row=6, column=3)
    button_m = Button(root, text="X", padx=10, pady=5, command=lambda :button_sub(3))
    button_m.grid(row=5, column=3)
    button_d = Button(root, text="/", padx=10, pady=5, command=lambda :button_sub(4))
    button_d.grid(row=4, column=3)
    button_result = Button(root, text="=", padx=60, pady=5, command=button_result)
    button_result.grid(row=8, column=0,columnspan=3)



    root.mainloop()

if __name__ == '__main__':
    main()