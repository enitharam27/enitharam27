def rat():
    f = open('enitha.txt','w+')
    f.write('rat')
    f.write('\n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
             f.write(str(i))
        f.write('\n')
    f.close()

def ratcp():
    f = open('enitha.txt','a+')
    f.write('rat column print')
    f.write('\n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
             f.write(str(j))
        f.write('\n')
    f.close()
    

def irat():
    f = open('alvi.txt','a+')
    f.write('inverse rat')
    f.write('\n---------------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
             f.write(str(i))
        f.write('\n')
    f.close()
def iratc():
    f = open('enitha.txt','a+')
    f.write('rat reverse print')
    f.write('\n-----------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
             f.write(str(j))
        f.write('\n')
    f.close()

def upcp():
    f = open('enitha.txt','a+')
    f.write('uppercase column print')
    f.write('\n---------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
             f.write(chr(j+65))
        f.write('\n')
    f.close()

def uprp():
    f = open('enitha.txt','a+')
    f.write('uppercase row print')
    f.write('\n------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
             f.write(chr(i+64))
        f.write('\n')
    f.close()

def lrp():
    f = open('enitha.txt','a+')
    f.write('lowercase row print')
    f.write('\n------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
             f.write(chr(i+96))
        f.write('\n')
    f.close()

def lcp():
    f = open('alvi.txt','a+')
    f.write('lowercase column print')
    f.write('\n---------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
             f.write(chr(i+97))
        f.write('\n')
    f.close()

def latrp():
    f = open('enitha.txt','a+')
    f.write('lat row print')
    f.write('\n----------------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                f.write(' ')
        for k in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
    
def latcp():
    f = open('enitha.txt','a+')
    f.write('lat column print')
    f.write('\n-------------------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                f.write(' ')
        for k in range(0,i):
            f.write(str(k))
        f.write('\n')
    f.close()

def luprp():
    f = open('enitha.txt','a+')
    f.write('lat uppercase row print')
    f.write('\n----------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()

def lupcp():
    f = open('enitha.txt','a+')
    f.write('lat uppercase column print')
    f.write('\n-------------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                f.write(' ')
        for k in range(0,i):
            f.write(chr(k+65))
        f.write('\n')
    f.close()
print(' ')
def llrp():
    f = open('enitha.txt','a+')
    f.write('lat lowercase row print')
    f.write('\n----------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                f.write(' ')
        for k in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()
print(' ')
def llcp():
    f = open('enitha.txt','a+')
    f.write('lat lowercase column print')
    f.write('\n-------------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                f.write(' ')
        for k in range(0,i):
            f.write(chr(k+97))
        f.write('\n')
    f.close()
print(' ')


def uprpp():
    f = open('enitha.txt','a+')
    f.write('uppercase reverse ')
    f.write('\n-----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64)+' ')
        f.write('\n')
    f.close()
print(' ')
def uppp():
    f = open('enitha.txt','a+')
    f.write('uppercase ')
    f.write('\n----------------------\n')
    for i in range(1,6):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64)+' ')
        f.write('\n')
    f.close()
    
print(' ')
def luprpp():
    f = open('enitha.txt','a+')
    f.write('lat uppercase in row reverse ')
    f.write('\n--------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()

def lrpp():
    f = open('enitha.txt','a+')
    f.write('lowercase  in reverse')
    f.write('\n-----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(chr(k+97)+' ')
        f.write('\n')
    f.close()
def lrrr():
    f = open('enitha.txt','a+')
    f.write(' row reverse')
    f.write('\n-----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()

def llcr():
    f = open('enitha.txt','a+')
    f.write('lowercase  column reverse')
    f.write('\n-----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(chr(k+97)+' ')
        f.write('\n')
    f.close()
def ncr():
    f = open('enitha.txt','a+')
    f.write('numbers in column reverse')
    f.write('\n-----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.close()
def nrpp():
    f = open('enitha.txt','a+')
    f.write('numbers reverse  ')
    f.write('\n-----------------------------\n')
    for i in range(5,0,-1):
        for j in range(5,i,-1):
                 f.write(' ')
        for k in range(0,i):
            f.write(str(i)+' ')
        f.write('\n')
    f.close()



if __name__=='__main__':
  rat()
  ratcp()
  iratc()
  irat()
  upcp()
  uprp()
  lrp()
  lcp()
  latrp()
  latcp()
  luprp()
  lupcp()
  llrp()
  llcp()
  uppp()
  uprpp()
  luprpp()
  lrrr()
  lrpp()
  llcr()
  nrpp()
  ncr()
