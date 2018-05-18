def three_integers(arr)
  arr = arr.sort
  first = arr[0] * arr[1] * arr[-1]
  second = arr[-3] * arr[-2] * arr[-1]
  return [first,second].max
end

p three_integers([1,2,3,4,5,6,2,3,4,22,3])
p three_integers([1,2,3,4,5,6,2,3,4,-22,3])
