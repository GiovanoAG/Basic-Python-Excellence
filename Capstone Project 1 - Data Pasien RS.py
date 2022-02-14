# CAPSTONE PROJECT 1
# DATA PASIEN RUMAH SAKIT

# Giovano Aditya Graha
# ======================================================================================================================================
# ======================================================================================================================================

# Library
from tabulate import tabulate
from datetime import date
import sys
import time

# --------------------------------------------------------------------------------------------------------------------------------------

# Default List
list_pasien = [
    {
        'Medical ID': '25',
        'Name': 'Philips',
        'DoB (Y-M-D)': '1989-2-1',
        'Gender': 'Man',
        'Blood Type': 'AB',
        'Diagnose': 'Cancer'
    },
    {
        'Medical ID': '437',
        'Name': 'Michael',
        'DoB (Y-M-D)': '2010-5-22',
        'Gender': 'Man',
        'Blood Type': 'O',
        'Diagnose': 'Patah Tulang'
    },
    {
        'Medical ID': '101',
        'Name': 'Stephanie',
        'DoB (Y-M-D)': '1997-2-27',
        'Gender': 'Woman',
        'Blood Type': 'B',
        'Diagnose': 'Thiroid'
    },
    {
        'Medical ID': '76',
        'Name': 'Marcus',
        'DoB (Y-M-D)': '1990-11-25',
        'Gender': 'Man',
        'Blood Type': 'A',
        'Diagnose': 'Cancer'
    },
]

# Updated List - Default List with Age Column Addition:

list_umur = []
for a in range(len(list_pasien)):
    d_o_b = list_pasien[a]["DoB (Y-M-D)"]

    d_o_b_splitted = d_o_b.split("-")
    dob_date = date(int(d_o_b_splitted[0]),int(d_o_b_splitted[1]),int(d_o_b_splitted[2]))

    now_ = date.today()
    selisih_umur = (now_ - dob_date)//365     # days n time
    umur_ = selisih_umur.days
    list_umur.append(umur_)

for b in range(len(list_pasien)):
    list_pasien[b]["Age"] = list_umur[b]

# (Default list is already updated with Age column)

# ======================================================================================================================================

#                                                                  FUNCTIONS

# --------------------------------------------------------------------------------------------------------------------------------------
# NAME
def name():
    nama_ = str(input('Patient Name\t\t\t: ').title())
    return nama_

# --------------------------------------------------------------------------------------------------------------------------------------
# DATE OF BIRTH & AGE

# Date of Birth
def tanggal_lahir():

    # Year of Birth
    while True:
        dob_tahun = input('\tYear of Birth\t: ')
        if len(str(dob_tahun)) == 4:
            print()
        else:
            print("\tPlease input 4 digit number as your actual Year of birth.")
            continue
        if str(dob_tahun).isnumeric() == False:
            print("\tPlease input 4 digit number as your actual Year of birth.")
            continue

        dob_tahun = int(dob_tahun)
        break

    # Month of Birth    
    while True:
        dob_bulan = input('\tMonth of Birth\t: ')
        if str(dob_bulan).isnumeric() == False:
            print("\tYour Month is invalid, please re-input your actual Month of Birth (1-12).")
            continue 
        elif 1 <= int(dob_bulan) <= 12:
            print()
        else:
            print("\tYour Month is invalid, please re-input your actual Month of Birth (1-12).")
            continue
        
        dob_bulan = int(dob_bulan)
        break

    # Day of Birth
    while True:
        dob_tanggal = input('\tDay of Birth\t: ')
        if str(dob_tanggal).isnumeric() == False:
            print("\tYour Date is invalid, please re-input your actual Day of Birth.")
            continue
        elif dob_bulan == 1 or dob_bulan == 3 or dob_bulan == 5 or dob_bulan == 7 or dob_bulan == 8 or dob_bulan == 10 or dob_bulan == 12:
            if 1 <= int(dob_tanggal) <= 31:
                tgllahir = date(dob_tahun, dob_bulan, int(dob_tanggal))
                print()
                break
            else:
                print("\tYour Date is invalid, please re-input your actual Day of Birth.")
                continue
        elif dob_bulan == 4 or dob_bulan == 6 or dob_bulan == 9 or dob_bulan == 11:
            if 1 <= int(dob_tanggal) <= 30:
                tgllahir = date(dob_tahun, dob_bulan, int(dob_tanggal))
                print()
                break
            else:
                print("\tYour Date is invalid, please re-input your actual Day of Birth.")
                continue
        elif dob_bulan == 2 and dob_tahun%4 == 0:
            if 1 <= int(dob_tanggal) <= 29:
                tgllahir = date(dob_tahun, dob_bulan, int(dob_tanggal))
                print()
                break
            else:
                print("\tYour Date is invalid, please re-input your actual Day of Birth.")
                continue
        elif dob_bulan == 2:
            if 1 <= int(dob_tanggal) <= 28:
                tgllahir = date(dob_tahun, dob_bulan, int(dob_tanggal))
                print()
                break
            else:
                print("\tYour Date is invalid, please re-input your actual Day of Birth.")
                continue

        dob_tanggal = int(dob_tanggal)

    print(f"Date of Birth (Y-M-D)\t\t: {tgllahir}")
    tgl_lahir = str(tgllahir)

    # Age
    now = date.today()
    selisih = (now - tgllahir)//365
    umur = selisih.days
    print(f"\tAge\t\t\t: {umur}")

    return tgl_lahir, umur

