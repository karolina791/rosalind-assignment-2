edges=[]
with open('rosalind_tree.txt', 'r') as data:
    for number in data:
        number= number.strip('\n')
        edges.append(number)

nodes=edges.pop(0)
nodes=int(nodes)

n_edges=len(edges)

edges_required= nodes-1

lack_edges= edges_required-n_edges
    





print(lack_edges)
    
