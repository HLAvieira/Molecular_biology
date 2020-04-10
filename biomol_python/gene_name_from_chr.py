#from a NCBI annotation of a chromossome, returns all gene names. Inputs: file path and file format
from Bio import SeqIO
list_of_chriii_syn_genes = []
def gene_name_from_chr(file_path, file_format):
    path = file_path
    format = file_format
    for seq_record in SeqIO.parse(path, format):
        i = int(seq_record.description.find('gene='))
        f = int(seq_record.description.find(']'))
        print(seq_record.description[i+5: f])
gene_name_from_chr("C:\Biopyhton_files\chriii_syn.fasta", "fasta")

