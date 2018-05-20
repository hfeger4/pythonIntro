def three_integers(arr)
  arr = arr.sort
  first = arr[0] * arr[1] * arr[-1]
  second = arr[-3] * arr[-2] * arr[-1]
  return [first,second].max
end

p three_integers([1,2,3,4,5,6,2,3,4,22,3])
p three_integers([1,2,3,4,5,6,2,3,4,-22,3])

#time complexity O(nlogn) logn due to the constant division and n times to recreate the stack.
def merge_sort(arr)
  return arr if arr.length == 1

  mid = arr.length/2
  left = arr.drop(mid)
  right = arr.take(mid)

  sorted_left = merge_sort(left)
  sorted_right = merge_sort(right)
  return merge(sorted_left,sorted_right)
end

def merge(left,right)
  arr = []
end
