# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:58:30 2020

@author: Sridhar
"""

s = input()
s = list(s)
i=0
l=len(s)
while(i<l):
    #print("Printing i at the beginning:",i)
    #print("Printing l at the beginning:",l)
    if(s[i]=='A' or s[i]=='a' or s[i]=='O'or s[i]=='Y'or s[i]=='E'or s[i]=='U'or s[i]=='I'or s[i]=='o'or s[i]=='y'or s[i]=='e'or s[i]=='u'or s[i]=='i'):
        s.remove(s[i])
        #print(s,' ',i)
        #print()
        l=l-1
        #print("Print l after decrement ",l)
        i=i-1
        #print("Print i after decrement ",i)
        
    i=i+1
    #print("Printing i after incrementing ",i)
i=1
#s[0]='.'
while(i<=len(s)):
    s.insert(i-1,'.')
    i=i+2
for i in range(len(s)):
    if(s[i]>=chr(65) and s[i]<=chr(90)):
        s[i]=chr(ord(s[i])+32)
s=''.join(s)
print(s)