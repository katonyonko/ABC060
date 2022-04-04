from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="060"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc073_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N,W=map(int,input().split())
  ob=[list(map(int,input().split())) for _ in range(N)]
  dp=[[[0]*(N*3+1) for j in range(N+1)] for i in range(N+1)]
  for i in range(N):
    for j in range(N+1):
      for k in range(N*3+1):
        dp[i+1][j][k]=dp[i][j][k]
        r=ob[i][0]-ob[0][0]
        if r<=k and j>0:
          dp[i+1][j][k]=max(dp[i+1][j][k],dp[i][j-1][k-r]+ob[i][1])
  print(max([dp[-1][i][j] for i in range(N+1) for j in range(N*3+1) if i*ob[0][0]+j<=W]))
  """ここから上にコードを記述"""

  print(test_case[__+1])