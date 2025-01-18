"""
VDJ-recombintie opdracht
Autheur: Floris Menninga
Datum: 5-01-2025

"""


heavy_chain = "STKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVGERPAQGGRVSAGSQAQRSCLDASRLCSPSPGQQGRPRLPLHPEASARPTHAQGEG"


def read_seq():

    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    seq_list = []
    start_seq = 0
    stop_seq = 0
    with open("/home/floris/Documenten/vdj_recomb/sequence_file.txt") as seq_text:
        for seq in seq_text: 
            for locatie in range(0, len(seq), 3):
                codon = seq[locatie:locatie + 3]
                if codon in start_codon: # Als het een start codon is...
                    start_seq += 1
                    stop_seq == 0

                if start_seq >= 0 and stop_seq != 1:
                    seq_list.append(codon)
                
                if codon in stop_codons:
                    stop_seq = 1
                else:
                    if stop_seq == 1:
                     print("Nieuw gen...")

                        

        print(seq_list.join(list))




def vdj_recombinatie(): 
    pass


def pn_additie():
    pass

def stop_condon_check():
    pass

def print_resultaat():
    pass


if __name__ == "__main__":
    read_seq()
