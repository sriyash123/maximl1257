from collections import defaultdict
import sys
def SmallestSubString (d):
  x_count = len(set(list(d)))
  m = len(d)
  f = defaultdict(int)
  s_id = 0
  m_len = sys.maxsize
  distinct_till_here = 0 
  for j in range(m):
    f[d[j]] += 1
    if f[d[j]] == 1:
      distinct_till_here += 1
    
    if x_count == distinct_till_here:
      while f[d[s_id]] > 1:
        if f[d[s_id]] > 1:
          f[d[s_id]] -= 1
        s_id += 1
      
      curr_len = j - s_id + 1
      m_len = min(m_len, curr_len)
  return m_len
 
 
    
 
d = input()
 
u = SmallestSubString(d)
print (u)
