from Bio import SeqIO
from Bio.Seq import reverse_complement
seq_list=[]
matched=[]
to_correct=[]
corrected=[]


for seq_record in SeqIO.parse('rosalind_corr.txt', 'fasta'):
    seq_list.append(seq_record.seq)
    

for i in range (len(seq_list)):
    current_seq=seq_list.pop(0)
    
    if current_seq in seq_list or reverse_complement(current_seq)in seq_list:
        matched.append(str(current_seq))
        matched.append(str(reverse_complement(current_seq)))
    
    else:
        to_correct.append(str(current_seq))

     
for match in matched:
    for t_c in to_correct:
        paired= zip(t_c, match)
        counter=0
            
        for tc, m in paired:
            if tc != m:
                counter= counter+1
           
                
        if counter==1:
            pair= ((t_c.strip("'"))+'->'+(match.strip("'")))
            
            
            if pair not in corrected:
                corrected.append(pair)
                with open('corr.txt', 'a') as file:
            
                    print((t_c.strip("'"))+'->'+(match.strip("'")),file=file)