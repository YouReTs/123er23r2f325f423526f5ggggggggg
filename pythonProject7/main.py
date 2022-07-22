# jangan ganti , hargai creator

import PORT
from PORT.albania import *
from PORT.argentina import *
from PORT.bangladesh import *
from PORT.brazil import *
from PORT.bulgaria import *
from PORT.canada import *
from PORT.china import *
from PORT.colombia import *
from PORT.germany import *
from PORT.india import *
from PORT.indonesia import *
from PORT.singapore import *
from PORT.thailand import *
from PORT.ukraine import *
from PORT.unitedkingdom import *
from PORT.unitedstates import *
import requests, os, re
from time import sleep


def main():
    os.system('clear')
    print("|                        https://github.com/kancotdiq      - versi 1          |")
    print("\n[01] "
          "\n[02] Argentina"
          "\n[03] Bangladesh"
          "\n[04] Brazil"
          "\n[05] Bulgaria"
          "\n[06] Canada"
          "\n[07] China"
          "\n[08] Colombia"
          "\n[09] Germany"
          "\n[10] India"
          "\n[11] Indonesia"
          "\n[12] Singapore"
          "\n[13] Thailand"
          "\n[14] Ukraine"
          "\n[15] United Kingdom"
          "\n[16] United States"
          "\n[99] Keluar")

    select = input("proxy_select~#:")
    if select == "1":
        albania()
    elif select == "2":
        argentina()
    elif select == "3":
        bangladesh()
    elif select == 4:
        brazil()
    elif select == 5:
        bulgaria()
    elif select == 6:
        canada()
    elif select == 7:
        china()
    elif select == 8:
        colombia()
    elif select == 9:
        germany()
    elif select == 10:
        india()
    elif select == 11:
        indonesia()
    elif select == 12:
        singapore()
    elif select == 13:
        thailand()
    elif select == 14:
        ukraine()
    elif select == 15:
        unitedkingdom()
    elif select == 16:
        unitedstates()
    elif select == 99:
        print("Keluar ...")
        os.sys.exit()
    else:
        print("Опции отсутствуют ...")
        sleep(1)
        print("Keluar ...")
        os.sys.exit()


if __name__ == "__main__":
    main()
