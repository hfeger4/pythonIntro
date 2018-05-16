def fibbonacci(n)
  fibb_arr = [0,1]
  return fibb_arr[n] if n < 2
  count = 2
  while count <= n
    fibb_arr << fibb_arr[-1] + fibb_arr[-2]
    count += 1
  end
  fibb_arr.last
end

p fibbonacci(1)

def dice_5_from_7()
  num = rand(7)
  while num > 5
    num = rand(7)
  end
  num
end

p dice_5_from_7()