# --------------------------------------------------------------------------------------------------------------------------------------
# GENDER
def jenis_kelamin():
    while True:
        jk = str(input("Gender (M/W)\t\t\t: ")).lower()
        if jk == "m":
            gender = "Man"
            break
        elif jk == "w":
            gender = "Woman"
            break
        else:
            print("Please input according to the instructions.")
            continue
    return gender

# --------------------------------------------------------------------------------------------------------------------------------------
# BLOOD TYPE
def golongan_darah():
    while True:
        goldar = str(input("Blood Type (A/B/O/AB)\t\t: ")).upper()
        if goldar == "A" or goldar == "B" or goldar == "O" or goldar == "AB":
            break
        else:
            print("Please input according to the instructions.")
            continue
    return goldar

# --------------------------------------------------------------------------------------------------------------------------------------
# DIAGNOSE
def diagnose():
    penyakit = str(input("Diagnose\t\t\t: ")).title()
    return penyakit

# ======================================================================================================================================

# SUB MENU(s)

# --------------------------------------------------------------------------------------------------------------------------------------
# Sub - Menu 1
def sub_menu_1():
    print('''
    ++++++++++ Record List Patient(s) Data ++++++++++

    1.\t List Patient(s) Data
    2.\t Report Specified Data
    3.\t Back to Main Menu
    ''')

# --------------------------------------------------------------------------------------------------------------------------------------
# Sub - Menu 2
def sub_menu_2():
    print('''
    ++++++++++ Add and Create Data ++++++++++

    1.\t Add Data
    2.\t Back to Main Menu
    ''')

# --------------------------------------------------------------------------------------------------------------------------------------
# Sub - Menu 3
def sub_menu_3():
    print('''
    ++++++++++ Delete Data ++++++++++

    1.\t Delete Data
    2.\t Back to Main Menu
    ''')

# --------------------------------------------------------------------------------------------------------------------------------------
# Sub - Menu 4
def sub_menu_4():
    print('''
    ++++++++++ Update and Change Data ++++++++++

    1.\t Update Patient Data
    2.\t Back to Main Menu
    ''')

# ======================================================================================================================================

# MENU(s)

# --------------------------------------------------------------------------------------------------------------------------------------
# START
def halo():

    fill_text = "\033[47m\033[30m"
    reset_fill = "\033[0m"
    print(f"\n\t{fill_text} ===== WELCOME TO PURWADHIKA JCDS 1602 HOSPITAL BSD ====={reset_fill}\n")
    print("Please find list Menu below, ")
    tablehalo = [["1)", "List Patient Data"],["2)","Add and Create Data"],["3)","Delete Data"],["4)","Update and Change Data"],["5)","Exit Program"]]
    print(tabulate(tablehalo))
    print()

