import tkinter as tk
from tkinter import ttk
import courseParser
import majorParser

# root window
root = tk.Tk()
root.geometry('600x400')
root.resizable(False, False)
root.title('CLI GUI')

# Title Labels for the graphviz GUI and CourseSearch
page2text = tk.Label(root, text="Graphviz")
page1text = tk.Label(root, text="CourseSearch")
page1text.config(font=('helvetica', 20))
page2text.config(font=('helvetica', 20))
 

# function for the course search function page
def course_search_page():
    page1text.pack()

    code = tk.Label(root, text='Course Code')
    code.pack()

    code_entry = tk.Entry (root) 
    code_entry.pack()

    year = tk.Label(root, text='Year')
    year.pack()

    year_entry = tk.Entry (root) 
    year_entry.pack()

    credit_count = tk.Label(root, text='Credit Count')
    credit_count.pack()

    credit_entry = tk.Entry (root) 
    credit_entry.pack()

    semester = tk.Label(root, text='Semester')
    semester.pack()

    semester_entry = tk.Entry (root) 
    semester_entry.pack()

    # function to destroy curr page when moving to a new page
    def destroy_page1():
        back_button.destroy()
        page1text.pack_forget()
        code.pack_forget()
        code_entry.pack_forget()
        year.pack_forget()
        year_entry.pack_forget()
        credit_count.pack_forget()
        credit_entry.pack_forget()
        semester.pack_forget()
        semester_entry.pack_forget()
        search_button.destroy()

    search_button = ttk.Button(
        root,
        text='Search!',
        command =lambda:[]
    )

    search_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    back_button = ttk.Button(
        root,
        text='Return Home',
        command =lambda:[ destroy_page1(), main()]
    )

    back_button.pack(
        ipadx=80,
        ipady=3,
        expand=True
    )


    
# function for the create graphviz function page
def graphviz_page():

    # function to destroy curr page when moving to a new page
    def destroy_page2():
        back_button.destroy()
        page2text.pack_forget()
        course_button.destroy()
        major_button.destroy()

    page2text.pack()

    course_button = ttk.Button(
        root,
        text='Make Course Graph',
        command =lambda:[ destroy_page2(), graph_course_page()]
    )
    course_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    major_button = ttk.Button(
        root,
        text='Make Major Graph',
        command =lambda:[ destroy_page2(), graph_major_page()]
    )

    major_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    back_button = ttk.Button(
        root,
        text='Return Home',
        command =lambda:[ destroy_page2(), main()]
    )
    back_button.pack(
        ipadx=80,
        ipady=3,
        expand=True
    )

def graph_course_page():
    page2text.pack()

    # function to destroy curr page when moving to a new page
    def destroy_page3():
        back_button.destroy()
        page2text.pack_forget()
        course.pack_forget()
        course_entry.pack_forget()
        create_button.destroy()

    course = tk.Label(root, text='Enter Course Code')
    course.pack()

    course_entry = tk.Entry (root) 
    course_entry.pack()

    # function which will be called when graph create button is pressed
    def create_graph():
        course_info = course_entry.get().lower()
        courseParser.getGraphvizInput(course_info)

    # Button to complete creation of graph
    create_button = ttk.Button(
        root,
        text='Create!',
        command =lambda:[create_graph(), destroy_page3(), main()]
    )

    create_button.pack(
        ipadx=80,
        ipady=3,
        expand=True
    )

    back_button = ttk.Button(
        root,
        text='Return Home',
        command =lambda:[ destroy_page3(), main()]
    )

    back_button.pack(
        ipadx=80,
        ipady=3,
        expand=True
    )
    


def graph_major_page():
    page2text.pack()
    
    # function to destroy curr page when moving to a new page
    def destroy_page4():
        back_button.destroy()
        page2text.pack_forget()
        major.pack_forget()
        major_entry.pack_forget()
        create_button.destroy()

    major = tk.Label(root, text='Enter Major')
    major.pack()

    major_entry = tk.Entry (root) 
    major_entry.pack()

    # function which will be called when graph create button is pressed
    def create_graph():
        major_info = major_entry.get().upper()
        majorParser.read_major(major_info)

    # Button to complete creation of graph
    create_button = ttk.Button(
        root,
        text='Create!',
        command =lambda:[create_graph(), destroy_page4(), main()]
    )

    create_button.pack(
        ipadx=80,
        ipady=3,
        expand=True
    )
    
    back_button = ttk.Button(
        root,
        text='Return Home',
        command =lambda:[ destroy_page4(), main()]
    )

    back_button.pack(
        ipadx=80,
        ipady=3,
        expand=True
    )

    


def main():
    # Course Search Button
    cs_button = ttk.Button(
        root,
        text='CourseSearch',
        command =lambda:[ exit_button.destroy(), cs_button.destroy(),gv_button.destroy(), course_search_page()]
    )

    cs_button.pack(
        ipadx=5,
        ipady=5,
        expand=True
    )

    # Graphviz button
    gv_button = ttk.Button(
        root,
        text='Graphviz',
        command =lambda:[ exit_button.destroy(), cs_button.destroy(),gv_button.destroy(), graphviz_page()]
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
        ipadx=80,
        ipady=3,
        expand=True
    )

    root.mainloop()

if __name__ == "__main__":
    main()
