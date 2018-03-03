'''
    pySHF8 main module
    (C) 2017 MMGISS,2018 apple502j All rights reserved.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


def c(p,q):
    # Scratch-like Array
    try:
        return p[q-1]
    except IndexError:
        return ""
def intn(s):
    # Int or ""
    if s=="":
        return ""
    else:
        return int(s)

def intz(s):
    # Int or 0
    try:
        return int(s)
    except:
        return 0

def SHF8Core(S_str):
    S_return=""
    if len(S_str)>0:
        S_char="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()-^¥@[;:],./=~|`{+*}<>? ｢｣､｡･_"
        S_numstr=""
        S_1=0
        for PL_0 in range(len(S_str)):
            S_1 += 1
            S_2=0
            while c(S_char,S_2) != c(S_str,S_1):
                S_2+=1
                if c(S_char,S_2) == c(S_str,S_1):
                    break
            if len(str(S_2)) == 1:
                S_2="0"+str(S_2)
            S_numstr+=str(S_2)
        while len(S_numstr)%16 != 0:
            S_numstr+="00"
        S_1=0
        S_hashvalues=[]
        for PL_1 in range(round(len(S_numstr)/16)):
             S_hashvalues.append("")
             for PL_2 in range(16):
                 S_1+=1
                 S_hashvalues[len(S_hashvalues)-1]=S_hashvalues[len(S_hashvalues)-1]+c(S_numstr,S_1)
        S_hashsearchnums=[-11,-7,-5,-2,-1,0,1,2,5,7,11]
        for PL_3 in range(len(S_hashvalues)):
            S_return=""
            S_numstr=c(S_hashvalues,1)
            S_1=0
            for PL_4 in range(16):
                S_1+=1
                S_2=0
                S_3=0
                for PL_5 in range(len(S_hashsearchnums)):
                    S_3+=1
                    S_4=S_1+c(S_hashsearchnums,S_3)
                    if S_4<1:
                        S_4+=16
                    S_2+=int(c(S_numstr,S_4))
                S_numstr+=str((S_2 +1)%10)
                S_return+=str((S_2 +1)%10)
            S_hashvalues.pop(0)
            S_hashvalues.append(S_return)

        S_return=""
        S_1=0
        for PL_6 in range(16):
            S_1+=1

            S_2=intn(c(c(S_hashvalues,S_3),(S_1-1)))
            S_3=0
            for PL_7 in range(len(S_hashvalues)):
                S_3+=1
                S_2=int(intz(S_2) + int(c(c(S_hashvalues,S_3),S_1)))
            S_return+=str(int(S_2)%10)
        S_1=0
        S_numstr=""
        S_char="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()-^¥@[;:],./=~|`{+*}<>?｢｣､｡･_"
        for PL_8 in range(8):
            S_numstr+=c(S_char,(1+intz(str(c(S_return,S_1+1))+str(c(S_return,S_1+2)))))
            S_1 += 2
        S_return=S_numstr
    return S_return

def SHF8(S_str):
    return SHF8Core(SHF8Core(SHF8Core(SHF8Core(S_str))))
