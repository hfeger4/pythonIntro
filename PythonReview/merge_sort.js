function merge_sort(arr){
  if(arr.length === 1){
    return arr;
  }
  let mid = Math.floor(arr.length/2);
  let left = arr.slice(0,mid);
  let right = arr.slice(mid);
  let sorted_left = merge_sort(left);
  let sorted_right = merge_sort(right);
  return merge(sorted_left,sorted_right);
}

function merge(left,right){
  const arr = [];
  while(left.length > 0 && right.length > 0){
    if(left[0] < right[0]){
      arr.push(left.shift());
    }else{
      arr.push(right.shift());
    }
  }
  return arr.concat(left).concat(right);
}

console.log(merge_sort([1,3,5,4,2]));
