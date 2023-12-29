from Bio import SeqIO
import networkx as nx

ids=[]
sequences=[]
dict_seq={}
seq_overlap=nx.DiGraph()

for seq_record in SeqIO.parse("rosalind_grph.txt", "fasta"):
    ids.append(seq_record.id)
    seq_record= str(seq_record.seq)
    seq_record= (seq_record.strip('\\'))
    seq_record= seq_record.strip('}')
    sequences.append(seq_record)

ids_s=[]

for i in ids:
    i=i.strip('\\')
    ids_s.append(i)
    

for seq in sequences:
    seq_beg= seq[:3]
    seq_end= seq[-3:]
        
    for seq1 in sequences:
        seq_beg1= seq1[:3]
        seq_end1= seq1[-3:]
            
                
        if seq_beg1==seq_end and seq!=seq1:
            x=sequences.index(seq)
            y=sequences.index(seq1)
            id1=ids_s[x]
            id2=ids_s[y]
            seq_overlap.add_edge(id1,id2)  
            

            
            
list_overlap=nx.edges(seq_overlap)

for i in list_overlap:
    for j in range(len(i)-1):
        print(i[j] + ' ' + i[j+1])