
# coding: utf-8

# In[68]:


import tkinter as tk

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb  

window = tk.Tk()
window.title("你比我猜 (Beta version by Linyun)")
 
window.config(bg=_from_rgb((255, 255, 214)))

window.counter = 0
v = tk.StringVar(window, value='60')
max_time_txt = tk.Entry(window,textvariable=v,width=5)
max_time_txt.grid(column=2, row=0)

timer_lbl = tk.Label(window, text="Timer",borderwidth=2, relief="groove")
timer_lbl.grid(column=1, row=0)


main_txt = tk.Label(window,text="WORD HERE", font=(None, 70),height=2, width=10)
main_txt.grid(column=5, row=10)
main_txt.config(bg=_from_rgb((255, 255, 214)))

logo = tk.PhotoImage(file="HElogo_my_meitu_2.png")
w1 = tk.Label(window, image=logo,text='here')
w1.grid(column=5, row=90)
w1.config(bg=_from_rgb((255, 255, 214)))

guessWord = open("words2.txt", encoding="utf-8").read().split('\n')


def clicked(event=None):
 
    countdown(int(max_time_txt.get()))
    main_txt['text'] = guessWord.pop()
    btn_start['state'] = 'disabled'
    btn_next['state'] = 'normal'    
def countdown(count):
    # change text in label        
    timer_lbl['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count-1)
    if count == 0:
        timer_lbl['text'] = 'Over'
        main_txt['text'] = "WORD HERE"
        btn_start['state'] = 'normal'
        btn_next['state'] = 'disabled'
        count_lbl.config(bg=_from_rgb((255, 225, 224)))

        
def word_next(event=None):
    if btn_next['state'] == 'normal':
        
        if var.get() == 1:
            window.counter += 1
            count_lbl['text'] = "Correct: "+str(window.counter)
        if len(guessWord) > 0:
            main_txt['text'] = guessWord.pop()
        else:
            main_txt['text'] = "No more words"
        
def key_select(event=None):
    var.set(not var.get())

btn_start = tk.Button(window, text="Start", command=clicked)
btn_start.grid(column=3, row=0)

count_lbl = tk.Label(window, text="Correct: 0",borderwidth=2, relief="ridge",font=(None, 30),height=1, width=10)
count_lbl.grid(column=5, row=1)
count_lbl.config(bg=_from_rgb((255, 255, 224)))


var = tk.IntVar()

rad1 = tk.Radiobutton(window,text='Correct', variable = var, value=True)
rad2 = tk.Radiobutton(window,text='Wrong', variable = var, value=False) 
rad1.grid(column=120, row=75) 
rad2.grid(column=125, row=75)
rad1.config(bg=_from_rgb((255, 255, 224)))
rad2.config(bg=_from_rgb((255, 255, 224)))

btn_next = tk.Button(window, text="Next", state = tk.DISABLED, command=word_next)
btn_next.grid(column=145, row=80)
btn_next.config(bg=_from_rgb((255, 255, 224)))
window.bind("<Right>", word_next)
window.bind('<Return>', clicked)
window.bind('<space>',key_select)

window.mainloop()

