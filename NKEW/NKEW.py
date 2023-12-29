from Bio import Phylo
import io

distances=""


file = open('rosalind_nkew.txt','r')
data = [i.split('\n') for i in file.read().strip().split('\n\n')]


for pre_tree, pair in data:
    x,y = pair.split()
    tree = Phylo.read(io.StringIO(pre_tree),'newick')
    distances= distances+ ' '+ str(int(tree.distance(x,y)))
    
print (distances)