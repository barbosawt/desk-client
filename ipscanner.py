from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Digite o host a ser verificado: ')
   t_IP = gethostbyname(target)
   print ('Iniciando o scan no host: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Porta %d: ABERTA' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)