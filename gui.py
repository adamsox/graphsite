import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('CLI GUI')


page2text = tk.Label(root, text="CourseSearch")
page1text = tk.Label(root, text="Graphviz")



def page1():
    page2text.pack_forget()
    page1text.pack()

    back_button = ttk.Button(
        root,
        text='Back',
        command =lambda:[ back_button.destroy(), page1text.pack_forget(), main()]
    )
    back_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )


    

def page2():

    page1text.pack_forget()
    page2text.pack()
    back_button = ttk.Button(
        root,
        text='Back',
        command =lambda:[ back_button.destroy(), page2text.pack_forget(), main()]
    )
    back_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )


def main():
    # exit button
    cs_button = ttk.Button(
        root,
        text='CourseSearch',
        command =lambda:[ exit_button.destroy(), cs_button.destroy(),gv_button.destroy(), page1()]
    )

    cs_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # exit button
    gv_button = ttk.Button(
        root,
        text='Graphviz',
        command =lambda:[ exit_button.destroy(), cs_button.destroy(),gv_button.destroy(), page2()]
    )

    gv_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # exit button
    exit_button = ttk.Button(
        root,
        text='Exit',
        command=lambda: root.quit()
    )

    exit_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    root.mainloop()

if __name__ == "__main__":
    main()
