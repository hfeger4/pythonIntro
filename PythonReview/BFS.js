function BFS(root){
  if(root === null){
    return;
  }

  var queue = [];
  queue.push(root);

  while(queue.length > 0){
    var currentNode = queue[0];

    if (currentNode.left !== null){
      queue.push(currentNode.left);
    }

    if (currentNode.right !== null){
      queue.push(currentNode.right);
    }

    queue.shift();
  }
}
