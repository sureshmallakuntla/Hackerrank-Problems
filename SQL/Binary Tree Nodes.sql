# Binary Tree Nodes
select N, t from (
select N, 'Root' as t from BST where P is null 
union 
select P, 'Inner' from BST where P not in (select N from BST where P is null) 
union 
select N, 'Leaf' from BST where N not in (select P from BST where P is not NULL group by P) 
) a order by N
