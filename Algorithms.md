# Algorithms



### A* Pathfinding

```pseudocode
// f_cost for a grid
f_cost(node) = f_cost(node) + (dist(node, current) + dist(node, target))

// f_cost for a graph
f_cost(node) = f_cost(node) + (weight(node, current) + weight(node, target))


// All nodes f_cost() value inizialized in 0
OPEN //the set of nodes to be evaluated
CLOSED //the set of nodes already evaluated
add the start node to OPEN
 
loop
        current = node in OPEN with the lowest f_cost
        remove current from OPEN
        add current to CLOSED
 
        if current is the target node //path has been found
                return
 
        foreach neighbour of the current node
                if neighbour is not traversable or neighbour is in CLOSED
                        skip to the next neighbour
 
                if new path to neighbour is shorter OR neighbour is not in OPEN
                        set f_cost of neighbour
                        set parent of neighbour to current
                        if neighbour is not in OPEN
                                add neighbour to OPEN
```

