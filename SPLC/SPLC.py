from Bio import SeqIO
from Bio.Seq import Seq

all_seq=[]
introns_seq=[]
introns=[]
DNA1=""
for seq_record in SeqIO.parse("rosalind_splc.txt", "fasta"):
    all_seq.append(seq_record.seq)
    

DNA1=str((all_seq[0]))

introns_seq=all_seq[-(len(all_seq)-1):]

H=DNA1

for i in introns_seq:
    introns.append(str(i))
    
for j in range (len(introns)):
    introns[j]=introns[j].strip('\\')
    introns[j]=introns[j].strip('}')
    DNA1= DNA1.replace(introns[j],'')
    
    
    
print (Seq(DNA1).translate())