import sys 
import smtplib
import getpass

print(70*"-")

class MainClass():
    def __init__ (self):
        pengirim_email = input("Email Pengirim (From)   : ")
        pass_pengirim = getpass.getpass("Password (Pass)\t\t: ")
        coba = open('receiver_list.txt', 'a')
        jawab = "ya"
        while jawab == "ya" :
            coba.write(input("Email Penerima \t\t: "))
            coba.write("\n")
            jawab = input("Apakah ingin menambah email lagi?(ya/tidak) : ")
        coba.close()
        subject = input("Subjek \t\t\t: ")
        header = "Subject : {}".format(subject)
        pesan = input("Pesan \t\t\t: ")

        combine_msg = header + "\n\n" + pesan

        try : 
            smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
            smtp_object.connect("smtp.gmail.com", 587)
            smtp_object.ehlo()
            smtp_object.starttls()
            smtp_object.login(pengirim_email, pass_pengirim)
            print("Berhasil Login!")
            file_baca = open('receiver_list.txt', 'r')
            penerima = file_baca.readlines()
            for penerima_email in penerima :
                smtp_object.sendmail(pengirim_email, penerima_email, combine_msg)
            file_baca.close()
            print("Email berhasil terkirim!")
            smtp_object.quit()

        except smtplib.SMTPException :
            print("Email gagal terkirim!")

""" __name__ ketika di run pada file ini akan menghasilkan __main__ , 
tetapi ketika di run pada file lain (test.py) akan menghasilkan nama file ini yaitu final_project"""

if __name__ == "__main__" :
    MainClass()
    print(70*"-")
    sys.exit()


"""
referensi : https://youtu.be/8AHGyp2AgNk
            https://youtu.be/sXjpkcF7rPQ  
            https://youtu.be/AURwCHb7BSo  
            https://www.petanikode.com/python-file/
"""

