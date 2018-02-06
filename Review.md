<!-- MarkdownTOC -->

- [Breadth-First Search](#breadth-first-search)
- [DFS](#dfs)
- [Binary Trees](#binary-trees)

<!-- /MarkdownTOC -->


<a name="breadth-first-search"></a>

# Breadth-First Search

[Largest value in each row of a binary tree](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/)
```python
row = [root]
while any(row):
    ## doing something for node in row
    # update row 
    row = [kid for node in row for kid in (node.left, node.right) if kid]

```

```
* whiten all node except the root 
* push root into the queue
* while queue is not empty 
    u = dequeue 
    add all white children of u into queue 
    process queue 
```
<a name="dfs"></a>

# DFS 

[Longest path in matrix](https://discuss.leetcode.com/topic/66065/python-dfs-bests-85-tips-for-all-dfs-in-matrix-question)

<a name="binary-trees"></a>

# Binary Trees 



## defaultdict
https://www.accelebrate.com/blog/using-defaultdict-python/



## Strings/array 
- str.strip(), str.lstrip(), str.rstrip() 
- str.join(), str.split 
- a[i:] always valid even if i > len(a) -1
