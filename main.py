import tkinter
from tkinter import scrolledtext

import createnum
import progress



key_number = ''
process = 10
def clicked():

    global key_number
    global process

    if btn_play["text"] == 'проверить':
        if not createnum.check_enter_number(txt.get()):
            inf_lable.configure(text='Не кореектно\n'
                                     'ведитечетырехзначное число\n'
                                     'без повторяющихся цифр:')
            txt.configure()

        else:
            bull, cow, flag = progress.intersections_number(key_number, txt.get())

            if flag:
                inf_lable.configure(text='ЧИСЛО РАЗГАДАНО!')
                btn_play.configure(text='игра')

            else:
                bull_lable.configure(text=f'bull: {bull}')
                cow_lable.configure(text=f'cow: {cow}')
                try_box.insert(tkinter.INSERT, txt.get() + '\n')
                process -= 1
                if process == 0:
                    process_lable.configure(text=f'попытки законичились')
                    inf_lable.configure(text='ВЫ ПРОИГРАЛИ!')
                    btn_play.configure(text='игра')
                else:
                    process_lable.configure(text=f'осталось {process} попыток')
                    inf_lable.configure(text='ведите cледующее четырехзначное число\n'
                                             'без повторяющихся цифр:')


    elif btn_play["text"] == 'игра':
        try_box.delete(1.0, tkinter.END)
        key_number = createnum.generator_number()
        inf_lable.configure(text='ведите четырехзначное число\n'
                                 'без повторяющихся цифр:')
        btn_play.configure(text='проверить')
        process = 10



window = tkinter.Tk()

window.geometry('500x300')
window.title('bulls and cows')

bull_lable = tkinter.Label(window, text = 'bull: ')
process_lable = tkinter.Label(window, text = '')
cow_lable = tkinter.Label(window, text = 'cow: ')
inf_lable = tkinter.Label(window, text = '')
try_box = scrolledtext.ScrolledText(window, width = 10, height = 10)
txt = tkinter.Entry(window, width  = 4)
btn_play = tkinter.Button(window, text='игра', command=clicked)

bull_lable.grid(column = 0, row = 0)
process_lable.grid(column = 0, row = 3)
cow_lable.grid(column = 1, row = 0)
inf_lable.grid(column = 1, row = 1)
btn_play.grid(column = 0, row = 1)
txt.grid(column = 0, row = 2)
try_box.grid(column = 0, row = 4)


window.mainloop()




