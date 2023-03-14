from IPython.display import display, Math
from numpy import sqrt, round
#
class escrever(object):
  def __init__(self):
     self.nome = None
  
  def mat(self,A):
      cols = ''.join(['r']*A.shape[1])
      str = r'\left[\begin{array}{' + cols + r'}'
      (m,n) = A.shape
      for i in range(m):
        for j in range(n):
          if j<n-1:
            str += '{}'.format(A[i,j]) + '&'
          else:
            str += '{}'.format(A[i,j]) + r'\\'
      return str + r'\end{array}\right]'

  def polos(self,xi,wn,casas=4):
    xi = round(xi,decimals=casas)
    wn = round(wn,decimals=casas)
    display(Math(r'\xi = ' + f'{xi}'))
    display(Math(r'\omega_n = ' + f'{wn}'))
    p = round(-xi*wn+1j*sqrt(1-xi**2),decimals=casas)
    display(Math(r's = ' + f'{p}'))

  def sist(self,A,B,C,D):
      str1 = r'\dot{\mathbf{x}} = ' + self.mat(A) + r'\mathbf{x}'
      str1 += '+' + self.mat(B) + r'\mathbf{u}'
      str2 = r'\mathbf{y} = ' + self.mat(C) + r'\mathbf{x}'
      str2 += ' + ' + self.mat(D) +  r'\mathbf{u}'
      display(Math(str1))
      display(Math(str2))
    


'''import numpy as np
n = np.random.randint(4,6)
p = np.random.randint(1,4)
q = np.random.randint(1,4)

A = np.random.randn(n,n)
B = np.random.randn(n,p)
C = np.random.randn(q,n)
D = np.random.randn(q,p)

print(dispss(A,B,C,D))'''
