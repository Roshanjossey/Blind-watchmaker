import string
import random
import time

CharList = string.ascii_lowercase + string.ascii_uppercase + string.digits + '|()_-,;*.+/ \\\''
target = ['              (()          ',
'              ())          ',
'              (()          ',
'              ())          ',
'              (()          ',
'              ())          ',
'              (()          ',
'              ())          ',
'              (()          ',
'              .+.          ',
'          _.-//_\\\\-._      ',
'        .\'.-\' XII \'-.\'.    ',
'      /`.\'*         *\'.`\\  ',
'     / /*        /    *\ \\ ',
'    | ;        _/       ; |',
'    | |IX     (_)    III| |',
'    | ;         \\       ; |',
'     \\ \\*        \\    */ / ',
'      \\ \'.*       \\ *.\'./  ',
'       \'._\'-.__VI_.-\'_.\'   ',
'          \'-.,___,.-\'      ']
for x in target:
  print(x)
