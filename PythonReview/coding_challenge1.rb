def stock_price_profit_max(arr)
  min = arr[0]
  i = 1
  max_profit = 0
  while i < arr.length
    temp_profit = arr[i] - min
    max_profit = max_profit > temp_profit ? max_profit : temp_profit
    min = min < arr[i] ? min : arr[i]
    i += 1
  end
  return max_profit
end

p stock_price_profit_max([10,12,14,12,13,11,8,7,6,13,23,45,11,10])

def mult_except_current(arr)
  ans_arr = []
  i = 0
  while i < arr.length
    temp = arr[i]
    arr[i] = 1
    ans_arr << arr.reduce(:*)
    arr[i] = temp
    i += 1
  end
  ans_arr
end

p mult_except_current([1,2,3,4])

def calc_overlap(coor1,coor2,dim1,dim2)
  greater = [coor1,coor2].max
  lower = [coor1+dim1,coor2+dim2].min

  if greater >= lower
    return [None,None]
  end

  overlap = lower - greater
  return [greater,overlap]
end

def calc_rect_overlap(r1,r2)
  x_overlap, w_overlap = calc_overlap(r1['x'],r1['w'],r2['x'],r2['w'])
  y_overlap, h_overlap = calc_overlap(r1['y'],r1['h'],r2['y'],r2['h'])

  return {'x': x_overlap, 'y': y_overlap,'w': w_overlap,'h': h_overlap}
end
