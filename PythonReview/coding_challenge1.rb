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
