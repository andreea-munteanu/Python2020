import os

"""
1. Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
dat ca parametru.
Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
"""


# works
def sort_by_extension(director) :
    content = [f for f in os.listdir(director) if os.path.isfile(os.path.join(director, f))]
    print("Unsorted: ", content)
    content.sort(key=lambda f : os.path.splitext(f)[1])
    print("Sorted: ", content)


# director = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU"
#
# sort_by_extension(director)

"""
2.	Să se scrie o funcție ce primește ca argumente două căi: director si fișier. 
Implementati functia astfel încât în fișierul de la calea *fișier* să fie scrisă pe câte o linie, calea absolută a 
fiecărui fișier din interiorul directorului de la calea *folder*, ce incepe cu litera A. 
"""


# doesnt work dont know why
def write_on_line(director, file_path) :
    # open file as to write in it
    wfile = open(file_path, 'w')        # file to write in
    for file in os.listdir(director) :  # for every file starting with A in directory:
        if file.startswith("A") :       # write abspath in file on different lines
            wfile.writelines("ana " + os.path.abspath(director))
    wfile.close()                       # Close the file when we’re done!
    # open same file as to read and print it
    rfile = open(file_path, 'r')
    lines = rfile.readlines()
    print(lines)


# directory = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU"
# filepath = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU\write_here\python_lab4.txt"
# write_on_line(directory, filepath)

"""
3. ﻿Să se scrie o funcție ce primește ca parametru un string my_path.
Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul fișierului. 
Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count), sortată 
descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu acea extensie. 
Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru. 
"""


def file_path(my_path: str) :
    if os.path.isfile(my_path) :
        # print(my_path, " is a file")
        with open(my_path, "r") as f :
            file_str = str(f.read())
            f.close()
        last_chr = file_str[-20 :]
        print(last_chr)
    elif os.path.isdir(my_path) :
        # print(my_path, " is a directory")
        # return tuple (extension, count)
        tuples = {}
    else :
        print(my_path, " is a different kind of file")
        exit()


# "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU\Doc1.docs"
# "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU"
# "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU\empty_text.txt"


# filename = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU\empty_text.txt"
# file_path(filename)

"""
4.	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la 
linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista finală. 
"""


# works
def list_of_extensions() :
    dir_path = input()
    if os.path.isdir(dir_path) :
        # print("Is directory")
        extension_list = []
        for f in os.listdir(dir_path) :              # for every file in directory
            if os.path.isfile(os.path.join(dir_path, f)) :
                L = os.path.splitext(f)[1]           # get extension
                if L in extension_list :             # add extension only if it doesnt already exist
                    continue
                else :
                    extension_list.append(L)
        extension_list = sorted(extension_list)  # sort ascendingly
        print(extension_list)
    else :
        print("Error: not a directory")
        return False


# "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU"
# list_of_extensions()

"""
5.	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search, și returneaza o listă
de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul
respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
"""

return_list = []

# uhm close but no
def return_list_to_search(target: str, to_search: str) :
    # return list of files
    print(target)
    try :
        if os.path.isfile(target) :
            with open(target) as file :
                if to_search in file.read() :
                    print(target)
                    # add to list
                    return_list.append(target)
        elif os.path.isdir(target) :
            for f in os.listdir(target) :
                return_list_to_search(f, to_search)
    except ValueError :
        print("Error: special type of file")


# target = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU"
# to_search = "abc"
# return_list_to_search(target, to_search)
# print(return_list)

"""
6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește 
un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea 
fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru
"""


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueNotADirectoryOrFileError(Error):
    """Raised when path is not a directory, nor a file"""
    pass

def callback(Error):
    if Error is ValueNotADirectoryOrFileError:
        raise ValueNotADirectoryOrFileError


def callback_function(target: str, to_search: str, callback) :
    # return list of files
    print(target)
    try :
        if os.path.isfile(target) :
            with open(target) as file :
                if to_search in file.read() :
                    print(target)
                    # add to list
                    return_list.append(target)
        elif os.path.isdir(target) :
            for f in os.listdir(target) :
                return_list_to_search(f, to_search)
    except Error :
        print("Error: special type of file")
        callback(Error)


"""
7.	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișier si 
returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea 
fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca 
se poate citi din/scrie in fisier.
"""

# full path
# file_size
# file_extension
# can_read
# can_write

# works
def return_dictionary(file_path: str):
    d = {"full_path": os.path.abspath(file_path),
         "file_size": os.path.getsize(file_path),
         "file_extension": os.path.splitext(file_path)[1],
         "can_read": bool(os.access(file_path, os.R_OK)),
         "can_write": bool(os.access(file_path, os.W_OK))
         }
    return d


# file_path_7 = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU\empty_text.txt"
# print(return_dictionary(file_path_7))

""""
8)	Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director 
aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path

Exemplu apel funcție: functie("C:\\director") va returna ["C:\\director\\fisier1.txt", "C:\\director\\fisier2.txt"]

Calea "C:\\director" are pe disc următoarea structură:

C:\\director\\fisier1.txt <- fișier
C:\\director\\fisier2.txt <- fișier
C:\\director\\director1 <- director
C:\\director\\director2 <- director
"""

# not sure root is okay
def all_abs_paths(dir_path):
    if os.path.isdir(dir_path):
        list_ex_8 = []
        # ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # --> D:\Facultate\Anul_3\Python\Labs
        ROOT_DIR = os.path.abspath(os.sep)                                     # --> D:\
        print("The root is: ", ROOT_DIR)
        for f in os.listdir(ROOT_DIR):
            if os.path.isfile(os.path.join(dir_path, f)):
                list_ex_8.append(os.path.abspath(f))
        return list_ex_8
    else:
        print("Error! Not a directory.")
        exit()


dir_path = "D:\Facultate\Anul_3\Python\Labs\Lab4\IGSU"
print(*all_abs_paths(dir_path), sep='\n')