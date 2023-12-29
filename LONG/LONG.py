from Bio import SeqIO
from itertools import permutations

seq_list=[]

for seq_record in SeqIO.parse('rosalind_long.txt', 'fasta'):
    seq_record=str(seq_record.seq)
    seq_record=seq_record.strip('}')
    seq_record=seq_record.strip('\\')
    seq_list.append(seq_record)


def overlap(seq1, seq2):
    position=0  
    while True:
        position=seq1.find(seq2[:1], position)  
        if position==-1: 
            return 0

        if seq2.startswith(seq1[position:]):
            return len(seq1)-position
        position += 1 

def max_overlap(seq_list):
    match1= 0
    m_seq1= ''
    m_seq2= ''
    
    for seq1, seq2 in permutations(seq_list, 2):
        match=overlap(seq1, seq2)
        
        if match>match1:
            m_seq1= seq1
            m_seq2= seq2
            match1= match
            
    return m_seq1, m_seq2, match1

def joined(seq_list):
    seq_1, seq_2, match = max_overlap(seq_list)
    
    while match > 0:
        seq_list.remove(seq_1)
        seq_list.remove(seq_2)
        seq_list.append(seq_1 + seq_2[-(len(seq_2) - match):])
        seq_1, seq_2, match = max_overlap(seq_list)
    
    superstring= str(seq_list).replace("'","")
    superstring=superstring.replace("[","")
    superstring=superstring.replace("]","")
    
    
    print (superstring)
    
    
joined(seq_list)