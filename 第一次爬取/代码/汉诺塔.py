def hanoi(n,x,y,z):
  if n == 1:
    print(x,'-->',z)
  else:
    # 将上面n-1个盘子从 x 移动到 y上
    hanoi(n-1,x,z,y)
    # 然后把最下面的一个 移动到z
    print(x,'-->',z)
    # 在把 y 上的 n-1个盘子移动到 z上
    hanoi(n-1,y,x,z)
num = int(input('输入汉诺塔层数'))
hanoi(num,'X','Y','Z')