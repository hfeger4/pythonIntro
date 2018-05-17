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

p fibbonacci(10)

def fib_rec(n)
  return 0 if n == 0
  return 1 if n == 1
  return fib_rec(n-1) + fib_rec(n-2)
end

p "fib_rec"
p fib_rec(10)

def dice_5_from_7()
  num = rand(7)
  while num > 5
    num = rand(7)
  end
  num
end

p dice_5_from_7()

def dice_7_from_5()
  num1 = rand(7)
  while num1 > 3.5
    num1 = rand(7)
  end
  num2 = rand(7)
  while num2 > 3.5
    num2 = rand(7)
  end
  return num1 + num2
end

p dice_7_from_5()

def roll7_twice()
  num = 25
  while num > 21
    roll1 = rand(5)
    roll2 = rand(5)

    num = ((roll1-1) * 5 + roll2)
  end
  return num%7 + 1
end
p "Roll 7 twice"
p roll7_twice

def string_reverse(str)
  return "" if str.length == 0
  str[-1] + string_reverse(str[0..-2])
end

p string_reverse("hello")

def my_sqrt(num)
  return "error" if num < 0
  return 1 if num == 1
  k = num/2
  while k > 1
    if (k * k) <= num
      return k
    end
    k -= 1
  end
  k
end

p my_sqrt(16)

def better_sqrt(num)
  return "error" if num < 0
  return 1 if num == 1

  low = 0
  high = (num/2)+1
  while low+1 < high
    mid = low + (high-low)/2
    square = mid ** 2

    if square == num
      return mid
    elsif square < num
      low = mid
    else
      high = mid
    end
  end
  return low
end

p better_sqrt(16)
