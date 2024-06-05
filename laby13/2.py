

from collections import defaultdict

def NaiveMatch(P, T):
   for s in range(len(T)-len(P)+1):
      for q in range(len(P)):
         if P[q]!=T[s+q]: break
      else: return True
   return False


def ComputeDelta(P):
   Sigma = set(P) # symbole występujące we wzorcu będą reprezentowane explicite
   delta = defaultdict(int) # przy innych symbolach zawsze wracamy do stanu 0
   for q in range(len(P)+1):
      for x in Sigma:
         r = min(q+1, len(P))
         while r>0 and P[:r] != P[q-r+1:q]+x:
            r -= 1
         delta[q, x] = r
   return delta

def AutoMatch(P, T):
   delta = ComputeDelta(P)
   q = 0
   for x in T:
      q = delta[q, x]
      if q==len(P):
         return True
   return False


def PSTable(P):
   PS = [-1]
   q = -1
   for x in P:
      while q>=0 and P[q]!=x:
         q = PS[q]
      q += 1
      PS.append(q)
   return PS

def KMPMatch(P, T):
   PS = PSTable(P)
   print(PS)
   q = 0
   for x in T:
      while q>=0:
         if P[q]==x:
            q += 1
            break
         q = PS[q]
      if q==len(P):
         return True
      q = max(0, q)
   return False


T = "abaabab"
P = "abab"
print(NaiveMatch(P, T), AutoMatch(P, T), KMPMatch(P, T))
P = "abaaabab"
T = 'abaaabaaba'
print(NaiveMatch(P, T), AutoMatch(P, T), KMPMatch(P, T))
