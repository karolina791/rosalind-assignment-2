from Bio import Phylo
import io

distances=""


file = open('rosalind_nwck1.txt','r')
data = [i.split('\n') for i in file.read().strip().split('\n\n')]


for pre_tree, pair in data:
    x,y = pair.split()
    tree = Phylo.read(io.StringIO(pre_tree),'newick')
    for clade in tree.find_clades():
        clade.branch_length = 1
    distances= distances+ ' '+ str(tree.distance(x,y))
    
print (distances)