# --------------------------------------------------------------------------------------------------------------------------------------
# 1. READ DATA
def list_data(list_pasien):

    table = []
    headers = ["Medical ID","Name", "DoB (Y-M-D)","Age","Gender","Blood Type","Diagnose"]

    if len(list_pasien) == 0:
        print("Data is empty.")
    else:
        for i in list_pasien:
            table.append(
                [i["Medical ID"],i["Name"],i["DoB (Y-M-D)"],i["Age"],i["Gender"],i["Blood Type"],i["Diagnose"]]
                )
        print("\n---------------- Patient(s) Data Purwadhika JCDS 1602 Hospital BSD ----------------\n")
        print(tabulate(table, headers,tablefmt="pretty"))

# --------------------------------------------------------------------------------------------------------------------------------------
# 1. READ DATA - SPECIFIED DATAA
def list_data_2(list_pasien):

    if len(list_pasien) == 0:
        print("Data is empty.")
    else:
        while True:
            data_tertentu = str(input('Please Input Medical Record ID Number: '))
            table2 = []
            headers2 = ["Medical ID","Name", "DoB (Y-M-D)","Age","Gender","Blood Type","Diagnose"]
            
            for m in list_pasien:
                if m["Medical ID"] == data_tertentu:
                    table2.append(
                        [m["Medical ID"],m["Name"],m["DoB (Y-M-D)"],m["Age"],m["Gender"],m["Blood Type"],m["Diagnose"]]
                        )
                    print(tabulate(table2, headers2,tablefmt="pretty"))
                    break
            else:
                print("Data is not exist.")
            break

# --------------------------------------------------------------------------------------------------------------------------------------
# 2. ADD AND CREATE DATA
def add_data(list_pasien):
    
    #MEDICAL RECORD ID NUMBER
    while True:
        id_ = str(input("Medical Record ID Number\t: "))
        if id_.isnumeric() == True and id_ != "0":
            for c in range(len(list_pasien)):
                if id_ == (list_pasien[c]['Medical ID']):
                    print("Your Medical Record Number is already registered and there might be an error.\nPlease re-enter.")
                    break
            else:
                break
        else:
            print("Please input correct Medical Record ID with integer number format.")
            continue

    #NAMA
    nama_ = name()

    #TANGGAL LAHIR
    tgl_lahir, umur = tanggal_lahir()

    #JENIS KELAMIN
    gender = jenis_kelamin()

    #GOLONGAN DARAH
    goldar = golongan_darah()
    
    #PENYAKIT
    penyakit = diagnose()



    while True:
        konfirmasi = input("Are you sure want to add the data? (Y/N): ").capitalize()
        if konfirmasi == "Y":
            added_data = [(id_), (nama_), (tgl_lahir), (umur), (gender), (goldar), (penyakit)]
            list_pasien.append({
                'Medical ID': added_data[0],
                'Name': added_data[1],
                'DoB (Y-M-D)': added_data[2],
                'Age': added_data[3],
                'Gender': added_data[4],
                'Blood Type': added_data[5],
                'Diagnose': added_data[6]
            })
            list_data(list_pasien)
            break

        elif konfirmasi == "N":
            print("Data is not added.")
            list_data(list_pasien)
            break
        else:
            continue

# --------------------------------------------------------------------------------------------------------------------------------------
# 3. DELETE DATA
def del_data(list_pasien):

    list_data(list_pasien)
    while True:
        unik_id = str(input('Please Input Medical Record ID Number to be deleted: '))
        for d in range(len(list_pasien)):
            if unik_id == list_pasien[d]["Medical ID"]:

                while True:
                    konfirmasi = input("Are you sure want to update? (Y/N): ").capitalize()
                    if konfirmasi == "Y":
                        del list_pasien[d]
                        break
                    elif konfirmasi == "N":
                        print("Data is not deleted.")
                        break
                    else:
                        continue

                list_data(list_pasien)
                break

        else:
            print("Medical Record ID Number is not exist.")
            break
        break

# --------------------------------------------------------------------------------------------------------------------------------------
# 4. UPDATE DATA
def upd_data(list_pasien):

    list_data(list_pasien)
    while True:
        upd_id = str(input('Please Input Medical Record ID Number to be updated: '))
        for e in range(len(list_pasien)):
            if upd_id == list_pasien[e]["Medical ID"]:
                namakolom = list(list_pasien[e].keys())
                print(f'''
                1. {namakolom[1]} to be
                2. {namakolom[2]} to be
                3. {namakolom[3]} to be
                4. {namakolom[4]} to be
                5. {namakolom[5]} to be
                (Input Others to Cancel)
                ''')
                opt_upd = input("Please choose data which will be updated (1-5): ")
                if opt_upd.isnumeric() == False:
                    print("Column Data is Invalid. \nDo you want to update again?")
                    break

                elif int(opt_upd) not in range(1,6):
                    print("Column Data is Invalid. \nDo you want to update again?")
                    break
                
                else:
                    opt_upd = int(opt_upd)
                    if opt_upd == 1:
                        new_value = name()
                    elif opt_upd == 2:
                        new_value, new_age = tanggal_lahir()
                    elif opt_upd == 3:
                        new_value = jenis_kelamin()
                    elif opt_upd == 4:
                        new_value = golongan_darah()
                    elif opt_upd == 5:
                        new_value = diagnose()
                    
                    while True:
                        konfirmasi = input("Are you sure want to update? (Y/N): ").capitalize()
                        if konfirmasi == "Y":
                            list_pasien[e][namakolom[opt_upd]] = new_value
                            if opt_upd == 2:
                                list_pasien[e]["Age"] = new_age
                            break
                        elif konfirmasi == "N":
                            print("Data is not updated.")
                            break
                        else:
                            continue

                list_data(list_pasien)
                break
           
        else:
            print("Medical Record ID Number is not exist.")
            break
        break

# --------------------------------------------------------------------------------------------------------------------------------------
# 5. EXIT PROGRAM
def delay_print(word):

    for huruf in word:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(0.020)

# ======================================================================================================================================

#                                                                   MAIN MENU

# --------------------------------------------------------------------------------------------------------------------------------------
while True:

    halo()

    pilihan_menu = input("Please input Menu (1-5): ")

    if pilihan_menu.isnumeric() == False:
        print("Menu is invalid. Please re-input.")
        continue
# 1.
    elif (int(pilihan_menu) == 1):
        while True:
            sub_menu_1()
            pilihan_sub_menu = input("Please input Sub-Menu (1-3): ")

            if pilihan_sub_menu.isnumeric() == False:
                print("Sub-Menu input is invalid. Please re-input.")
                continue
            elif int(pilihan_sub_menu) == 1:
                list_data(list_pasien)
                continue
            elif int(pilihan_sub_menu) == 2:
                list_data_2(list_pasien)
                continue
            elif int(pilihan_sub_menu) == 3:
                break
            else:
                print("Sub-Menu input is invalid. Please re-input.")
                continue
# 2.   
    elif (int(pilihan_menu) == 2):
        while True:
            sub_menu_2()
            pilihan_sub_menu = input("Please input Sub-Menu (1-2): ")

            if pilihan_sub_menu.isnumeric() == False:
                print("Sub-Menu input is invalid. Please re-input")
                continue
            elif int(pilihan_sub_menu) == 1:
                add_data(list_pasien)
            elif int(pilihan_sub_menu) == 2:
                break
            else:
                print("Sub-Menu input is invalid. Please re-input")
                continue
# 3.        
    elif (int(pilihan_menu) == 3):
        while True:
            sub_menu_3()
            pilihan_sub_menu = input("Please input Sub-Menu (1-2): ")

            if pilihan_sub_menu.isnumeric() == False:
                print("Sub-Menu input is invalid. Please re-input")
                continue
            elif int(pilihan_sub_menu) == 1:
                del_data(list_pasien)
            elif int(pilihan_sub_menu) == 2:
                break
            else:
                print("Sub-Menu input is invalid. Please re-input")
                continue
# 4.        
    elif (int(pilihan_menu) == 4):
        while True:
            sub_menu_4()
            pilihan_sub_menu = input("Please input Sub-Menu (1-2): ")

            if pilihan_sub_menu.isnumeric() == False:
                print("Sub-Menu input is invalid. Please re-input")
                continue
            elif int(pilihan_sub_menu) == 1:
                upd_data(list_pasien)
            elif int(pilihan_sub_menu) == 2:
                break
            else:
                print("Sub-Menu input is invalid. Please re-input")
                continue
# 5.
    elif (int(pilihan_menu) == 5):
        delay_print('''
        \t ~ THANK YOU ~

        (: STAY SAFE AND KEEP HEALTHY :)
        \n''')
        break
    
    else:
        print("Menu is invalid. Please re-input.")

# --------------------------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================================




